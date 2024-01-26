from fastapi import FastAPI

from pos.api.product_api import product_api
from pos.api.receipt_api import receipt_api
from pos.api.sales_api import sales_api
from pos.api.unit_api import unit_api
from pos.core.repository.product_repository.sqlite_product_repository import (
    SQLiteProductRepository,
)
from pos.core.repository.receipt_repository.sqlite_receipt_repository import (
    SQLiteReceiptRepository,
)
from pos.core.repository.sales_repository.sqlite_sales_repository import (
    SQLiteSalesRepository,
)
from pos.core.repository.unit_repository.sqlite_unit_repository import (
    SQLiteUnitRepository,
)


def setup_for_production(database_name: str) -> FastAPI:
    return setup(database_name)


def setup_for_testing() -> FastAPI:
    return setup("test.db")


def setup(database_name: str) -> FastAPI:
    app = FastAPI()

    app.include_router(unit_api)
    app.include_router(product_api)
    app.include_router(receipt_api)
    app.include_router(sales_api)

    unit_repository = SQLiteUnitRepository(database_name)
    product_repository = SQLiteProductRepository(database_name)
    receipt_repository = SQLiteReceiptRepository(database_name)
    sales_repository = SQLiteSalesRepository(database_name)

    app.state.unit_repository = unit_repository
    app.state.product_repository = product_repository
    app.state.receipt_repository = receipt_repository
    app.state.sales_repository = sales_repository

    unit_repository.setup()
    product_repository.setup()
    receipt_repository.setup()
    sales_repository.setup()

    return app
