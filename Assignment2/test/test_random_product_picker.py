from typing import Tuple

from pos.product.iproduct import IProduct
from pos.product.product import Product
from pos.product_picker.random_product_picker import RandomProductPicker
from pos.report.report import Report


class LobioRepository:
    def __init__(self) -> None:
        self.products: list[IProduct] = list()

    def setup(self) -> None:
        pass

    def get_all_products(self) -> list[IProduct]:
        return [Product("mwvane lobio", 1), Product("default lobio", 100)]

    def add_sale(self, product: IProduct) -> None:
        pass

    def add_revenue(self, amount: float, payment_method: str) -> None:
        pass

    def get_report(self) -> Report:
        return Report(list(), list())

    def get_customer_amount_discount(self, customer_amount: int) -> Tuple[bool, int]:
        return False, 0


def test_random_product_picker() -> None:
    picked_products = RandomProductPicker(LobioRepository()).pick_products()

    for picked in picked_products:
        assert picked.get_name() in ["mwvane lobio", "default lobio"]
