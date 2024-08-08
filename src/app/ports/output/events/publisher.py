import functools
from abc import ABC, abstractmethod

from src.domain.events.event import Event


class EventPublisher(ABC):
    @abstractmethod
    def publish(self, event: Event) -> None:
        raise NotImplementedError


def event_publisher(publisher):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            publisher.publish(result)
            return result
        return wrapper
    return decorator
