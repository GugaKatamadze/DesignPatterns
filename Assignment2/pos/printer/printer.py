from typing import Protocol

from pos.product.iproduct import IProduct
from pos.report.report import Report


class Printer(Protocol):
    def print_menu(self, products: list[IProduct]) -> None:
        pass

    def print_receipt(self, receipt: dict[IProduct, int]) -> None:
        pass

    def print_report(self, report: Report) -> None:
        pass
