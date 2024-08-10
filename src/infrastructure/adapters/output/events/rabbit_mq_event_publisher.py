import logging

import pika
from aio_pika.abc import AbstractRobustConnection
from injector import singleton

from src.app.ports.output.events.event_publisher import EventPublisher
from src.domain.events.event import Event
from src.infrastructure.acl.dto.events.integration_event import to_json

logger = logging.getLogger(__name__)


@singleton
class RabbitMqEventPublisher(EventPublisher):
    _connection: AbstractRobustConnection

    def __init__(self) -> None:
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host="localhost", heartbeat=0)
        )
        self._channel = connection.channel()

    def publish(self, event: Event) -> None:
        self._channel.exchange_declare(
            exchange=f"{event.source}.{event.name}",
            exchange_type="fanout",
        )
        self._channel.basic_publish(
            exchange=f"{event.source}.{event.name}", routing_key="", body=to_json(event)
        )
        print(f"Published event {event.name} with id {event.id}")
        logger.info(f"Published event {event.name} with id {event.id}")
