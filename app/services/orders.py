from typing import Any

from app.crm.client import RetailCRMClient
from app.schemas.orders import OrderCreate


class OrderService:
    def __init__(self, crm: RetailCRMClient):
        self.crm = crm

    async def list_orders(
        self, filters: dict[str, Any], page: int, limit: int
    ) -> dict[str, Any]:
        return await self.crm.list_orders(filters, page, limit)

    async def create_order(self, data: OrderCreate) -> dict[str, Any]:
        return await self.crm.create_order(data.model_dump(mode="json"))
