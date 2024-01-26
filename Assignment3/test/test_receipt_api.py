import json
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


def test_create_receipt(client: TestClient) -> None:
    response = client.post("/receipts")

    assert response.status_code == 201
    assert response.json() == {
        "receipt": {
            "id": ANY,
            "status": "open",
            "products": [],
            "total": 0,
        }
    }


def test_add_product(client: TestClient, controller: Tuple[Connection, Cursor]) -> None:
    controller[1].execute(
        "INSERT INTO receipts VALUES (?, ?, ?, ?)",
        (
            "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            "open",
            json.dumps([]),
            0,
        ),
    )

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

    response = client.post(
        "/receipts/3fa85f64-5717-4562-b3fc-2c963f66afa6/products",
        json={"id": "3fa85f64-5717-4562-b3fc-2c963f66afa6", "quantity": 10},
    )

    assert response.status_code == 201
    assert response.json() == {
        "receipt": {
            "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            "status": "open",
            "products": [
                {
                    "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                    "quantity": 10,
                    "price": 100.0,
                    "total": 1000.0,
                }
            ],
            "total": 1000.0,
        }
    }


def test_add_product_to_closed_receipt(
    client: TestClient, controller: Tuple[Connection, Cursor]
) -> None:
    controller[1].execute(
        "INSERT INTO receipts VALUES (?, ?, ?, ?)",
        (
            "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            "closed",
            json.dumps([]),
            0,
        ),
    )

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

    response = client.post(
        "/receipts/3fa85f64-5717-4562-b3fc-2c963f66afa6/products",
        json={"id": "3fa85f64-5717-4562-b3fc-2c963f66afa6", "quantity": 10},
    )

    message = "Receipt with id <3fa85f64-5717-4562-b3fc-2c963f66afa6> is closed"

    assert response.status_code == 403
    assert response.json() == {"error": {"message": message}}


def test_read_receipt(
    client: TestClient, controller: Tuple[Connection, Cursor]
) -> None:
    controller[1].execute(
        "INSERT INTO receipts VALUES (?, ?, ?, ?)",
        (
            "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            "open",
            json.dumps([]),
            0,
        ),
    )

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

    products_json = []

    receipt_product_json = {
        "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "quantity": 10,
        "price": 100.0,
        "total": 1000.0,
    }

    products_json.append(receipt_product_json)

    receipt_products_str = json.dumps(products_json)

    controller[1].execute(
        "UPDATE receipts SET products = ? WHERE uuid = ?",
        (receipt_products_str, "3fa85f64-5717-4562-b3fc-2c963f66afa6"),
    )

    controller[1].execute(
        "UPDATE receipts SET total = ? WHERE uuid = ?",
        (1000.0, "3fa85f64-5717-4562-b3fc-2c963f66afa6"),
    )

    controller[0].commit()

    response = client.get(
        "/receipts/3fa85f64-5717-4562-b3fc-2c963f66afa6",
    )

    assert response.status_code == 200
    assert response.json() == {
        "receipt": {
            "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            "status": "open",
            "products": [
                {
                    "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                    "quantity": 10,
                    "price": 100.0,
                    "total": 1000.0,
                }
            ],
            "total": 1000.0,
        }
    }


def test_close_receipt(
    client: TestClient, controller: Tuple[Connection, Cursor]
) -> None:
    controller[1].execute(
        "INSERT INTO receipts VALUES (?, ?, ?, ?)",
        (
            "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            "open",
            json.dumps([]),
            0,
        ),
    )

    controller[0].commit()

    response = client.patch(
        "/receipts/3fa85f64-5717-4562-b3fc-2c963f66afa6?status=closed"
    )

    assert response.status_code == 200


def test_close_nonexistent_receipt(client: TestClient) -> None:
    response = client.patch(
        "/receipts/3fa85f64-5717-4562-b3fc-2c963f66afa6?status=closed"
    )

    message = "Receipt with id <3fa85f64-5717-4562-b3fc-2c963f66afa6> does not exist"

    assert response.status_code == 404
    assert response.json() == {"error": {"message": message}}


def test_delete_receipt(
    client: TestClient, controller: Tuple[Connection, Cursor]
) -> None:
    controller[1].execute(
        "INSERT INTO receipts VALUES (?, ?, ?, ?)",
        (
            "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            "open",
            json.dumps([]),
            0,
        ),
    )

    controller[0].commit()

    response = client.delete("/receipts/3fa85f64-5717-4562-b3fc-2c963f66afa6")

    assert response.status_code == 200


def test_delete_closed_receipt(
    client: TestClient, controller: Tuple[Connection, Cursor]
) -> None:
    controller[1].execute(
        "INSERT INTO receipts VALUES (?, ?, ?, ?)",
        (
            "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            "closed",
            json.dumps([]),
            0,
        ),
    )

    controller[0].commit()

    response = client.delete("/receipts/3fa85f64-5717-4562-b3fc-2c963f66afa6")

    message = "Receipt with id <3fa85f64-5717-4562-b3fc-2c963f66afa6> is closed"

    assert response.status_code == 403
    assert response.json() == {"error": {"message": message}}


def test_delete_nonexistent_receipt(client: TestClient) -> None:
    response = client.delete("/receipts/3fa85f64-5717-4562-b3fc-2c963f66afa6")

    message = "Receipt with id <3fa85f64-5717-4562-b3fc-2c963f66afa6> does not exist"

    assert response.status_code == 404
    assert response.json() == {"error": {"message": message}}
