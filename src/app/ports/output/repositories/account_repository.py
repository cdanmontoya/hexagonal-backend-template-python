from abc import abstractmethod

from src.app.ports.output.repositories.repository import Repository
from src.domain.model.account import Account, AccountId


class AccountRepository(Repository):
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
