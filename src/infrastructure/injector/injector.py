from injector import Injector

from src.infrastructure.injector.database_module import DatabaseModule
from src.infrastructure.injector.repositories_module import (
    RepositoriesModule,
)


def create_injector() -> Injector:
    return Injector([RepositoriesModule, DatabaseModule])
