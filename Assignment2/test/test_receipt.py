from pos.product.iproduct import IProduct
from pos.product.product import Product
from pos.uncategorized.receipt import Receipt


def test_get_products() -> None:
    receipt = Receipt()

    assert len(receipt.get_products()) == 0

    receipt.products[Product("pilmenebi", 13)] = 1

    products: dict[IProduct, int] = receipt.get_products()

    assert len(products) == 1

    product_names = list()

    for product, amount in products.items():
        product_names.append((product.get_name(), amount))

    assert ("pilmenebi", 1) in product_names

    receipt.products[Product("varenikebi", 7)] = 2

    products = receipt.get_products()

    assert len(products) == 2

    product_names = list()

    for product, amount in products.items():
        product_names.append((product.get_name(), amount))

    assert ("varenikebi", 2) in product_names


def test_add_item() -> None:
    receipt = Receipt()

    receipt.add_item(Product("pilmenebi", 13))

    products: dict[IProduct, int] = receipt.get_products()

    assert len(products) == 1

    product_names = list()

    for product, amount in products.items():
        product_names.append((product.get_name(), amount))

    assert ("pilmenebi", 1) in product_names

    receipt.add_item(Product("varenikebi", 7))

    products = receipt.get_products()

    assert len(products) == 2

    product_names = list()

    for product, amount in products.items():
        product_names.append((product.get_name(), amount))

    assert ("varenikebi", 1) in product_names


def test_add_items() -> None:
    receipt = Receipt()

    receipt.add_items(Product("pilmenebi", 13), 2)

    assert len(receipt.get_products()) == 1


def test_get_total_price() -> None:
    receipt = Receipt()

    receipt.add_item(Product("pilmenebi", 13))

    assert receipt.get_total_price() == 13

    receipt.add_items(Product("varenikebi", 7), 2)

    assert receipt.get_total_price() == 27
