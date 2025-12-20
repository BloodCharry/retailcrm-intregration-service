import pytest
from app.api.v1.deps import get_crm_client
from tests.integration.test_orders import test_create_order_real


@pytest.mark.asyncio
async def test_create_payment_real():
    client = get_crm_client()
    order_id = await test_create_order_real()

    new_payment = {
        "order": {"id": order_id},
        "amount": 100.0,
        "type": "cash",
        "comment": "Test payment",
    }
    result = await client.create_payment(new_payment)
    assert result.get("success") is True
    assert "id" in result
