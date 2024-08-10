from src.app.ports.output.events.event_publisher import EventPublisher
from src.domain.events.event import Event
from src.infrastructure.acl.dto.events.integration_event import to_json


class ConsoleEventPublisher(EventPublisher):
    def publish(self, event: Event) -> None:
        print(to_json(event))
