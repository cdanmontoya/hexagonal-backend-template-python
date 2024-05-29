import pytest
from fastapi.testclient import TestClient

from infrastructure.adapters.input.http.application import app


@pytest.fixture
def application() -> TestClient:
    return TestClient(app)
