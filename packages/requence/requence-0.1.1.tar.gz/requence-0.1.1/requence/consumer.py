from pika.adapters.blocking_connection import BlockingChannel
from pika.spec import Basic, BasicProperties
from typing import Any, TypedDict, Awaitable, Dict, List, Optional, Protocol, cast
from .version import Version
from .context import ContextHelper, Context
from .typing import Service
from .utils import is_valid_uuid, is_valid_version, now
from .exceptions import RetryException, AbortException

import os
import pika
import json
import re
import asyncio

class ConsumerConfig(TypedDict, total=False):
    url: Optional[str]
    version: Optional[str]
    prefetch: Optional[int]

class Meta(TypedDict):
    services: List[Service]

class Payload(TypedDict, total=True):
    context: Context
    meta: Meta

class OnMessageCallback(Protocol):
    def __call__(self, context: ContextHelper) -> Any | None | Awaitable[Any | None]: ...

class Consumer:
    def __init__(self, config: ConsumerConfig, on_message_callback: OnMessageCallback):

        url = config.get("url") or os.getenv("REQUENCE_URL")
        if not isinstance(url, str) or not url.startswith("amqp://"):
            raise ValueError("URL must be an amqp connection string.")

        version = config.get("version") or os.getenv("VERSION")
        if not isinstance(version, str) or not is_valid_version(version):
            raise ValueError("Version must be a valid version")

        prefetch = config.get("prefetch") or 1
        if not isinstance(prefetch, int):
            raise ValueError("Prefetch must be an integer")

        parsed_url = pika.URLParameters(url)

        if not parsed_url.credentials:
            raise ValueError("Url connection string needs a username")

        username = parsed_url.credentials.username

        parameters = pika.URLParameters(url)
        connection = pika.BlockingConnection(parameters)

        queue = username
        exchange = username

        channel = connection.channel()
        channel.exchange_declare(exchange=exchange, passive=True)
        channel.exchange_declare(exchange=exchange + "-retry", passive=True)
        channel.queue_declare(queue=queue, passive=True)
        channel.basic_qos(prefetch_count=prefetch)

        self.__version = Version(version)
        self.__channel = channel
        self.__exchange = exchange
        self.__on_message_callback = on_message_callback
        channel.basic_consume(queue=queue, on_message_callback=self.__on_message)
        channel.start_consuming()

    def close(self):
        self.__channel.stop_consuming()
        self.__channel.close()

    async def __handle_response(self, body: bytes, delivery_tag: int, properties: pika.BasicProperties):
        try:
            correlation_id = properties.correlation_id
            if not is_valid_uuid(correlation_id):
                raise Exception("Invalid or missing correlation ID.")

            payloadData = json.loads(body.decode('utf-8'))
            if not isinstance(payloadData, dict):
                raise ValueError("Context must be a dictionary.")

            payload = cast(Payload, payloadData)
            extended_context = self.__on_message_callback(ContextHelper(correlation_id, payload.get("context"), payload.get("meta").get("services")))

            if (isinstance(extended_context, Awaitable)):
                extended_context = await extended_context

            self.__channel.basic_ack(delivery_tag)
            self.__channel.basic_publish(
                exchange=self.__exchange,
                routing_key="",
                body=json.dumps(extended_context).encode('utf-8'),
                properties=pika.BasicProperties(correlation_id=correlation_id)
            )
        except RetryException as e:
            properties.expiration = str(e.delay or 1000)
            self.__channel.basic_publish(
                exchange=self.__exchange + "-retry",
                routing_key="retry",
                body=body,
                properties=properties
            )
            self.__channel.basic_ack(delivery_tag)
        except AbortException as e:
            message = str(e)
            if (len(message) == 0):
                raise e

            properties.expiration = str(1)
            properties.priority = 0
            properties.content_type = "text/plain"
            properties.headers["error"] = True

            self.__channel.basic_publish(
                exchange=self.__exchange + "-retry",
                routing_key="requeue",
                body=message,
                properties=properties
            )
            self.__channel.basic_ack(delivery_tag)
        except Exception as e:
            print("Encountered an error inside consumer handler:")
            print(str(e))
            self.__channel.basic_nack(delivery_tag, multiple=False, requeue=False)

    def __on_message(self, channel: BlockingChannel, method: Basic.Deliver, properties: BasicProperties, body: bytes):
        try:
            expected_version = properties.headers.get('version')
            if not self.__version.satisfies(expected_version):
                expiration_date = properties.headers.get('original-expiration-date', None)
                if (not expiration_date and properties.expiration):
                    expiration_date = str(now() + int(properties.expiration))

                if (expiration_date and now() > int(expiration_date)):
                    channel.basic_nack(delivery_tag=method.delivery_tag, multiple=False, requeue=False)
                    return

                properties.headers['original-expiration-date'] = expiration_date
                properties.headers['version-mismatch'] = self.__version
                properties.expiration = str(0)

                self.__channel.basic_publish(
                    exchange=self.__exchange + "-retry",
                    routing_key="retry",
                    body=body,
                    properties=properties
                )
                channel.basic_ack(delivery_tag=method.delivery_tag)
                return

            asyncio.run(self.__handle_response(body, method.delivery_tag, properties))

        except Exception as e:
            print(e)
            channel.basic_nack(delivery_tag=method.delivery_tag, multiple=False, requeue=False)
