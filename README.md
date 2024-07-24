# Python Template

![](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![](https://img.shields.io/badge/fastapi-109989?style=for-the-badge&logo=FASTAPI&logoColor=white)
![](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg?style=for-the-badge)](https://github.com/psf/black)

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=cdanmontoya_python-template&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=cdanmontoya_python-template)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=cdanmontoya_python-template&metric=bugs)](https://sonarcloud.io/summary/new_code?id=cdanmontoya_python-template)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=cdanmontoya_python-template&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=cdanmontoya_python-template)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=cdanmontoya_python-template&metric=coverage)](https://sonarcloud.io/summary/new_code?id=cdanmontoya_python-template)
[![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=cdanmontoya_python-template&metric=duplicated_lines_density)](https://sonarcloud.io/summary/new_code?id=cdanmontoya_python-template)
[![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=cdanmontoya_python-template&metric=ncloc)](https://sonarcloud.io/summary/new_code?id=cdanmontoya_python-template)
[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=cdanmontoya_python-template&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=cdanmontoya_python-template)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=cdanmontoya_python-template&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=cdanmontoya_python-template)
[![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=cdanmontoya_python-template&metric=sqale_index)](https://sonarcloud.io/summary/new_code?id=cdanmontoya_python-template)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=cdanmontoya_python-template&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=cdanmontoya_python-template)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=cdanmontoya_python-template&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=cdanmontoya_python-template)


# Folder structure
The folder structure is inspired in a Hexagonal Architecture and borrows concepts from Domain Driven Design. The main 
goal is to achieve a decoupled implementation that keeps the business knowledge and processes defined in entities,
abstractions and services in the `domain` and `app` packages, and the concrete implementations and details that depend on external systems or third-party 
software in the `infrastructure` package.


```text
.
├── src/
│   ├── app/                        # Defines the application behavior
│   │   ├── commands/                   # Holds the data required to execute operations that write into the system
│   │   ├── queries/                    # Holds the data required to execute operations that read data from the system
│   │   ├── use_cases/                  # Implements the bussiness logic
│   │   └── ports/                      # Defines abstractions to interact with external systems
│   │       └── output/                  
│   ├── domain/                     # Represents the bussiness knowledge and understanding
│   │   ├── model/                      # Defines relevant bussiness entities and their operations
│   │   ├── services/                   # Implements logic that involves several entities
│   │   └── events/                     # Holds information about the facts that happened on the system
│   └── infrastructure/
│       ├── acl/                    # Anticorruption layer that aims to keep the domain isolated from external systems
│       │   ├── dto/                    # Data transfer objects for both input and outupt
│       │   └── translators/            # Translates DTOs into commands, queries and domain entities, and vice-versa
│       ├── adapters/               # Concrete implementations depending on frameworks and particular technologies
│       │   ├── input/                  # Input adapters that recieve interactions from external systems using different protocols
│       │   │   ├── events/
│       │   │   └── http/
│       │   └── output/                 # Output adapters that call external systems
│       ├── injector/               # Dependency injection configuration
│       └── migrations/             # Database schema evolutions configuration
└── test/
    ├── unit/
    │   └── ...          # Both unit and integration tests mimic the same folder structure as the src/ folder, but only for the required files
    ├── it/
    │   └── ...
    └── resources/
        ├── factories/
        └── fixtures/
```


# Running the project

## Dependency management
The project suggests to use [Poetry](https://python-poetry.org) as the dependency management tool. Once installed, you can 
create a virtual environment for this project running the following commands.

```bash
poetry shell
poetry install
```

Further dependencies can be added running 

```bash
poetry add <dependency>
poetry add --group dev <dependency> # for development-only dependencies
```

## Database management
### Local instance

### Evolving the schema

## Run locally
```bash
uvicorn src.infrastructure.adapters.input.http.application:app --host 0.0.0.0 --port 15000 --reload
```

## Tests

### Run all in a single command
```bash
coverage run --source=src -m pytest tests
coverage report
coverage html
```

### Run by type
```bash
coverage run --source=src -m pytest tests/unit
coverage xml -i

coverage run --source=src -m pytest tests/it
coverage xml -i

coverge combine # To merge both coverage reports
```



# References and further readings

* [**Evolutionary Database Design:**](https://martinfowler.com/articles/evodb.html) is a technique that allows to continuously 
evolve database schemas, matching with agile development environments. In this project is achieved using [Alembic](https://alembic.sqlalchemy.org/en/latest/).
* Hexagonal architecture: #TODO: define
* CQRS: #TODO: define
* Dependency injection
* 

