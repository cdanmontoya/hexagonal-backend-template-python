from python_template.domain.model.account import AccountId
from python_template.app.commands.update_account import UpdateAccount
from python_template.infrastructure.acl.dto.update_account_request_dto import (
    UpdateAccountRequestDto,
)


class UpdateAccountRequestDtoTranslator:

    @staticmethod
    def of(request_dto: UpdateAccountRequestDto):
        return UpdateAccount(
            AccountId(request_dto.id), request_dto.email, request_dto.cellphones
        )
