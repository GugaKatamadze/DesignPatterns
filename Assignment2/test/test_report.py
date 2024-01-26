from pos.report.report import Report
from pos.report.revenue_info import RevenueInfo
from pos.report.sales_info import SalesInfo


def test_sales_info() -> None:
    sales_info = SalesInfo("borshi", 500)

    assert sales_info.get_product_name() == "borshi"
    assert sales_info.get_sales() == 500


def test_revenue_info() -> None:
    revenue_info = RevenueInfo("card", 10)

    assert revenue_info.get_payment_method() == "card"
    assert revenue_info.get_amount() == 10


def test_report() -> None:
    sales: list[SalesInfo] = list()
    revenue: list[RevenueInfo] = list()

    sales.append(SalesInfo("borshi", 500))
    revenue.append(RevenueInfo("card", 10))

    report = Report(sales, revenue)

    assert len(report.get_sales()) == 1
    assert len(report.get_revenue()) == 1

    assert report.get_sales()[0].get_product_name() == "borshi"
    assert report.get_sales()[0].get_sales() == 500

    assert report.get_revenue()[0].get_payment_method() == "card"
    assert report.get_revenue()[0].get_amount() == 10
