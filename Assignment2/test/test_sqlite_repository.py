import sqlite3

from pos.product.iproduct import IProduct
from pos.product.product import Product
from pos.repository.sqlite_repository import SQLiteRepository


def test_setup() -> None:
    SQLiteRepository("test.db").setup()

    cursor = sqlite3.connect("test.db").cursor()

    table_names: list[str] = list()

    for result in cursor.execute("SELECT name FROM sqlite_master").fetchall():
        table_names.append(result[0])

    assert "products" in table_names
    assert "pack_discounts" in table_names
    assert "sales" in table_names
    assert "revenues" in table_names


def test_get_all_products() -> None:
    repository = SQLiteRepository("test.db")

    repository.setup()

    products: list[IProduct] = repository.get_all_products()

    assert len(products) == 7

    product_infos = list()

    for product in products:
        product_infos.append((product.get_name(), product.get_price()))

    assert ("water", 1) in product_infos
    assert ("pizza", 15) in product_infos
    assert ("burger", 25) in product_infos
    assert ("sushi", 30) in product_infos
    assert ("lobio", 100) in product_infos
    assert ("Pack of 6 waters", 4.8) in product_infos
    assert ("Pack of 3 pizzas", 27) in product_infos


def test_add_sale() -> None:
    repository = SQLiteRepository("test.db")

    repository.setup()

    repository.add_sale(Product("qalebis meqsikuri", 8))

    cursor = sqlite3.connect("test.db").cursor()

    sales = cursor.execute("SELECT * FROM sales").fetchall()

    assert len(sales) == 1

    assert sales[0][0] == "qalebis meqsikuri"
    assert sales[0][1] == 1

    repository.add_sale(Product("qalebis meqsikuri", 8))

    sales = cursor.execute("SELECT * FROM sales").fetchall()

    assert len(sales) == 1

    assert sales[0][0] == "qalebis meqsikuri"
    assert sales[0][1] == 2


def test_add_revenue() -> None:
    repository = SQLiteRepository("test.db")

    repository.setup()

    repository.add_revenue(10, "card")

    cursor = sqlite3.connect("test.db").cursor()

    revenues = cursor.execute("SELECT * FROM revenues").fetchall()

    assert len(revenues) == 1

    assert revenues[0][0] == "card"
    assert revenues[0][1] == 10

    repository.add_revenue(20, "card")

    sales = cursor.execute("SELECT * FROM revenues").fetchall()

    assert len(sales) == 1

    assert sales[0][0] == "card"
    assert sales[0][1] == 30


def test_get_report() -> None:
    repository = SQLiteRepository("test.db")

    repository.setup()

    repository.add_sale(Product("qalebis meqsikuri", 8))

    repository.add_revenue(10, "card")

    report = repository.get_report()

    assert len(report.get_sales()) == 1
    assert len(report.get_revenue()) == 1

    assert report.get_sales()[0].get_product_name() == "qalebis meqsikuri"
    assert report.get_sales()[0].get_sales() == 1

    assert report.get_revenue()[0].get_payment_method() == "card"
    assert report.get_revenue()[0].get_amount() == 10

    repository.add_sale(Product("arturas meqsikuri", 8))

    repository.add_revenue(10, "cash")

    report = repository.get_report()

    assert len(report.get_sales()) == 2
    assert len(report.get_revenue()) == 2

    sales_infos = list()

    for sales_info in report.get_sales():
        sales_infos.append((sales_info.get_product_name(), sales_info.get_sales()))

    revenue_infos = list()

    for revenue_info in report.get_revenue():
        revenue_infos.append(
            (revenue_info.get_payment_method(), revenue_info.get_amount())
        )

    assert ("qalebis meqsikuri", 1) in sales_infos
    assert ("arturas meqsikuri", 1) in sales_infos

    assert ("card", 10) in revenue_infos
    assert ("cash", 10) in revenue_infos


def test_get_customer_amount_discount() -> None:
    repository = SQLiteRepository("test.db")

    repository.setup()

    eligible, discount = repository.get_customer_amount_discount(1)

    assert not eligible

    eligible, discount = repository.get_customer_amount_discount(10)

    assert eligible
    assert discount == 20
