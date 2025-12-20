import pytest
from app.api.v1.deps import get_crm_client
from app.core.config import settings
from tests.integration.test_customers import test_create_customer_real


@pytest.mark.asyncio
async def test_list_orders_real():
    client = get_crm_client()
    result = await client.list_orders(filters={"createdAtFrom": "2024-01-01", "createdAtTo": "2024-12-31"})
    assert "orders" in result


@pytest.mark.asyncio
async def test_create_order_real():
    client = get_crm_client()
    customer_id = await test_create_customer_real()

    new_order = {
        "number": "TEST-ORDER-001",
        "customer": {"id": customer_id},
        "items": [{"offer": {"id": settings.test_offer_id}, "quantity": 1}],
    }
    result = await client.create_order(new_order)
    assert result.get("success") is True
    assert "id" in result
    return result["id"]
