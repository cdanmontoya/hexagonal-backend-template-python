from injector import Module, Binder

from src.app.ports.input.events.event_consumer import EventConsumer
from src.app.ports.output.events.event_publisher import EventPublisher
from src.infrastructure.adapters.input.events.rabbit_mq_event_consumer import (
    RabbitMqEventConsumer,
)
from src.infrastructure.adapters.output.events.rabbit_mq_event_publisher import (
    RabbitMqEventPublisher,
)


class PublishersModule(Module):
    def configure(self, binder: Binder) -> None:
        binder.bind(interface=EventPublisher, to=RabbitMqEventPublisher)


class ConsumersModule(Module):
    def configure(self, binder: Binder) -> None:
        binder.bind(interface=EventConsumer, to=RabbitMqEventConsumer)
