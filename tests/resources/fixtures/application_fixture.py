import pytest
from fastapi.testclient import TestClient

from infrastructure.adapters.input.http.application import Application
from infrastructure.injector.injector import create_injector


@pytest.fixture
def application() -> TestClient:
    return TestClient(Application(create_injector()).create_app())
