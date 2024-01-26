import json
import sqlite3
from sqlite3 import Connection, Cursor
from typing import Tuple

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


def test_read_sales(client: TestClient, controller: Tuple[Connection, Cursor]) -> None:
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
        "INSERT INTO receipts VALUES (?, ?, ?, ?)",
        (
            "3fa85f64-5717-4562-b3fc-2c963f66afa7",
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

    products_json_1 = []
    products_json_2 = []

    receipt_product_json_1 = {
        "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
        "quantity": 10,
        "price": 100.0,
        "total": 1000.0,
    }

    receipt_product_json_2 = {
        "id": "3fa85f64-5717-4562-b3fc-2c963f66afa7",
        "quantity": 10,
        "price": 100.0,
        "total": 1000.0,
    }

    products_json_1.append(receipt_product_json_1)
    products_json_2.append(receipt_product_json_2)

    receipt_products_str_1 = json.dumps(products_json_1)
    receipt_products_str_2 = json.dumps(products_json_2)

    controller[1].execute(
        "UPDATE receipts SET products = ? WHERE uuid = ?",
        (receipt_products_str_1, "3fa85f64-5717-4562-b3fc-2c963f66afa6"),
    )

    controller[1].execute(
        "UPDATE receipts SET products = ? WHERE uuid = ?",
        (receipt_products_str_2, "3fa85f64-5717-4562-b3fc-2c963f66afa7"),
    )

    controller[1].execute(
        "UPDATE receipts SET total = ? WHERE uuid = ?",
        (1000.0, "3fa85f64-5717-4562-b3fc-2c963f66afa6"),
    )

    controller[1].execute(
        "UPDATE receipts SET total = ? WHERE uuid = ?",
        (1000.0, "3fa85f64-5717-4562-b3fc-2c963f66afa7"),
    )

    controller[0].commit()

    response = client.get("/sales")

    assert response.status_code == 200
    assert response.json() == {
        "sales": {
            "n_receipts": 2,
            "revenue": 2000.0,
        }
    }
