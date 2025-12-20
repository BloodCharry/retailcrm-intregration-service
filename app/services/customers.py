from typing import Any

from app.crm.client import RetailCRMClient
from app.schemas.customers import CustomerCreate


class CustomerService:
    def __init__(self, crm: RetailCRMClient):
        self.crm = crm

    async def list_customers(
        self, filters: dict[str, Any], page: int, limit: int
    ) -> dict[str, Any]:
        """Получение списка клиентов с фильтрацией."""
        return await self.crm.list_customers(filters, page, limit)

    async def create_customer(self, data: CustomerCreate) -> dict[str, Any]:
        """Создание нового клиента."""
        return await self.crm.create_customer(data.model_dump(mode="json"))
