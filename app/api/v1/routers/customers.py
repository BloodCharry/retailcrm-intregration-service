from typing import Any

from fastapi import APIRouter

from app.api.v1.deps import CRMClientDep
from app.schemas.customers import CustomerCreate
from app.services.customers import CustomerService

router = APIRouter()


@router.get("/customers")
async def list_customers(crm: CRMClientDep) -> dict[str, Any]:
    service = CustomerService(crm)
    return await service.list_customers({}, page=1, limit=20)


@router.post("/customers")
async def create_customer(data: CustomerCreate, crm: CRMClientDep) -> dict[str, Any]:
    service = CustomerService(crm)
    return await service.create_customer(data)
