from app.commands.insert_account import InsertAccount
from infrastructure.acl.dto.insert_account_request_dto import (
    InsertAccountRequestDto,
)


class InsertAccountRequestDtoTranslator:

    @staticmethod
    def of(request_dto: InsertAccountRequestDto) -> InsertAccount:
        return InsertAccount(request_dto.email, request_dto.cellphones)
