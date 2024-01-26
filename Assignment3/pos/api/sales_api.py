from fastapi import APIRouter
from pydantic import BaseModel
from starlette.responses import JSONResponse

from pos.api.dependables import SalesRepositoryDependable

sales_api = APIRouter()


class SalesResponse(BaseModel):  # type: ignore
    n_receipts: int
    revenue: float


@sales_api.get("/sales", response_model=SalesResponse)  # type: ignore
def read_sales(sales_repository: SalesRepositoryDependable) -> JSONResponse:
    sales = sales_repository.read_sales()

    return JSONResponse(
        status_code=200,
        content={
            "sales": {
                "n_receipts": sales.get_n_receipts(),
                "revenue": sales.get_revenue(),
            }
        },
    )
