from uuid import UUID


class Product:
    def __init__(
        self, uuid: UUID, unit_uuid: UUID, name: str, barcode: str, price: float
    ) -> None:
        self.uuid = uuid
        self.unit_uuid = unit_uuid
        self.name = name
        self.barcode = barcode
        self.price = price

    def get_uuid(self) -> UUID:
        return self.uuid

    def get_unit_uuid(self) -> UUID:
        return self.unit_uuid

    def get_name(self) -> str:
        return self.name

    def get_barcode(self) -> str:
        return self.barcode

    def get_price(self) -> float:
        return self.price
