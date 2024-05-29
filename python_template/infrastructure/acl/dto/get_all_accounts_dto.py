from pydantic import BaseModel

from infrastructure.acl.dto.account_dto import AccountDto


class GetAllAccountsResponseDto(BaseModel):
    accounts: list[AccountDto]
