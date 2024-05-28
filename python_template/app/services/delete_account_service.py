from python_template.domain.model.account import Account, AccountId
from python_template.app.ports.output.repositories.account_repository import (
    AccountRepository,
)


class DeleteAccountService:
    __account_repository: AccountRepository

    def __init__(self, account_repository: AccountRepository) -> None:
        self.__account_repository = account_repository

    def delete(self, key: AccountId) -> Account:
        return self.__account_repository.delete(key)
