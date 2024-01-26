from typing import Protocol
from uuid import UUID

from pos.core.model.unit import Unit


class UnitRepository(Protocol):
    def setup(self) -> None:
        pass

    def create_unit(self, unit: Unit) -> None:
        pass

    def read_unit(self, uuid: UUID) -> Unit:
        pass

    def read_units(self) -> list[Unit]:
        pass

    def contains_name(self, name: str) -> bool:
        pass

    def contains_uuid(self, uuid: UUID) -> bool:
        pass
