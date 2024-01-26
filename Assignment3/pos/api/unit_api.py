from uuid import UUID

from fastapi import APIRouter
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from pos.api.dependables import UnitRepositoryDependable
from pos.core.errors import AlreadyExistsError, DoesNotExistError
from pos.core.service.unit_service import UnitService

unit_api = APIRouter()


class CreateUnitRequest(BaseModel):  # type: ignore
    name: str


class UnitResponse(BaseModel):  # type: ignore
    id: str
    name: str


@unit_api.post("/units", response_model=UnitResponse)  # type: ignore
def create_unit(
    request: CreateUnitRequest, unit_repository: UnitRepositoryDependable
) -> JSONResponse:
    name = request.name

    try:
        unit = UnitService(unit_repository).create_unit(name)

        return JSONResponse(
            status_code=201,
            content={"unit": {"id": str(unit.get_uuid()), "name": unit.get_name()}},
        )
    except AlreadyExistsError:
        return JSONResponse(
            status_code=409,
            content={"error": {"message": f"Unit with name <{name}> already exists"}},
        )


@unit_api.get("/units/{uuid}", response_model=UnitResponse)  # type: ignore
def read_unit(uuid: UUID, unit_repository: UnitRepositoryDependable) -> JSONResponse:
    try:
        unit = UnitService(unit_repository).read_unit(uuid)

        return JSONResponse(
            status_code=200,
            content={"unit": {"id": str(unit.get_uuid()), "name": unit.get_name()}},
        )
    except DoesNotExistError:
        return JSONResponse(
            status_code=404,
            content={"error": {"message": f"Unit with id <{uuid}> does not exist"}},
        )


@unit_api.get("/units", response_model=list[UnitResponse])  # type: ignore
def read_units(unit_repository: UnitRepositoryDependable) -> JSONResponse:
    return JSONResponse(
        status_code=200,
        content={
            "units": [
                {"id": unit.get_uuid(), "name": unit.get_name()}
                for unit in UnitService(unit_repository).read_units()
            ]
        },
    )
