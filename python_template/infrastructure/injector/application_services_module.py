from injector import Module, Binder

from python_template.app.services.delete_account_service import DeleteAccountService
from python_template.app.services.get_accounts_service import GetAccountsService
from python_template.app.services.insert_account_service import InsertAccountService
from python_template.app.services.update_account_service import UpdateAccountService


class ApplicationServicesModule(Module):
    def configure(self, binder: Binder) -> None:
        binder.bind(DeleteAccountService)
        binder.bind(GetAccountsService)
        binder.bind(InsertAccountService)
        binder.bind(UpdateAccountService)
