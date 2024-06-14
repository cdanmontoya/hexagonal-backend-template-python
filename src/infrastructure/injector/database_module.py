from injector import Module, provider, singleton
from sqlalchemy import Engine, create_engine


class DatabaseModule(Module):
    @singleton
    @provider
    def sqlite_database(self) -> Engine:
        return create_engine("sqlite:///template.db", echo=True)
