from python_template.app.commands.insert_account import InsertAccount
from python_template.infrastructure.acl.dto.insert_account_request_dto import (
    InsertAccountRequestDto,
)


class InsertAccountRequestDtoTranslator:

    @staticmethod
    def of(request_dto: InsertAccountRequestDto):
        return InsertAccount(request_dto.email, request_dto.cellphones)
