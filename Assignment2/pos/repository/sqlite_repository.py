import sqlite3
from typing import Tuple

from pos.product.iproduct import IProduct
from pos.product.pack_of_products import PackOfProducts
from pos.product.product import Product
from pos.product_decorator.discount import Discount
from pos.report.report import Report
from pos.report.revenue_info import RevenueInfo
from pos.report.sales_info import SalesInfo
from pos.repository.pack_info import PackInfo


class SQLiteRepository:
    def __init__(self, database_name: str) -> None:
        self.connection = sqlite3.connect(database_name)
        self.cursor = self.connection.cursor()

    def setup(self) -> None:
        self._create_products()
        self._create_pack_discounts()
        self._create_sales()
        self._create_revenue()
        self._create_customer_amount_discounts()

        self.connection.commit()

    def get_all_products(self) -> list[IProduct]:
        self.cursor.row_factory = lambda cursor, row: Product(*row)

        products: list[IProduct] = self.cursor.execute(
            "SELECT * FROM products"
        ).fetchall()

        self.cursor.row_factory = None

        products.extend(self._get_all_packs_of_products())

        return products

    def add_sale(self, product: IProduct) -> None:
        self.cursor.execute(
            "SELECT sales FROM sales WHERE name = ?", (product.get_name(),)
        )
        result = self.cursor.fetchone()

        if result is None:
            self.cursor.execute(
                "INSERT INTO sales VALUES (?, ?)", (product.get_name(), 1)
            )
        else:
            self.cursor.execute(
                "UPDATE sales SET sales = ? WHERE name = ?",
                (result[0] + 1, product.get_name()),
            )

        self.connection.commit()

    def add_revenue(self, amount: float, payment_method: str) -> None:
        self.cursor.execute(
            "SELECT revenue FROM revenues WHERE name = ?", (payment_method,)
        )

        result = self.cursor.fetchone()

        if result is None:
            self.cursor.execute(
                "INSERT INTO revenues VALUES (?, ?)", (payment_method, amount)
            )
        else:
            self.cursor.execute(
                "UPDATE revenues SET revenue = ? WHERE name = ?",
                (result[0] + amount, payment_method),
            )

        self.connection.commit()

    def get_report(self) -> Report:
        self.cursor.row_factory = lambda cursor, row: SalesInfo(*row)

        sales_info: list[SalesInfo] = self.cursor.execute(
            "SELECT * FROM sales"
        ).fetchall()

        self.cursor.row_factory = lambda cursor, row: RevenueInfo(*row)

        revenue_info = self.cursor.execute("SELECT * FROM revenues").fetchall()

        self.cursor.row_factory = None

        return Report(sales_info, revenue_info)

    def get_customer_amount_discount(self, customer_amount: int) -> Tuple[bool, int]:
        result = self.cursor.execute(
            "SELECT discount FROM customer_amount_discounts WHERE amount = ?",
            (customer_amount,),
        ).fetchone()

        if result is None:
            return False, 0
        else:
            return True, result[0]

    def _get_all_packs_of_products(self) -> list[IProduct]:
        packs_of_products: list[IProduct] = list()

        self.cursor.row_factory = lambda cursor, row: PackInfo(*row)

        pack_infos: list[PackInfo] = self.cursor.execute(
            "SELECT * FROM pack_discounts"
        ).fetchall()

        self.cursor.row_factory = None

        for pack_info in pack_infos:
            product = Product(
                pack_info.get_name(), self._get_product_price(pack_info.get_name())
            )

            pack_of_products = PackOfProducts()

            pack_of_products.add_products(product, pack_info.get_amount())

            discounted_product = Discount(pack_info.get_discount(), pack_of_products)

            packs_of_products.append(discounted_product)

        return packs_of_products

    def _get_product_price(self, product_name: str) -> float:
        return float(
            self.cursor.execute(
                "SELECT price FROM products WHERE name = ?", (product_name,)
            ).fetchone()[0]
        )

    def _create_products(self) -> None:
        self.cursor.execute("DROP TABLE IF EXISTS products")
        self.cursor.execute("CREATE TABLE products(name str UNIQUE , price float)")
        self.cursor.execute("INSERT INTO products VALUES ('water', 1)")
        self.cursor.execute("INSERT INTO products VALUES ('pizza', 15)")
        self.cursor.execute("INSERT INTO products VALUES ('burger', 25)")
        self.cursor.execute("INSERT INTO products VALUES ('sushi', 30)")
        self.cursor.execute("INSERT INTO products VALUES ('lobio', 100)")

    def _create_pack_discounts(self) -> None:
        self.cursor.execute("DROP TABLE IF EXISTS pack_discounts")
        self.cursor.execute(
            "CREATE TABLE pack_discounts(name str, amount int, discount int)"
        )
        self.cursor.execute("INSERT INTO pack_discounts VALUES ('water', 6, 20)")
        self.cursor.execute("INSERT INTO pack_discounts VALUES ('pizza', 3, 40)")

    def _create_sales(self) -> None:
        self.cursor.execute("DROP TABLE IF EXISTS sales")
        self.cursor.execute("CREATE TABLE sales(name str UNIQUE , sales int)")

    def _create_revenue(self) -> None:
        self.cursor.execute("DROP TABLE IF EXISTS revenues")
        self.cursor.execute(
            "CREATE TABLE revenues(name payment_method UNIQUE , revenue float)"
        )

    def _create_customer_amount_discounts(self) -> None:
        self.cursor.execute("DROP TABLE IF EXISTS customer_amount_discounts")
        self.cursor.execute(
            "CREATE TABLE customer_amount_discounts(amount int UNIQUE , discount int)"
        )
        self.cursor.execute("INSERT INTO customer_amount_discounts VALUES (10, 20)")
