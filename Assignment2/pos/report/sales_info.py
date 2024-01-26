class SalesInfo:
    def __init__(self, product_name: str, sales: int):
        self.product_name = product_name
        self.sales = sales

    def __repr__(self) -> str:
        return f"{self.product_name} {self.sales}"

    def get_product_name(self) -> str:
        return self.product_name

    def get_sales(self) -> int:
        return self.sales
