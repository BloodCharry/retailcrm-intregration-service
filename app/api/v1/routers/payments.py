from typing import Any

from fastapi import APIRouter

from app.api.v1.deps import CRMClientDep
from app.schemas.payments import PaymentCreate
from app.services.payments import PaymentService

router = APIRouter()


@router.post("/payments")
async def create_payment(data: PaymentCreate, crm: CRMClientDep) -> dict[str, Any]:
    service = PaymentService(crm)
    return await service.create_payment(data)
