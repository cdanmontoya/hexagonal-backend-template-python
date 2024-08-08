from src.app.ports.output.events.publisher import EventPublisher
from src.domain.events.event import Event
from src.infrastructure.adapters.output.publishers.integration_event import to_json


class RabbitMqEventPublisher(EventPublisher):
    def publish(self, event: Event) -> None:
        print(f"Published event {to_json(event)}")
