from uuid import UUID

from fastapi import APIRouter
from injector import inject

from app.services.delete_account_service import DeleteAccountService
from app.services.get_accounts_service import GetAccountsService
from app.services.insert_account_service import InsertAccountService
from app.services.update_account_service import UpdateAccountService
from domain.model.account import Account, AccountId
from infrastructure.acl.dto.account_dto import AccountDto
from infrastructure.acl.dto.get_all_accounts_dto import GetAllAccountsResponseDto
from infrastructure.acl.dto.insert_account_request_dto import (
    InsertAccountRequestDto,
)
from infrastructure.acl.dto.update_account_request_dto import (
    UpdateAccountRequestDto,
)
from infrastructure.acl.translators.account_dto_translator import AccountDtoTranslator
from infrastructure.acl.translators.get_all_accounts_response_dto_translator import GetAllAccountsDtoTranslator
from infrastructure.acl.translators.insert_account_request_dto_translator import (
    InsertAccountRequestDtoTranslator,
)
from infrastructure.acl.translators.update_account_request_dto_translator import (
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

    async def insert(self, request: InsertAccountRequestDto) -> AccountDto:
        insert_account = InsertAccountRequestDtoTranslator.of(request)
        account = self.__insert_account_service.insert(insert_account)
        return AccountDtoTranslator.of(account)

    async def get_all(self) -> GetAllAccountsResponseDto:
        accounts = self.__get_accounts_service.get_all()
        return GetAllAccountsDtoTranslator.of(accounts)

    async def get(self, account_id: UUID) -> AccountDto | None:
        account = self.__get_accounts_service.get(AccountId(account_id))
        return AccountDtoTranslator.of(account)

    async def delete(self, account_id: UUID) -> AccountDto:
        account = self.__delete_account_service.delete(AccountId(account_id))
        return AccountDtoTranslator.of(account)

    async def update(self, request: UpdateAccountRequestDto) -> AccountDto:
        update_account = UpdateAccountRequestDtoTranslator.of(request)
        account = self.__update_account_service.update(update_account)
        return AccountDtoTranslator.of(account)
