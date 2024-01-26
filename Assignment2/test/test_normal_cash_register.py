from pos.cash_register.normal_cash_register import NormalCashRegister


def test_add_sale() -> None:
    cash_register = NormalCashRegister()

    cash_register.add_sale("lobio")

    assert len(cash_register.sales) == 1

    assert "lobio" in cash_register.sales

    assert cash_register.sales["lobio"] == 1

    cash_register.add_sale("lobio")

    assert cash_register.sales["lobio"] == 2


def test_add_revenue() -> None:
    cash_register = NormalCashRegister()

    cash_register.add_revenue(10, "card")

    assert len(cash_register.revenues) == 1

    assert "card" in cash_register.revenues

    assert cash_register.revenues["card"] == 10

    cash_register.add_revenue(20, "card")

    assert cash_register.revenues["card"] == 30


def test_get_report() -> None:
    cash_register = NormalCashRegister()

    cash_register.add_sale("lobio")
    cash_register.add_revenue(10, "card")

    report = cash_register.get_report()

    assert len(report.get_sales()) == 1
    assert len(report.get_revenue()) == 1

    assert report.get_sales()[0].get_product_name() == "lobio"
    assert report.get_sales()[0].get_sales() == 1

    assert report.get_revenue()[0].get_payment_method() == "card"
    assert report.get_revenue()[0].get_amount() == 10


def test_clear() -> None:
    cash_register = NormalCashRegister()

    cash_register.add_sale("lobio")
    cash_register.add_revenue(10, "card")

    cash_register.clear()

    assert len(cash_register.get_report().get_sales()) == 0
    assert len(cash_register.get_report().get_revenue()) == 0
