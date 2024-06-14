from injector import Injector

from src.infrastructure.injector.repositories_module import (
    RepositoriesModule,
)


def create_injector() -> Injector:
    return Injector([RepositoriesModule])
