import os

import pika
from aio_pika import connect_robust
from aio_pika.abc import AbstractRobustConnection
from injector import Module, Binder, provider
from pika.adapters.blocking_connection import BlockingConnection
from testcontainers.rabbitmq import RabbitMqContainer

from src.app.ports.input.events.event_consumer import EventConsumer
from src.app.ports.output.events.event_publisher import EventPublisher
from src.infrastructure.adapters.input.events.rabbit_mq_event_consumer import (
    RabbitMqEventConsumer,
)
from src.infrastructure.adapters.output.events.rabbit_mq_event_publisher import (
    RabbitMqEventPublisher,
)


class PublishersModule(Module):
    @provider
    def message_broker_blocking_connection(self) -> BlockingConnection:
        pika.BlockingConnection(
            pika.ConnectionParameters(
                host=os.getenv("MESSAGE_BROKER_HOST", "localhost"),
                port=os.getenv("MESSAGE_BROKER_PORT", 5672),
                heartbeat=0,
            )
        )

    # @provider
    # def message_broker_async_connection(self) -> AbstractRobustConnection:
    #     async with RabbitMqContainer("rabbitmq:3-management-alpine") as rabbitmq:
    #         self._connection = await connect_robust(
    #             host=os.getenv("MESSAGE_BROKER_HOST", "localhost"),
    #             port=int(os.getenv("MESSAGE_BROKER_PORT", 5672)),
    #             login=os.getenv("MESSAGE_BROKER_USER", "guest"),
    #             password=os.getenv("MESSAGE_BROKER_PASS", "guest"),
    #         )
    #         return pika.BlockingConnection(rabbitmq.get_connection_params())

    def configure(self, binder: Binder) -> None:
        binder.bind(interface=EventPublisher, to=RabbitMqEventPublisher)


class ConsumersModule(Module):
    def configure(self, binder: Binder) -> None:
        binder.bind(interface=EventConsumer, to=RabbitMqEventConsumer)
