from typing import Any

from app.crm.client import RetailCRMClient
from app.schemas.payments import PaymentCreate


class PaymentService:
    def __init__(self, crm: RetailCRMClient):
        self.crm = crm

    async def create_payment(self, data: PaymentCreate) -> dict[str, Any]:
        payload = {
            "amount": str(data.amount),
            "type": data.type,
            "order": {"id": data.order_id},
        }
        return await self.crm.create_payment(payload)
