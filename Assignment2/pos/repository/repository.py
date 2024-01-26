from typing import Protocol, Tuple

from pos.product.iproduct import IProduct
from pos.report.report import Report


class Repository(Protocol):
    def setup(self) -> None:
        pass

    def get_all_products(self) -> list[IProduct]:
        pass

    def add_sale(self, product: IProduct) -> None:
        pass

    def add_revenue(self, amount: float, payment_method: str) -> None:
        pass

    def get_report(self) -> Report:
        pass

    def get_customer_amount_discount(self, customer_amount: int) -> Tuple[bool, int]:
        pass
