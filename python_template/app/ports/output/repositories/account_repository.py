from abc import abstractmethod, ABC

from python_template.domain.model.account import Account, AccountId


class AccountRepository(ABC):
    @abstractmethod
    def get(self, key: AccountId) -> Account | None:
        raise NotImplementedError

    @abstractmethod
    def get_all(self) -> list[Account]:
        raise NotImplementedError

    @abstractmethod
    def insert(self, account: Account) -> Account:
        raise NotImplementedError

    @abstractmethod
    def update(self, key: AccountId, account: Account) -> Account:
        raise NotImplementedError

    @abstractmethod
    def delete(self, key: AccountId) -> Account:
        raise NotImplementedError
