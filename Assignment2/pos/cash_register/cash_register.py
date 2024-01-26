from typing import Protocol

from pos.report.report import Report


class CashRegister(Protocol):
    def add_sale(self, product_name: str) -> None:
        pass

    def add_revenue(self, amount: float, payment_method: str) -> None:
        pass

    def get_report(self) -> Report:
        pass

    def clear(self) -> None:
        pass
