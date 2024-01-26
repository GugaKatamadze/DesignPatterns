import sqlite3
from sqlite3 import Connection, Cursor
from typing import Tuple
from unittest.mock import ANY

import pytest
from starlette.testclient import TestClient

from pos.runner.setup import setup_for_testing


@pytest.fixture
def client() -> TestClient:
    return TestClient(setup_for_testing())


@pytest.fixture
def controller() -> Tuple[Connection, Cursor]:
    connection = sqlite3.connect("test.db", check_same_thread=False)
    cursor = connection.cursor()

    return connection, cursor


def test_create_product(client: TestClient) -> None:
    response = client.post(
        "/products",
        json={
            "unit_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            "name": "lobio",
            "barcode": "1234567890",
            "price": 100.0,
        },
    )

    assert response.status_code == 201
    assert response.json() == {
        "product": {
            "id": ANY,
            "unit_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            "name": "lobio",
            "barcode": "1234567890",
            "price": 100.0,
        }
    }


def test_create_existing_product(client: TestClient) -> None:
    response = client.post(
        "/products",
        json={
            "unit_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            "name": "lobio",
            "barcode": "1234567890",
            "price": 100.0,
        },
    )

    response = client.post(
        "/products",
        json={
            "unit_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            "name": "lobio",
            "barcode": "1234567890",
            "price": 100.0,
        },
    )

    assert response.status_code == 409
    assert response.json() == {
        "error": {"message": "Product with barcode <1234567890> already exists"}
    }


def test_read_product(
    client: TestClient, controller: Tuple[Connection, Cursor]
) -> None:
    controller[1].execute(
        "INSERT INTO products VALUES (?, ?, ?, ?, ?)",
        (
            "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            "lobio",
            "1234567890",
            "100.0",
        ),
    )

    controller[0].commit()

    response = client.get("/products/3fa85f64-5717-4562-b3fc-2c963f66afa6")

    assert response.status_code == 200
    assert response.json() == {
        "product": {
            "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            "unit_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            "name": "lobio",
            "barcode": "1234567890",
            "price": 100.0,
        }
    }


def test_read_nonexistent_product(client: TestClient) -> None:
    response = client.get("/products/3fa85f64-5717-4562-b3fc-2c963f66afa6")

    message = "Product with id <3fa85f64-5717-4562-b3fc-2c963f66afa6> does not exist"

    assert response.status_code == 404
    assert response.json() == {"error": {"message": message}}


def test_read_products(
    client: TestClient, controller: Tuple[Connection, Cursor]
) -> None:
    controller[1].execute(
        "INSERT INTO products VALUES (?, ?, ?, ?, ?)",
        (
            "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            "lobio",
            "1234567890",
            "100.0",
        ),
    )
    controller[1].execute(
        "INSERT INTO products VALUES (?, ?, ?, ?, ?)",
        (
            "3fa85f64-5717-4562-b3fc-2c963f66afa7",
            "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            "lobio",
            "1234567891",
            "100.0",
        ),
    )

    controller[0].commit()

    response = client.get("/products")

    assert response.status_code == 200
    assert response.json() == {
        "products": [
            {
                "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                "unit_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                "name": "lobio",
                "barcode": "1234567890",
                "price": 100.0,
            },
            {
                "id": "3fa85f64-5717-4562-b3fc-2c963f66afa7",
                "unit_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                "name": "lobio",
                "barcode": "1234567891",
                "price": 100.0,
            },
        ]
    }


def test_update_product(
    client: TestClient, controller: Tuple[Connection, Cursor]
) -> None:
    controller[1].execute(
        "INSERT INTO products VALUES (?, ?, ?, ?, ?)",
        (
            "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            "lobio",
            "1234567890",
            "100.0",
        ),
    )

    controller[0].commit()

    response = client.patch(
        "/products/3fa85f64-5717-4562-b3fc-2c963f66afa6/?price=200.0"
    )

    assert response.status_code == 200


def test_update_nonexistent_product(client: TestClient) -> None:
    response = client.patch(
        "/products/3fa85f64-5717-4562-b3fc-2c963f66afa6/?price=200.0"
    )

    message = "Product with id <3fa85f64-5717-4562-b3fc-2c963f66afa6> does not exist"

    assert response.status_code == 404
    assert response.json() == {"error": {"message": message}}
