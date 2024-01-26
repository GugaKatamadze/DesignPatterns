import random

from pos.product.iproduct import IProduct
from pos.product_picker.picked_product import PickedProduct
from pos.repository.repository import Repository


class RandomProductPicker:
    def __init__(self, repository: Repository):
        self.repository = repository

    def pick_products(self) -> list[PickedProduct]:
        random_products: list[PickedProduct] = list()

        products: list[IProduct] = self.repository.get_all_products()

        for _ in range(1, 10):
            index = random.randint(0, len(products) - 1)
            amount = random.randint(1, 10)

            random_products.append(PickedProduct(products[index], amount))

        return random_products
