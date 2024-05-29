from injector import Injector

from python_template.infrastructure.injector.application_services_module import (
    ApplicationServicesModule,
)
from python_template.infrastructure.injector.repositories_module import (
    RepositoriesModule,
)

injector = Injector([RepositoriesModule, ApplicationServicesModule])
