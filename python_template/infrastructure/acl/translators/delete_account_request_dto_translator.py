from uuid import UUID

from app.commands.delete_account import DeleteAccount
from domain.model.account import AccountId


class DeleteAccountRequestDtoTranslator:

    @staticmethod
    def of(request_dto: UUID) -> DeleteAccount:
        return DeleteAccount(AccountId(request_dto))
