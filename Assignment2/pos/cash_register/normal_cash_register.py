from pos.report.report import Report
from pos.report.revenue_info import RevenueInfo
from pos.report.sales_info import SalesInfo


class NormalCashRegister:
    def __init__(self) -> None:
        self.sales: dict[str, int] = dict()
        self.revenues: dict[str, float] = dict()

    def add_sale(self, product_name: str) -> None:
        if product_name not in self.sales:
            self.sales[product_name] = 0

        self.sales[product_name] += 1

    def add_revenue(self, amount: float, payment_method: str) -> None:
        if payment_method not in self.revenues:
            self.revenues[payment_method] = 0

        self.revenues[payment_method] += amount

    def get_report(self) -> Report:
        sales_info: list[SalesInfo] = list()
        revenue_info: list[RevenueInfo] = list()

        for product_name, sales in self.sales.items():
            sales_info.append(SalesInfo(product_name, sales))

        for payment_method, amount in self.revenues.items():
            revenue_info.append(RevenueInfo(payment_method, amount))

        return Report(sales_info, revenue_info)

    def clear(self) -> None:
        self.sales.clear()
        self.revenues.clear()
