from uuid import UUID

from fastapi import APIRouter
from pydantic import BaseModel
from starlette.responses import JSONResponse

from pos.api.dependables import ProductRepositoryDependable
from pos.core.errors import AlreadyExistsError, DoesNotExistError
from pos.core.service.product_service import ProductService

product_api = APIRouter()


class CreateProductRequest(BaseModel):  # type: ignore
    unit_id: UUID
    name: str
    barcode: str
    price: float


class ProductResponse(BaseModel):  # type: ignore
    id: str
    unit_id: str
    name: str
    barcode: str
    price: float


class ProductListResponse(BaseModel):  # type: ignore
    products: list[ProductResponse]


@product_api.post("/products", response_model=ProductResponse)  # type: ignore
def create_product(
    request: CreateProductRequest, product_repository: ProductRepositoryDependable
) -> JSONResponse:
    unit_uuid = request.unit_id
    name = request.name
    barcode = request.barcode
    price = request.price

    try:
        product = ProductService(product_repository).create_product(
            unit_uuid, name, barcode, price
        )

        return JSONResponse(
            status_code=201,
            content={
                "product": {
                    "id": str(product.get_uuid()),
                    "unit_id": str(product.get_unit_uuid()),
                    "name": product.get_name(),
                    "barcode": product.get_barcode(),
                    "price": product.get_price(),
                }
            },
        )
    except AlreadyExistsError:
        return JSONResponse(
            status_code=409,
            content={
                "error": {"message": f"Product with barcode <{barcode}> already exists"}
            },
        )


@product_api.get("/products/{uuid}", response_model=ProductResponse)  # type: ignore
def read_product(
    uuid: UUID, product_repository: ProductRepositoryDependable
) -> JSONResponse:
    try:
        product = ProductService(product_repository).read_product(uuid)

        return JSONResponse(
            status_code=200,
            content={
                "product": {
                    "id": str(product.get_uuid()),
                    "unit_id": str(product.get_unit_uuid()),
                    "name": product.get_name(),
                    "barcode": product.get_barcode(),
                    "price": product.get_price(),
                }
            },
        )
    except DoesNotExistError:
        return JSONResponse(
            status_code=404,
            content={"error": {"message": f"Product with id <{uuid}> does not exist"}},
        )


@product_api.get("/products", response_model=ProductListResponse)  # type: ignore
def read_products(product_repository: ProductRepositoryDependable) -> JSONResponse:
    return JSONResponse(
        status_code=200,
        content={
            "products": [
                {
                    "id": str(product.get_uuid()),
                    "unit_id": str(product.get_unit_uuid()),
                    "name": product.get_name(),
                    "barcode": product.get_barcode(),
                    "price": product.get_price(),
                }
                for product in ProductService(product_repository).read_products()
            ]
        },
    )


@product_api.patch("/products/{uuid}")  # type: ignore
def update_product(
    uuid: UUID, price: float, product_repository: ProductRepositoryDependable
) -> JSONResponse:
    try:
        ProductService(product_repository).update_product(uuid, price)

        return JSONResponse(status_code=200, content={})
    except DoesNotExistError:
        return JSONResponse(
            status_code=404,
            content={"error": {"message": f"Product with id <{uuid}> does not exist"}},
        )
