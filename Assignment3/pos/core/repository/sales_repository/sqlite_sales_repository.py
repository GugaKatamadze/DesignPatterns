import sqlite3

from pos.core.model.sales import Sales


class SQLiteSalesRepository:
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

    def read_sales(self) -> Sales:
        self.cursor.execute("SELECT COUNT(*) FROM receipts")

        n_receipts = self.cursor.fetchone()[0]

        self.cursor.execute("SELECT SUM(total) FROM receipts")

        result = self.cursor.fetchone()

        revenue = 0

        if result[0] is not None:
            revenue = result[0]

        return Sales(n_receipts, revenue)
