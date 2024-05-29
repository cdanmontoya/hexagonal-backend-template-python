from dataclasses import dataclass

from python_template.domain.model.account import AccountId


@dataclass(frozen=True)
class DeleteAccount:
    id: AccountId
