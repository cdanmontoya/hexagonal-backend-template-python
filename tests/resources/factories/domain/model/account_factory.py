import uuid

import factory

from domain.model.account import Account, AccountId
from resources.factories.domain.model.contact_information_factory import (
    ContactInformationFactory,
)


class AccountIdFactory(factory.Factory):
    class Meta:
        model = AccountId

    id = uuid.uuid4()


class AccountFactory(factory.Factory):
    class Meta:
        model = Account

    id = factory.SubFactory(AccountIdFactory)
    contact_information = factory.SubFactory(ContactInformationFactory)
