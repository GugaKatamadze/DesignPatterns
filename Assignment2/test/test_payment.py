from pos.payment_method_picker.payment_methods import PaymentMethods
from pos.uncategorized.payment import Payment


def test_get_amount() -> None:
    payment = Payment(10, PaymentMethods.CARD)

    assert payment.get_amount() == 10
    assert payment.get_payment_method() == PaymentMethods.CARD
