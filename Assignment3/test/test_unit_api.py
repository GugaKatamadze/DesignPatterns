import sqlite3
import uuid
from sqlite3 import Connection, Cursor
from typing import Tuple
from unittest.mock import ANY

import pytest
from fastapi.testclient import TestClient

from pos.runner.setup import setup_for_testing


@pytest.fixture
def client() -> TestClient:
    return TestClient(setup_for_testing())


@pytest.fixture
def controller() -> Tuple[Connection, Cursor]:
    connection = sqlite3.connect("test.db", check_same_thread=False)
    cursor = connection.cursor()

    return connection, cursor


def test_create_unit(client: TestClient) -> None:
    response = client.post("/units", json={"name": "kg"})

    assert response.status_code == 201
    assert response.json() == {"unit": {"id": ANY, "name": "kg"}}


def test_read_nonexistent_unit(client: TestClient) -> None:
    random_uuid = uuid.uuid4()

    response = client.get(f"/units/{random_uuid}")

    assert response.status_code == 404
    assert response.json() == {
        "error": {"message": f"Unit with id <{random_uuid}> does not exist"}
    }


def test_read_existing_unit(
    client: TestClient, controller: Tuple[Connection, Cursor]
) -> None:
    random_uuid = uuid.uuid4()

    controller[1].execute("INSERT INTO units VALUES (?, ?)", (str(random_uuid), "kg"))

    controller[0].commit()

    response = client.get(f"/units/{random_uuid}")

    assert response.status_code == 200
    assert response.json() == {"unit": {"id": str(random_uuid), "name": "kg"}}


def test_read_units_when_there_are_none(client: TestClient) -> None:
    response = client.get("/units")

    assert response.status_code == 200
    assert response.json() == {"units": []}


def test_read_units(client: TestClient, controller: Tuple[Connection, Cursor]) -> None:
    random_uuid_1 = uuid.uuid4()
    random_uuid_2 = uuid.uuid4()

    controller[1].execute("INSERT INTO units VALUES (?, ?)", (str(random_uuid_1), "kg"))
    controller[1].execute("INSERT INTO units VALUES (?, ?)", (str(random_uuid_2), "mg"))

    controller[0].commit()

    response = client.get("/units")

    assert response.status_code == 200
    assert response.json() == {
        "units": [
            {"id": str(random_uuid_1), "name": "kg"},
            {"id": str(random_uuid_2), "name": "mg"},
        ]
    }
