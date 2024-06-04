from injector import Injector

from src.infrastructure.injector.application_services_module import (
    ApplicationServicesModule,
)
from src.infrastructure.injector.repositories_module import (
    RepositoriesModule,
)


def create_injector() -> Injector:
    return Injector([RepositoriesModule, ApplicationServicesModule])
