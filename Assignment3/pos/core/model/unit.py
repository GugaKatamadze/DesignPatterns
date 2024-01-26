from uuid import UUID


class Unit:
    def __init__(self, uuid: UUID, name: str) -> None:
        self.uuid = uuid
        self.name = name

    def get_uuid(self) -> UUID:
        return self.uuid

    def get_name(self) -> str:
        return self.name
