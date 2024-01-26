from pos.customer.customer import Customer
from pos.payment_method.card import Card
from pos.payment_method.payment_method import PaymentMethod
from pos.payment_method_picker.payment_methods import PaymentMethods
from pos.product.product import Product
from pos.product_picker.picked_product import PickedProduct


class LobioPicker:
    def pick_products(self) -> list[PickedProduct]:
        return [PickedProduct(Product("lobio", 100), 1)]


class CardPicker:
    def pick(self) -> PaymentMethod:
        return Card()


def test_pick_products() -> None:
    customer = Customer(LobioPicker(), CardPicker())

    picked_products = customer.pick_products()

    assert len(picked_products) == 1

    assert picked_products[0].get_name() == "lobio"
    assert picked_products[0].get_amount() == 1


def test_pay() -> None:
    customer = Customer(LobioPicker(), CardPicker())

    customer.pay(10)

    assert customer.last_paid_amount == 10
    assert customer.last_used_payment_method == PaymentMethods.CARD


def test_get_last_payment() -> None:
    customer = Customer(LobioPicker(), CardPicker())

    customer.pay(10)

    last_payment = customer.get_last_payment()

    assert (10, PaymentMethods.CARD) == (
        last_payment.get_amount(),
        last_payment.get_payment_method(),
    )
