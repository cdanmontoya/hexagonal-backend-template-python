from injector import inject

from app.ports.output.repositories.account_repository import (
    AccountRepository,
)
from domain.model.account import Account, AccountId


class GetAccountsService:
    __account_repository: AccountRepository

    @inject
    def __init__(self, account_repository: AccountRepository) -> None:
        self.__account_repository = account_repository

    def get(self, key: AccountId) -> Account | None:
        return self.__account_repository.get(key)

    def get_all(self) -> list[Account]:
        return self.__account_repository.get_all()
