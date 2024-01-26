from uuid import UUID, uuid4

from pos.core.errors import AlreadyExistsError, DoesNotExistError
from pos.core.model.unit import Unit
from pos.core.repository.unit_repository.unit_repository import UnitRepository


class UnitService:
    def __init__(self, repository: UnitRepository) -> None:
        self.repository = repository

    def create_unit(self, name: str) -> Unit:
        if self.repository.contains_name(name):
            raise AlreadyExistsError

        unit_uuid = uuid4()

        self.repository.create_unit(Unit(unit_uuid, name))

        return self.repository.read_unit(unit_uuid)

    def read_unit(self, unit_uuid: UUID) -> Unit:
        if not self.repository.contains_uuid(unit_uuid):
            raise DoesNotExistError

        return self.repository.read_unit(unit_uuid)

    def read_units(self) -> list[Unit]:
        return self.repository.read_units()
