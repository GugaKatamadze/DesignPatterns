from uuid import UUID


class ReceiptProduct:
    def __init__(self, uuid: UUID, quantity: int, price: float, total: float) -> None:
        self.uuid = uuid
        self.quantity = quantity
        self.price = price
        self.total = total

    def get_uuid(self) -> UUID:
        return self.uuid

    def get_quantity(self) -> int:
        return self.quantity

    def get_price(self) -> float:
        return self.price

    def get_total(self) -> float:
        return self.total
