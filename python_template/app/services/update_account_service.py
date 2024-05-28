from uuid import uuid4

from python_template.app.commands.update_account import UpdateAccount
from python_template.app.ports.output.repositories.account_repository import (
    AccountRepository,
)
from python_template.domain.model.account import Account, AccountId
from python_template.domain.model.contact_information import ContactInformation


class UpdateAccountService:
    __account_repository: AccountRepository

    def __init__(self, account_repository: AccountRepository) -> None:
        self.__account_repository = account_repository

    def update(self, update_account: UpdateAccount) -> Account:
        account = Account(
            update_account.id,
            ContactInformation(update_account.email, update_account.cellphones),
        )

        return self.__account_repository.update(update_account.id, account)
