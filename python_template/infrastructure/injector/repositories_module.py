from injector import Module, Binder

from python_template.app.ports.output.repositories.account_repository import (
    AccountRepository,
)
from python_template.infrastructure.adapters.output.repositories.account_repository_dict import (
    AccountRepositoryDict,
)


class RepositoriesModule(Module):
    def configure(self, binder: Binder) -> None:
        binder.bind(AccountRepository, AccountRepositoryDict)
