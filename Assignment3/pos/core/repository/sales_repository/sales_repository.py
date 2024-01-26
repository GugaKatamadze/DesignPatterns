from typing import Protocol

from pos.core.model.sales import Sales


class SalesRepository(Protocol):
    def setup(self) -> None:
        pass

    def read_sales(self) -> Sales:
        pass
