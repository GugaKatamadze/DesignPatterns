import sqlite3
from uuid import UUID

from pos.core.model.product import Product


class SQLiteProductRepository:
    def __init__(self, database_name: str) -> None:
        self.connection = sqlite3.connect(database_name, check_same_thread=False)
        self.cursor = self.connection.cursor()

    def setup(self) -> None:
        self.cursor.execute("DROP TABLE IF EXISTS products")
        self.cursor.execute(
            "CREATE TABLE products("
            "   uuid str UNIQUE,"
            "   unit_uuid str,"
            "   name str,"
            "   barcode str UNIQUE,"
            "   price float"
            ")"
        )

        self.connection.commit()

    def create_product(self, product: Product) -> None:
        self.cursor.execute(
            "INSERT INTO products VALUES (?, ?, ?, ?, ?)",
            (
                str(product.get_uuid()),
                str(product.get_unit_uuid()),
                product.get_name(),
                product.get_barcode(),
                product.get_price(),
            ),
        )

        self.connection.commit()

    def read_product(self, uuid: UUID) -> Product:
        self.cursor.execute(
            "SELECT unit_uuid, name, barcode, price FROM products WHERE uuid = ?",
            (str(uuid),),
        )

        result = self.cursor.fetchone()

        return Product(uuid, result[0], result[1], str(result[2]), result[3])

    def read_products(self) -> list[Product]:
        self.cursor.row_factory = lambda cursor, row: Product(*row)

        products: list[Product] = self.cursor.execute(
            "SELECT * FROM products"
        ).fetchall()

        self.cursor.row_factory = None

        for product in products:
            product.barcode = str(product.barcode)

        return products

    def contains_barcode(self, barcode: str) -> bool:
        self.cursor.execute("SELECT * FROM products WHERE barcode = ?", (barcode,))

        return self.cursor.fetchone() is not None

    def contains_uuid(self, uuid: UUID) -> bool:
        self.cursor.execute("SELECT * FROM products WHERE uuid = ?", (str(uuid),))

        return self.cursor.fetchone() is not None

    def update_product(self, uuid: UUID, price: float) -> None:
        self.cursor.execute(
            "UPDATE products SET price = ? WHERE uuid = ?",
            (
                price,
                str(uuid),
            ),
        )

        self.connection.commit()

    def get_price(self, uuid: UUID) -> float:
        self.cursor.execute("SELECT price from products WHERE uuid = ?", (str(uuid),))

        return float(self.cursor.fetchone()[0])
