from abc import abstractmethod, ABC


class Repository[K, T](ABC):
    @abstractmethod
    def get(self, k: K) -> T | None:
        raise NotImplementedError

    @abstractmethod
    def get_all(self) -> list[T]:
        raise NotImplementedError

    @abstractmethod
    def insert(self, t: T) -> T:
        raise NotImplementedError

    @abstractmethod
    def update(self, k: K, t: T) -> T:
        raise NotImplementedError

    @abstractmethod
    def delete(self, key: K) -> T:
        raise NotImplementedError
