from typing import Annotated

from fastapi import Depends
from fastapi.requests import Request

from pos.core.repository.product_repository.product_repository import ProductRepository
from pos.core.repository.receipt_repository.receipt_repository import ReceiptRepository
from pos.core.repository.sales_repository.sales_repository import SalesRepository
from pos.core.repository.unit_repository.unit_repository import UnitRepository


def get_unit_repository(request: Request) -> UnitRepository:
    return request.app.state.unit_repository  # type: ignore


def get_product_repository(request: Request) -> ProductRepository:
    return request.app.state.product_repository  # type: ignore


def get_receipt_repository(request: Request) -> ReceiptRepository:
    return request.app.state.receipt_repository  # type: ignore


def get_sales_repository(request: Request) -> SalesRepository:
    return request.app.state.sales_repository  # type: ignore


UnitRepositoryDependable = Annotated[UnitRepository, Depends(get_unit_repository)]

ProductRepositoryDependable = Annotated[
    ProductRepository, Depends(get_product_repository)
]

ReceiptRepositoryDependable = Annotated[
    ReceiptRepository, Depends(get_receipt_repository)
]

SalesRepositoryDependable = Annotated[SalesRepository, Depends(get_sales_repository)]
