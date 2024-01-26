import random

import typer

from pos.cash_register.normal_cash_register import NormalCashRegister
from pos.cashier.cashier import Cashier
from pos.customer_factory.random_customer_factory import RandomCustomerFactory
from pos.printer.fancy_printer import FancyPrinter
from pos.repository.sqlite_repository import SQLiteRepository
from pos.uncategorized.shift import Shift

DATABASE_LOCATION = "pos.db"
MAX_SHIFT_AMOUNT = 3
CUSTOMER_AMOUNT_TO_REQUEST_TO_MAKE_REPORT = 20
CUSTOMER_AMOUNT_TO_REQUEST_TO_END_SHIFT = 100


class POS:
    @staticmethod
    def setup() -> None:
        SQLiteRepository(DATABASE_LOCATION).setup()

    @staticmethod
    def list() -> None:
        FancyPrinter().print_menu(
            SQLiteRepository(DATABASE_LOCATION).get_all_products()
        )

    @staticmethod
    def simulate() -> None:
        repository = SQLiteRepository(DATABASE_LOCATION)

        current_customer_number = 1

        for _ in range(0, MAX_SHIFT_AMOUNT):
            shift = Shift(repository, Cashier(), FancyPrinter(), NormalCashRegister())

            while True:
                customer_amount = random.randint(1, 10)

                shift.serve_customer(
                    RandomCustomerFactory().create(repository), customer_amount
                )

                if (
                    current_customer_number % CUSTOMER_AMOUNT_TO_REQUEST_TO_MAKE_REPORT
                    == 0
                ):
                    if typer.confirm("Do you want to make a report?"):
                        FancyPrinter().print_report(shift.get_report())

                if (
                    current_customer_number % CUSTOMER_AMOUNT_TO_REQUEST_TO_END_SHIFT
                    == 0
                ):
                    if typer.confirm("Do you want to end the shift?"):
                        shift.end()

                        current_customer_number += 1

                        break

                current_customer_number += 1

    @staticmethod
    def report() -> None:
        FancyPrinter().print_report(SQLiteRepository(DATABASE_LOCATION).get_report())
