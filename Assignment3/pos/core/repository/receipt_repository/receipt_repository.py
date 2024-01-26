from typing import Protocol
from uuid import UUID

from pos.core.model.receipt import Receipt
from pos.core.model.receipt_product import ReceiptProduct


class ReceiptRepository(Protocol):
    def setup(self) -> None:
        pass

    def create_receipt(self, receipt: Receipt) -> None:
        pass

    def add_product(self, receipt_uuid: UUID, product: ReceiptProduct) -> None:
        pass

    def read_receipt(self, uuid: UUID) -> Receipt:
        pass

    def contains_uuid(self, uuid: UUID) -> bool:
        pass

    def close_receipt(self, uuid: UUID, status: str) -> None:
        pass

    def delete_receipt(self, uuid: UUID) -> None:
        pass

    def is_closed(self, uuid: UUID) -> bool:
        pass
