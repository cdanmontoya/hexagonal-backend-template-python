from app.commands.update_account import UpdateAccount
from domain.model.account import AccountId
from infrastructure.acl.dto.update_account_request_dto import (
    UpdateAccountRequestDto,
)


class UpdateAccountRequestDtoTranslator:

    @staticmethod
    def of(request_dto: UpdateAccountRequestDto) -> UpdateAccount:
        return UpdateAccount(
            AccountId(request_dto.id), request_dto.email, request_dto.cellphones
        )
