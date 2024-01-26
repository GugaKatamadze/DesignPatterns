from pos.product.product import Product
from pos.product_picker.picked_product import PickedProduct


def test_get_product() -> None:
    picked_product = PickedProduct(Product("lobio", 100), 50)

    assert picked_product.get_product().get_name() == "lobio"
    assert picked_product.get_product().get_price() == 100


def test_get_amount() -> None:
    picked_product = PickedProduct(Product("lobio", 100), 50)

    assert picked_product.get_amount() == 50


def test_get_total_price() -> None:
    picked_product = PickedProduct(Product("lobio", 100), 50)

    assert picked_product.get_total_price() == 5000


def test_get_name() -> None:
    picked_product = PickedProduct(Product("lobio", 100), 50)

    assert picked_product.get_name() == "lobio"
