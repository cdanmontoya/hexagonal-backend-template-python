import os

from pytest import fixture
from sqlalchemy import create_engine, Engine
from starlette.testclient import TestClient
from testcontainers.core.waiting_utils import wait_for_logs
from testcontainers.postgres import PostgresContainer

from src.infrastructure.adapters.input.http.application import Application
from src.infrastructure.config.injector.injector import create_injector


@fixture(scope="function")
def postgres_container() -> PostgresContainer:
    postgres = PostgresContainer(
        image=os.getenv("DB_IMAGE", "postgres"),
        username=os.getenv("DB_USER", "dbuser"),
        password=os.getenv("DB_PASS", "dbpassword"),
        dbname=os.getenv("DB_DATABASE"),
    )
    with postgres:
        wait_for_logs(
            postgres,
            r"UTC \[1\] LOG:  database system is ready to accept connections",
            10,
        )
        yield postgres


@fixture(scope="function")
def db(postgres_container: PostgresContainer) -> Engine:
    url = postgres_container.get_connection_url()
    engine = create_engine(url, echo=False, future=True)
    yield engine


@fixture(scope="function")
def test_client(db: Engine) -> TestClient:
    inject = create_injector()
    inject.binder.bind(Engine, db)
    return TestClient(Application(inject).create_app())
