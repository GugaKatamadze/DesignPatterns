from pos.report.revenue_info import RevenueInfo
from pos.report.sales_info import SalesInfo


class Report:
    def __init__(self, sales: list[SalesInfo], revenue: list[RevenueInfo]) -> None:
        self.sales = sales
        self.revenue = revenue

    def get_sales(self) -> list[SalesInfo]:
        return self.sales

    def get_revenue(self) -> list[RevenueInfo]:
        return self.revenue
