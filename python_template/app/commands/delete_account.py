from dataclasses import dataclass

from domain.model.account import AccountId


@dataclass(frozen=True)
class DeleteAccount:
    id: AccountId
