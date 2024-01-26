import sqlite3
from uuid import UUID

from pos.core.model.unit import Unit


class SQLiteUnitRepository:
    def __init__(self, database_name: str) -> None:
        self.connection = sqlite3.connect(database_name, check_same_thread=False)
        self.cursor = self.connection.cursor()

    def setup(self) -> None:
        self.cursor.execute("DROP TABLE IF EXISTS units")
        self.cursor.execute("CREATE TABLE units(uuid str UNIQUE, name str UNIQUE)")

        self.connection.commit()

    def create_unit(self, unit: Unit) -> None:
        self.cursor.execute(
            "INSERT INTO units VALUES (?, ?)", (str(unit.get_uuid()), unit.get_name())
        )

        self.connection.commit()

    def read_unit(self, uuid: UUID) -> Unit:
        self.cursor.execute("SELECT name FROM units WHERE uuid = ?", (str(uuid),))

        return Unit(uuid, self.cursor.fetchone()[0])

    def read_units(self) -> list[Unit]:
        self.cursor.row_factory = lambda cursor, row: Unit(*row)

        units: list[Unit] = self.cursor.execute("SELECT * FROM units").fetchall()

        self.cursor.row_factory = None

        return units

    def contains_name(self, name: str) -> bool:
        self.cursor.execute("SELECT * FROM units WHERE name = ?", (name,))

        return self.cursor.fetchone() is not None

    def contains_uuid(self, uuid: UUID) -> bool:
        self.cursor.execute("SELECT * FROM units WHERE uuid = ?", (str(uuid),))

        return self.cursor.fetchone() is not None
