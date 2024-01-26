from pos.product.iproduct import IProduct
from pos.report.report import Report
from pos.report.revenue_info import RevenueInfo
from pos.report.sales_info import SalesInfo


class FancyPrinter:
    def print_menu(self, products: list[IProduct]) -> None:
        if len(products) == 0:
            return

        name_column_width = max(len(product.get_name()) for product in products) + 2
        price_column_width = (
            max(len(str(product.get_price())) for product in products) + 2
        )

        print("Product", end="")

        remaining_space_amount = name_column_width - len("Product")

        self._print_chars(" ", remaining_space_amount)

        print("| Price")

        self._print_chars("-", name_column_width)

        print("|", end="")

        self._print_chars("-", price_column_width)

        print()

        for product in products:
            print(product.get_name(), end="")

            self._print_chars(" ", name_column_width - len(product.get_name()))

            print(f"| {product.get_price()}")

    def print_receipt(self, receipt: dict[IProduct, int]) -> None:
        if len(receipt) == 0:
            return

        name_column_width = self._get_name_column_width(receipt)
        units_column_width = self._get_units_column_width(receipt)
        price_column_width = self._get_price_column_width(receipt)
        total_column_width = self._get_total_column_width(receipt)

        print("Product", end="")
        self._print_chars(" ", name_column_width - len("Product"))
        print("|", end="")
        self._print_section("Units", units_column_width - len("Units"))
        self._print_section("Price", price_column_width - len("Price"))
        self._print_section("Total", total_column_width - len("Total"))
        print()

        self._print_chars("-", name_column_width)
        print("|", end="")
        self._print_chars("-", units_column_width)
        print("|", end="")
        self._print_chars("-", price_column_width)
        print("|", end="")
        self._print_chars("-", total_column_width)
        print("|")

        for product, amount in receipt.items():
            print(product.get_name(), end="")

            self._print_chars(" ", name_column_width - len(product.get_name()))

            print("|", end="")

            self._print_product_info(units_column_width, amount)
            self._print_product_info(price_column_width, product.get_price())
            self._print_product_info(
                total_column_width, round(product.get_price() * amount, 2)
            )

            print()

    def print_report(self, report: Report) -> None:
        sales = report.get_sales()
        revenue = report.get_revenue()

        if len(sales) > 0:
            self._print_sales_info(sales)
            print()

        if len(revenue) > 0:
            self._print_revenue_info(revenue)
            print()

    def _print_sales_info(self, sales_info: list[SalesInfo]) -> None:
        if len(sales_info) == 0:
            return

        product_column_width = max(
            max(len(product.get_product_name()) for product in sales_info) + 2,
            len("Product") + 2,
        )
        sales_column_width = max(
            max(len(str(product.get_sales())) for product in sales_info) + 2,
            len("Sales") + 2,
        )

        print("Product", end="")

        remaining_space_amount = product_column_width - len("Product")

        self._print_chars(" ", remaining_space_amount)

        print("| Sales")

        self._print_chars("-", product_column_width)

        print("|", end="")

        self._print_chars("-", sales_column_width)

        print()

        for product in sales_info:
            print(product.get_product_name(), end="")

            self._print_chars(
                " ", product_column_width - len(product.get_product_name())
            )

            print(f"| {product.get_sales()}")

    def _print_revenue_info(self, revenue_info: list[RevenueInfo]) -> None:
        if len(revenue_info) == 0:
            return

        payment_column_width = max(
            max(len(revenue.get_payment_method()) for revenue in revenue_info) + 2,
            len("Payment") + 2,
        )
        revenue_column_width = max(
            max(len(str(revenue.get_amount())) for revenue in revenue_info) + 2,
            len("Revenue") + 2,
        )

        print("Payment", end="")

        remaining_space_amount = payment_column_width - len("Payment")

        self._print_chars(" ", remaining_space_amount)

        print("| Revenue")

        self._print_chars("-", payment_column_width)

        print("|", end="")

        self._print_chars("-", revenue_column_width)

        print()

        for revenue in revenue_info:
            print(revenue.get_payment_method(), end="")

            self._print_chars(
                " ", payment_column_width - len(revenue.get_payment_method())
            )

            print(f"| {revenue.get_amount()}")

    @staticmethod
    def _get_name_column_width(receipt: dict[IProduct, int]) -> int:
        return max(
            max(len(product.get_name()) for product in receipt.keys()) + 2,
            len("Product") + 2,
        )

    @staticmethod
    def _get_units_column_width(receipt: dict[IProduct, int]) -> int:
        return max(
            max(len(str(amount)) for amount in receipt.values()) + 2, len("Units") + 2
        )

    @staticmethod
    def _get_price_column_width(receipt: dict[IProduct, int]) -> int:
        return max(
            max(len(str(product.get_price())) for product, amount in receipt.items())
            + 2,
            len("Price") + 2,
        )

    @staticmethod
    def _get_total_column_width(receipt: dict[IProduct, int]) -> int:
        return max(
            max(
                len(str(round(product.get_price() * amount, 2)))
                for product, amount in receipt.items()
            )
            + 2,
            len("Total") + 2,
        )

    @staticmethod
    def _print_chars(char: str, amount: int) -> None:
        for _ in range(0, amount):
            print(char, end="")

    @classmethod
    def _print_section(cls, section_name: str, space_amount_left: int) -> None:
        cls._print_chars(" ", int(space_amount_left / 2))

        print(section_name, end="")

        cls._print_chars(" ", int(space_amount_left / 2) + space_amount_left % 2)

        print("|", end="")

    @classmethod
    def _print_product_info(cls, section_width: int, value: float) -> None:
        value_str = str(value)

        cls._print_chars(" ", int((section_width - len(value_str)) / 2))

        print(value_str, end="")

        cls._print_chars(
            " ",
            int((section_width - len(value_str)) / 2)
            + int((section_width - len(value_str)) % 2),
        )

        print("|", end="")
