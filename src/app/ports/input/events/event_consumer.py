from abc import abstractmethod, ABC


class EventConsumer(ABC):
    @abstractmethod
    def process_event(self, event):
        pass

