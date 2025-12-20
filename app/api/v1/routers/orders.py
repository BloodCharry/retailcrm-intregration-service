from typing import Any

from fastapi import APIRouter

from app.api.v1.deps import CRMClientDep
from app.schemas.orders import OrderCreate
from app.services.orders import OrderService

router = APIRouter()


@router.get("/orders")
async def list_orders(crm: CRMClientDep) -> dict[str, Any]:
    service = OrderService(crm)
    return await service.list_orders({}, page=1, limit=20)


@router.post("/orders")
async def create_order(data: OrderCreate, crm: CRMClientDep) -> dict[str, Any]:
    service = OrderService(crm)
    return await service.create_order(data)
