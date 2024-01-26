from pos.core.model.sales import Sales
from pos.core.repository.sales_repository.sales_repository import SalesRepository


class SalesService:
    def __init__(self, sales_repository: SalesRepository) -> None:
        self.sales_repository = sales_repository

    def read_sales(self) -> Sales:
        return self.sales_repository.read_sales()
