from uuid import UUID, uuid4

from pos.core.errors import AlreadyExistsError, DoesNotExistError
from pos.core.model.product import Product
from pos.core.repository.product_repository.product_repository import ProductRepository


class ProductService:
    def __init__(self, repository: ProductRepository) -> None:
        self.repository = repository

    def create_product(
        self, unit_uuid: UUID, name: str, barcode: str, price: float
    ) -> Product:
        if self.repository.contains_barcode(barcode):
            raise AlreadyExistsError

        product_uuid = uuid4()

        product = Product(product_uuid, unit_uuid, name, barcode, price)

        self.repository.create_product(product)

        return self.repository.read_product(product_uuid)

    def read_product(self, uuid: UUID) -> Product:
        if not self.repository.contains_uuid(uuid):
            raise DoesNotExistError

        return self.repository.read_product(uuid)

    def read_products(self) -> list[Product]:
        return self.repository.read_products()

    def update_product(self, uuid: UUID, price: float) -> None:
        if not self.repository.contains_uuid(uuid):
            raise DoesNotExistError

        self.repository.update_product(uuid, price)
