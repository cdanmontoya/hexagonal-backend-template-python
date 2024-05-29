from injector import Injector

from infrastructure.injector.application_services_module import (
    ApplicationServicesModule,
)
from infrastructure.injector.repositories_module import (
    RepositoriesModule,
)

injector = Injector([RepositoriesModule, ApplicationServicesModule])
