from injector import Injector

from src.infrastructure.config.injector.database_module import DatabaseModule
from src.infrastructure.config.injector.publishers_module import PublishersModule
from src.infrastructure.config.injector.repositories_module import RepositoriesModule


def create_injector() -> Injector:
    return Injector([RepositoriesModule, DatabaseModule, PublishersModule])
