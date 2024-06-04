from injector import inject

from src.app.ports.output.repositories.account_repository import (
    AccountRepository,
)
from src.app.queries.get_account_by_id import GetAccountById
from src.domain.model.account import Account


class GetAccountsService:
    __account_repository: AccountRepository

    @inject
    def __init__(self, account_repository: AccountRepository) -> None:
        self.__account_repository = account_repository

    def get(self, get_account: GetAccountById) -> Account | None:
        return self.__account_repository.get(get_account.account_id)

    def get_all(self) -> list[Account]:
        return self.__account_repository.get_all()
