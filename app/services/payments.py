from typing import Any

from app.crm.client import RetailCRMClient
from app.schemas.payments import PaymentCreate


class PaymentService:
    def __init__(self, crm: RetailCRMClient):
        self.crm = crm

    async def create_payment(self, data: PaymentCreate) -> dict[str, Any]:
        return await self.crm.create_payment(data.model_dump())
