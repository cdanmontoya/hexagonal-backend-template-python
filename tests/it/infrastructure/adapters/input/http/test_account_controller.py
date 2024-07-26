import uuid

from starlette.testclient import TestClient

from tests.resources.factories.infrastructure.acl.dto.insert_account_request_dto_factory import (
    InsertAccountRequestDtoFactory,
)
from tests.resources.fixtures.database_fixture import (
    test_client,
    db,
    postgres_container,
)


def test_given_no_accounts_when_listing_all_should_return_empty_list(
    test_client: TestClient,
):
    response = test_client.get("/accounts")
    assert response.status_code == 200
    assert response.json()["accounts"] == []


def test_given_no_accounts_when_finding_one_should_return_not_found(
    test_client: TestClient,
):
    response = test_client.get(f"/accounts/{uuid.uuid4()}")
    assert response.status_code == 200
    assert response.json()["message"] == "Account not found"


def test_given_an_inserted_account_when_listing_all_should_return_a_non_empty_list(
    test_client: TestClient,
):
    request = InsertAccountRequestDtoFactory.create()

    response = test_client.post("/accounts", json=request.model_dump())
    list_response = test_client.get("/accounts")

    assert response.status_code == 200
    assert response.json()["contact_information"]["email"] == request.email
    assert len(list_response.json()["accounts"]) == 1


def test_given_an_existing_account_when_deleting_should_return_ok(
    test_client: TestClient,
):
    insert_request = InsertAccountRequestDtoFactory.create()
    test_client.post("/accounts", json=insert_request.model_dump())

    list_response = test_client.get("/accounts")
    account_id = list_response.json()["accounts"][0]["id"]

    delete_response = test_client.delete(f"/accounts/{account_id}")
    response_list = test_client.get("/accounts")

    assert delete_response.status_code == 200
    assert len(response_list.json()["accounts"]) == 0
