import pytest
from fastapi.testclient import TestClient

from src.infrastructure.adapters.input.http.application import Application
from src.infrastructure.injector.injector import create_injector


@pytest.fixture
def application() -> TestClient:
    return TestClient(Application(create_injector()).create_app())
