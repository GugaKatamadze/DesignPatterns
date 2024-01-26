from typing import Protocol
from uuid import UUID

from pos.core.model.product import Product


class ProductRepository(Protocol):
    def setup(self) -> None:
        pass

    def create_product(self, product: Product) -> None:
        pass

    def read_product(self, uuid: UUID) -> Product:
        pass

    def read_products(self) -> list[Product]:
        pass

    def contains_barcode(self, barcode: str) -> bool:
        pass

    def contains_uuid(self, uuid: UUID) -> bool:
        pass

    def update_product(self, uuid: UUID, price: float) -> None:
        pass

    def get_price(self, uuid: UUID) -> float:
        pass
