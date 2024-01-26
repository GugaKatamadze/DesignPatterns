from typing import Tuple

from pos.cash_register.cash_register import CashRegister
from pos.cashier.icashier import ICashier
from pos.customer.icustomer import ICustomer
from pos.printer.printer import Printer
from pos.report.report import Report
from pos.repository.repository import Repository


class Shift:
    def __init__(
        self,
        repository: Repository,
        cashier: ICashier,
        printer: Printer,
        cash_register: CashRegister,
    ):
        self.repository = repository
        self.cashier = cashier
        self.printer = printer
        self.cash_register = cash_register

    def serve_customer(self, customer: ICustomer, customer_amount: int) -> None:
        self.cashier.take_order(customer)

        receipt = self.cashier.get_receipt()

        self.printer.print_receipt(receipt.get_products())

        eligible, discount = self._check_discount_eligibility(customer_amount)

        total_price = receipt.get_total_price()

        if eligible:
            total_price = self._get_discount(total_price, discount)

        customer.pay(total_price)

        self.cashier.update_sales(self.cash_register, self.repository)
        self.cashier.update_revenue(
            self.cash_register, self.repository, customer.get_last_payment()
        )

        self.cashier.close_receipt()

    def get_report(self) -> Report:
        return self.cash_register.get_report()

    def end(self) -> None:
        self.cash_register.clear()

    def _check_discount_eligibility(self, customer_amount: int) -> Tuple[bool, int]:
        return self.repository.get_customer_amount_discount(customer_amount)

    def _get_discount(self, price: float, discount: int) -> float:
        return round((1 - discount / 100) * price, 2)
