from pos.product.pack_of_products import PackOfProducts
from pos.product.product import Product
from pos.product_decorator.discount import Discount


def test_product() -> None:
    product = Product("lobio", 100)

    assert product.get_name() == "lobio"
    assert product.get_price() == 100


def test_pack_of_products() -> None:
    pack = PackOfProducts()

    pack.add_product(Product("achma", 40))

    assert pack.get_price() == 40
    assert pack.get_name() == "Pack of 1 achmas"

    pack.add_product(Product("achma", 40))

    assert pack.get_name() == "Pack of 2 achmas"

    assert pack.get_price() == 80

    another_pack = PackOfProducts()

    another_pack.add_product(Product("achma", 40))
    another_pack.add_product(Product("achma", 40))

    pack.add_product(another_pack)

    assert pack.get_price() == 160


def test_product_discount() -> None:
    discounted_achma = Discount(20, Product("achma", 40))

    assert discounted_achma.get_price() == 32

    pack = PackOfProducts()

    pack.add_product(Product("achma", 40))
    pack.add_product(Product("achma", 40))

    discounted_pack_of_achmas = Discount(50, pack)

    assert discounted_pack_of_achmas.get_price() == 40
