from uuid import UUID

from app.queries.get_account_by_id import GetAccountById
from domain.model.account import AccountId


class GetAccountByIdRequestDtoTranslator:

    @staticmethod
    def of(request_dto: UUID) -> GetAccountById:
        return GetAccountById(AccountId(request_dto))
