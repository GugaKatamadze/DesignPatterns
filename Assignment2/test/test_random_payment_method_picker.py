from pos.payment_method.card import Card
from pos.payment_method.cash import Cash
from pos.payment_method_picker.random_payment_method_picker import (
    RandomPaymentMethodPicker,
)


def test_random_payment_method_picker() -> None:
    picked = RandomPaymentMethodPicker().pick()

    assert isinstance(picked, Card) or isinstance(picked, Cash)
