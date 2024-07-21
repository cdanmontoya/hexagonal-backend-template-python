from injector import Module, provider, singleton
from sqlalchemy import Engine, create_engine


class DatabaseModule(Module):
    path = "sqlite:///template.db"

    @singleton
    @provider
    def sqlite_database(self) -> Engine:
        return create_engine(self.path, echo=True)
