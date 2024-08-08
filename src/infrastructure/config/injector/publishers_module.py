from injector import Module, Binder

from src.app.ports.output.events.publisher import EventPublisher
from src.infrastructure.adapters.output.publishers.rabbitmq_event_publisher import (
    RabbitMqEventPublisher,
)


class PublishersModule(Module):
    def configure(self, binder: Binder) -> None:
        binder.bind(interface=EventPublisher, to=RabbitMqEventPublisher)
