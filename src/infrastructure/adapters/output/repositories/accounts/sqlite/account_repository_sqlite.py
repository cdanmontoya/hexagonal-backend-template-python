from typing import override

from injector import singleton, inject
from sqlalchemy import Engine, select
from sqlalchemy.orm import Session

from src.app.ports.output.repositories.account_repository import (
    AccountRepository,
)
from src.domain.model.account import Account, AccountId
from src.infrastructure.adapters.output.repositories.accounts.sqlite.account_mapper import (
    AccountMapper,
)
from src.infrastructure.adapters.output.repositories.accounts.sqlite.account_model import (
    Base,
    AccountDao,
)


@singleton
class AccountRepositorySQLite(AccountRepository):
    __engine: Engine

    @inject
    def __init__(self, engine: Engine) -> None:
        self.__engine = engine
        Base.metadata.create_all(engine)

    @override
    def get(self, key: AccountId) -> Account | None:
        session = Session(self.__engine)
        statement = select(AccountDao).where(AccountDao.id.__eq__(str(key.id)))
        account_dao = session.scalar(statement)

        return AccountMapper.from_account_dao(account_dao) if account_dao else None

    @override
    def get_all(self) -> list[Account]:
        session = Session(self.__engine)
        statement = select(AccountDao)

        return [
            AccountMapper.from_account_dao(account_dao)
            for account_dao in session.scalars(statement)
        ]

    @override
    def insert(self, account: Account) -> Account:
        with Session(self.__engine) as session:
            account_dao = AccountMapper.from_account(account)
            session.add(account_dao)
            session.commit()

        return account

    @override
    def update(self, key: AccountId, account: Account) -> Account: ...

    @override
    def delete(self, key: AccountId) -> Account:
        session = Session(self.__engine)
        account_dao = session.get(AccountDao, str(key.id))

        if account_dao:
            account = AccountMapper.from_account_dao(account_dao)
            session.delete(account_dao)
            session.commit()
        else:
            account = None

        return account
