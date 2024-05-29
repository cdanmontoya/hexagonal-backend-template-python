from injector import inject

from app.ports.output.repositories.account_repository import (
    AccountRepository,
)
from domain.model.account import Account, AccountId


class DeleteAccountService:
    __account_repository: AccountRepository

    @inject
    def __init__(self, account_repository: AccountRepository) -> None:
        self.__account_repository = account_repository

    def delete(self, key: AccountId) -> Account:
        return self.__account_repository.delete(key)
