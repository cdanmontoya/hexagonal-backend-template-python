from abc import abstractmethod, ABC


class EventConsumer(ABC):
    @abstractmethod
    def run(self):
        raise NotImplementedError
