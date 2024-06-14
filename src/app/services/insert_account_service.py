from uuid import uuid4

from injector import inject

from src.app.commands.insert_account import InsertAccount
from src.app.ports.output.repositories.account_repository import (
    AccountRepository,
)
from src.domain.error import Error
from src.domain.model.account import Account, AccountId
from src.domain.model.contact_information import ContactInformation
from src.domain.services.validation_service import ValidationService


class InsertAccountService:
    __account_repository: AccountRepository
    __validation_service: ValidationService
    __EMAIL_DOMAIN: str

    @inject
    def __init__(
        self,
        account_repository: AccountRepository,
        validation_service: ValidationService,
    ) -> None:
        self.__account_repository = account_repository
        self.__validation_service = validation_service
        self.__EMAIL_DOMAIN = "email.com"

    def insert(self, insert_account: InsertAccount) -> Account | Error:
        account = Account(
            AccountId(uuid4()),
            ContactInformation(insert_account.email, insert_account.cellphones),
        )

        is_valid = self.__validation_service.is_valid(account, self.__EMAIL_DOMAIN)

        if is_valid:
            return self.__account_repository.insert(account)
        else:
            return Error("Account is not valid")
