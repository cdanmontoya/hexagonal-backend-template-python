from uuid import uuid4

from injector import inject

from src.app.commands.insert_account import InsertAccount
from src.app.ports.output.repositories.account_repository import (
    AccountRepository,
)
from src.domain.model.account import Account, AccountId
from src.domain.model.contact_information import ContactInformation


class InsertAccountService:
    __account_repository: AccountRepository

    @inject
    def __init__(self, account_repository: AccountRepository) -> None:
        self.__account_repository = account_repository

    def insert(self, insert_account: InsertAccount) -> Account:
        account = Account(
            AccountId(uuid4()),
            ContactInformation(insert_account.email, insert_account.cellphones),
        )

        return self.__account_repository.insert(account)
