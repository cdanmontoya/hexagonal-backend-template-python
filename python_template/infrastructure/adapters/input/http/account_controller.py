from uuid import UUID

from fastapi import APIRouter
from injector import inject

from python_template.app.services.delete_account_service import DeleteAccountService
from python_template.app.services.get_accounts_service import GetAccountsService
from python_template.app.services.insert_account_service import InsertAccountService
from python_template.app.services.update_account_service import UpdateAccountService
from python_template.domain.model.account import Account, AccountId
from python_template.infrastructure.acl.dto.insert_account_request_dto import (
    InsertAccountRequestDto,
)
from python_template.infrastructure.acl.dto.update_account_request_dto import (
    UpdateAccountRequestDto,
)
from python_template.infrastructure.acl.translators.insert_account_request_dto_translator import (
    InsertAccountRequestDtoTranslator,
)
from python_template.infrastructure.acl.translators.update_account_request_dto_translator import (
    UpdateAccountRequestDtoTranslator,
)


class AccountController:
    router: APIRouter
    __insert_account_service: InsertAccountService
    __get_accounts_service: GetAccountsService
    __delete_account_service: DeleteAccountService
    __update_account_service: UpdateAccountService

    @inject
    def __init__(
        self,
        insert_account_service: InsertAccountService,
        get_accounts_service: GetAccountsService,
        delete_account_service: DeleteAccountService,
        update_account_service: UpdateAccountService,
    ) -> None:
        self.router = APIRouter(
            prefix="/accounts",
            tags=["accounts"],
        )
        self.__insert_account_service = insert_account_service
        self.__get_accounts_service = get_accounts_service
        self.__delete_account_service = delete_account_service
        self.__update_account_service = update_account_service

        self.router.add_api_route("/", self.insert, methods=["POST"])
        self.router.add_api_route("/", self.get_all, methods=["GET"])
        self.router.add_api_route("/{account_id}", self.get, methods=["GET"])
        self.router.add_api_route("/{account_id}", self.delete, methods=["DELETE"])
        self.router.add_api_route("/{account_id}", self.update, methods=["PUT"])

    async def insert(self, request: InsertAccountRequestDto) -> Account:
        insert_account = InsertAccountRequestDtoTranslator.of(request)
        return self.__insert_account_service.insert(insert_account)

    async def get_all(self) -> list[Account]:
        return self.__get_accounts_service.get_all()

    async def get(self, account_id: UUID) -> Account | None:
        return self.__get_accounts_service.get(AccountId(account_id))

    async def delete(self, account_id: UUID) -> Account:
        return self.__delete_account_service.delete(AccountId(account_id))

    async def update(self, request: UpdateAccountRequestDto) -> Account:
        update_account = UpdateAccountRequestDtoTranslator.of(request)
        return self.__update_account_service.update(update_account)
