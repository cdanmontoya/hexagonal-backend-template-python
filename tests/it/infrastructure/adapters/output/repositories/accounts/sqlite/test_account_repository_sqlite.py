import uuid

import pytest

from src.app.ports.output.repositories.account_repository import AccountRepository
from src.domain.model.account import AccountId
from src.infrastructure.adapters.output.repositories.accounts.sqlite.account_repository_sqlite import (
    AccountRepositorySQLite,
)
from src.infrastructure.injector.database_module import DatabaseModule
from tests.resources.factories.domain.model.account_factory import AccountFactory
from tests.resources.factories.domain.model.contact_information_factory import (
    ContactInformationFactory,
)


@pytest.fixture
def repository() -> AccountRepository:
    engine = DatabaseModule().sqlite_database()
    return AccountRepositorySQLite(engine)


@pytest.mark.usefixtures("clear_db_fixture")
def test_given_an_user_should_insert_correctly(repository: AccountRepository):
    account = AccountFactory.create()

    repository.insert(account)
    inserted_account = repository.get(account.id)

    assert inserted_account is not None
    assert account.id.id == inserted_account.id.id


@pytest.mark.usefixtures("clear_db_fixture")
def test_given_an_user_should_delete_correctly(repository: AccountRepository):
    account = AccountFactory.create()

    repository.insert(account)
    repository.delete(account.id)

    deleted_account = repository.get(account.id)

    assert deleted_account is None


@pytest.mark.usefixtures("clear_db_fixture")
def test_given_an_user_should_update_email_correctly(repository: AccountRepository):
    account_id = AccountId(uuid.uuid4())
    old_contact = ContactInformationFactory(email="old@email.com")
    new_contact = ContactInformationFactory(email="new@email.com")

    old_account = AccountFactory.create(id=account_id, contact_information=old_contact)
    repository.insert(old_account)

    new_account = AccountFactory.create(id=account_id, contact_information=new_contact)
    repository.update(account_id, new_account)

    updated_account = repository.get(account_id)

    assert updated_account is not None
    assert updated_account.contact_information.email == new_contact.email
