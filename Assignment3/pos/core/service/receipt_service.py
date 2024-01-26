from uuid import UUID, uuid4

from pos.core.errors import DoesNotExistError, ReceiptIsClosedError
from pos.core.model.receipt import Receipt
from pos.core.model.receipt_product import ReceiptProduct
from pos.core.repository.product_repository.product_repository import ProductRepository
from pos.core.repository.receipt_repository.receipt_repository import ReceiptRepository


class ReceiptService:
    def __init__(
        self,
        receipt_repository: ReceiptRepository,
        product_repository: ProductRepository,
    ) -> None:
        self.receipt_repository = receipt_repository
        self.product_repository = product_repository

    def create_receipt(self) -> Receipt:
        receipt_uuid = uuid4()

        receipt = Receipt(receipt_uuid, "open", [], 0)

        self.receipt_repository.create_receipt(receipt)

        return self.receipt_repository.read_receipt(receipt_uuid)

    def add_product(
        self, receipt_uuid: UUID, product_uuid: UUID, quantity: int
    ) -> Receipt:
        if self.receipt_repository.is_closed(receipt_uuid):
            raise ReceiptIsClosedError

        price = self.product_repository.get_price(product_uuid)
        total = quantity * price

        product = ReceiptProduct(product_uuid, quantity, price, total)

        self.receipt_repository.add_product(receipt_uuid, product)

        return self.receipt_repository.read_receipt(receipt_uuid)

    def read_receipt(self, uuid: UUID) -> Receipt:
        if not self.receipt_repository.contains_uuid(uuid):
            raise DoesNotExistError

        return self.receipt_repository.read_receipt(uuid)

    def close_receipt(self, uuid: UUID, status: str) -> None:
        if not self.receipt_repository.contains_uuid(uuid):
            raise DoesNotExistError

        self.receipt_repository.close_receipt(uuid, status)

    def delete_receipt(self, uuid: UUID) -> None:
        if not self.receipt_repository.contains_uuid(uuid):
            raise DoesNotExistError

        if self.receipt_repository.is_closed(uuid):
            raise ReceiptIsClosedError

        self.receipt_repository.delete_receipt(uuid)
