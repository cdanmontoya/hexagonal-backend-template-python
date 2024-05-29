from dataclasses import dataclass

from python_template.domain.model.account import AccountId


@dataclass(frozen=True)
class UpdateAccount:
    id: AccountId
    email: str
    cellphones: list[str]
