from uuid import UUID

from pos.core.model.receipt_product import ReceiptProduct


class Receipt:
    def __init__(
        self, uuid: UUID, status: str, products: list[ReceiptProduct], total: float
    ) -> None:
        self.uuid = uuid
        self.status = status
        self.products = products
        self.total = total

    def get_uuid(self) -> UUID:
        return self.uuid

    def get_status(self) -> str:
        return self.status

    def get_products(self) -> list[ReceiptProduct]:
        return self.products

    def get_total(self) -> float:
        return self.total
