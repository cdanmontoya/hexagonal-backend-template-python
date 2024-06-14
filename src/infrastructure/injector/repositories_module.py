from injector import Module, Binder

from src.app.ports.output.repositories.account_repository import (
    AccountRepository,
)
from src.infrastructure.adapters.output.repositories.accounts.sqlite.account_repository_sqlite import (
    AccountRepositorySQLite,
)


class RepositoriesModule(Module):
    def configure(self, binder: Binder) -> None:
        binder.bind(interface=AccountRepository, to=AccountRepositorySQLite)  # type: ignore
