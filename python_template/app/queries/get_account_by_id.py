from dataclasses import dataclass

from python_template.domain.model.account import AccountId


@dataclass(frozen=True)
class GetAccountById:
    account_id: AccountId
