from uuid import UUID

from fastapi import APIRouter
from pydantic import BaseModel
from starlette.responses import JSONResponse

from pos.api.dependables import ProductRepositoryDependable, ReceiptRepositoryDependable
from pos.core.errors import DoesNotExistError, ReceiptIsClosedError
from pos.core.service.receipt_service import ReceiptService

receipt_api = APIRouter()


class ReceiptProductResponse(BaseModel):  # type: ignore
    id: str
    quantity: int
    price: float
    total: float


class CreateReceiptResponse(BaseModel):  # type: ignore
    id: UUID
    status: str
    products: list[ReceiptProductResponse]
    total: float


class AddProductRequest(BaseModel):  # type: ignore
    id: UUID
    quantity: int


@receipt_api.post("/receipts", response_model=CreateReceiptResponse)  # type: ignore
def create_receipt(
    receipt_repository: ReceiptRepositoryDependable,
    product_repository: ProductRepositoryDependable,
) -> JSONResponse:
    receipt = ReceiptService(receipt_repository, product_repository).create_receipt()

    return JSONResponse(
        status_code=201,
        content={
            "receipt": {
                "id": str(receipt.get_uuid()),
                "status": "open",
                "products": [],
                "total": 0,
            }
        },
    )


@receipt_api.post(
    "/receipts/{receipt_uuid}/products", response_model=CreateReceiptResponse
)  # type: ignore
def add_product(
    receipt_uuid: UUID,
    request: AddProductRequest,
    receipt_repository: ReceiptRepositoryDependable,
    product_repository: ProductRepositoryDependable,
) -> JSONResponse:
    product_uuid = request.id
    quantity = request.quantity

    try:
        receipt = ReceiptService(receipt_repository, product_repository).add_product(
            receipt_uuid, product_uuid, quantity
        )

        products_json = []

        for receipt_product in receipt.get_products():
            receipt_product_json = {
                "id": str(receipt_product.get_uuid()),
                "quantity": receipt_product.get_quantity(),
                "price": receipt_product.get_price(),
                "total": receipt_product.get_total(),
            }

            products_json.append(receipt_product_json)

        return JSONResponse(
            status_code=201,
            content={
                "receipt": {
                    "id": str(receipt.get_uuid()),
                    "status": receipt.get_status(),
                    "products": products_json,
                    "total": receipt.get_total(),
                }
            },
        )
    except ReceiptIsClosedError:
        return JSONResponse(
            status_code=403,
            content={
                "error": {"message": f"Receipt with id <{receipt_uuid}> is closed"}
            },
        )


@receipt_api.get(
    "/receipts/{uuid}", response_model=CreateReceiptResponse
)  # type: ignore
def read_receipt(
    uuid: UUID,
    receipt_repository: ReceiptRepositoryDependable,
    product_repository: ProductRepositoryDependable,
) -> JSONResponse:
    try:
        receipt = ReceiptService(receipt_repository, product_repository).read_receipt(
            uuid
        )

        products_json = []

        for receipt_product in receipt.get_products():
            receipt_product_json = {
                "id": str(receipt_product.get_uuid()),
                "quantity": receipt_product.get_quantity(),
                "price": receipt_product.get_price(),
                "total": receipt_product.get_total(),
            }

            products_json.append(receipt_product_json)

        return JSONResponse(
            status_code=200,
            content={
                "receipt": {
                    "id": str(receipt.get_uuid()),
                    "status": receipt.get_status(),
                    "products": products_json,
                    "total": receipt.get_total(),
                }
            },
        )
    except DoesNotExistError:
        return JSONResponse(
            status_code=404,
            content={"error": {"message": f"Receipt with id <{uuid}> does not exist"}},
        )


@receipt_api.patch("/receipts/{uuid}")  # type: ignore
def close_receipt(
    uuid: UUID,
    status: str,
    receipt_repository: ReceiptRepositoryDependable,
    product_repository: ProductRepositoryDependable,
) -> JSONResponse:
    try:
        ReceiptService(receipt_repository, product_repository).close_receipt(
            uuid, status
        )

        return JSONResponse(status_code=200, content={})
    except DoesNotExistError:
        return JSONResponse(
            status_code=404,
            content={"error": {"message": f"Receipt with id <{uuid}> does not exist"}},
        )


@receipt_api.delete("/receipts/{uuid}")  # type: ignore
def delete_receipt(
    uuid: UUID,
    receipt_repository: ReceiptRepositoryDependable,
    product_repository: ProductRepositoryDependable,
) -> JSONResponse:
    try:
        ReceiptService(receipt_repository, product_repository).delete_receipt(uuid)

        return JSONResponse(status_code=200, content={})
    except DoesNotExistError:
        return JSONResponse(
            status_code=404,
            content={"error": {"message": f"Receipt with id <{uuid}> does not exist"}},
        )
    except ReceiptIsClosedError:
        return JSONResponse(
            status_code=403,
            content={"error": {"message": f"Receipt with id <{uuid}> is closed"}},
        )
