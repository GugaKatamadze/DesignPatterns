import json
import sqlite3
from uuid import UUID

from pos.core.model.receipt import Receipt
from pos.core.model.receipt_product import ReceiptProduct


class SQLiteReceiptRepository:
    def __init__(self, database_name: str) -> None:
        self.connection = sqlite3.connect(database_name, check_same_thread=False)
        self.cursor = self.connection.cursor()

    def setup(self) -> None:
        self.cursor.execute("DROP TABLE IF EXISTS receipts")
        self.cursor.execute(
            "CREATE TABLE receipts("
            "   uuid str UNIQUE,"
            "   status str,"
            "   products str,"
            "   total float"
            ")"
        )

        self.connection.commit()

    def create_receipt(self, receipt: Receipt) -> None:
        self.cursor.execute(
            "INSERT INTO receipts VALUES (?, ?, ?, ?)",
            (
                str(receipt.get_uuid()),
                str(receipt.get_status()),
                json.dumps([]),
                0,
            ),
        )

        self.connection.commit()

    def add_product(self, receipt_uuid: UUID, product: ReceiptProduct) -> None:
        products = self.read_receipt(receipt_uuid).get_products()

        products.append(product)

        products_json = []

        grand_total: float = 0

        for receipt_product in products:
            receipt_product_json = {
                "id": str(receipt_product.get_uuid()),
                "quantity": receipt_product.get_quantity(),
                "price": receipt_product.get_price(),
                "total": receipt_product.get_total(),
            }

            grand_total += receipt_product.get_total()

            products_json.append(receipt_product_json)

        receipt_products_str = json.dumps(products_json)

        self.cursor.execute(
            "UPDATE receipts SET products = ? WHERE uuid = ?",
            (receipt_products_str, str(receipt_uuid)),
        )
        self.cursor.execute(
            "UPDATE receipts SET total = ? WHERE uuid = ?",
            (grand_total, str(receipt_uuid)),
        )

        self.connection.commit()

    def read_receipt(self, uuid: UUID) -> Receipt:
        self.cursor.execute(
            "SELECT status, products, total from receipts WHERE uuid = ?", (str(uuid),)
        )

        result = self.cursor.fetchone()

        receipt_products = []

        for receipt_product in json.loads(result[1]):
            uuid = receipt_product["id"]
            quantity = receipt_product["quantity"]
            price = receipt_product["price"]
            total = receipt_product["total"]

            receipt_products.append(ReceiptProduct(uuid, quantity, price, total))

        return Receipt(uuid, result[0], receipt_products, result[2])

    def contains_uuid(self, uuid: UUID) -> bool:
        self.cursor.execute("SELECT * FROM receipts WHERE uuid = ?", (str(uuid),))

        return self.cursor.fetchone() is not None

    def close_receipt(self, uuid: UUID, status: str) -> None:
        self.cursor.execute(
            "UPDATE receipts SET status = ? WHERE uuid = ?", (status, str(uuid))
        )

        self.connection.commit()

    def delete_receipt(self, uuid: UUID) -> None:
        self.cursor.execute("DELETE FROM receipts WHERE uuid = ?", (str(uuid),))

        self.connection.commit()

    def is_closed(self, uuid: UUID) -> bool:
        self.cursor.execute("SELECT status FROM receipts WHERE uuid = ?", (str(uuid),))

        result: str = self.cursor.fetchone()[0]

        return result == "closed"
