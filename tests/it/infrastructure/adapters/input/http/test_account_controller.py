from starlette.testclient import TestClient

from tests.resources.fixtures.application_fixture import application


def test_given_no_accounts_when_listing_all_should_return_empty_list(application: TestClient):
    response = application.get("/accounts")
    assert response.status_code == 200
    assert response.json() == []
