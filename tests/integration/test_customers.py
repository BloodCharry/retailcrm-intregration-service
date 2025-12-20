import pytest
from app.api.v1.deps import get_crm_client


@pytest.mark.asyncio
async def test_list_customers_real():
    client = get_crm_client()
    result = await client.list_customers(filters={"email": "testuser@example.com"})
    assert "customers" in result


@pytest.mark.asyncio
async def test_create_customer_real():
    client = get_crm_client()
    new_customer = {
        "firstName": "Test",
        "lastName": "User",
        "email": "testuser@example.com",
        "phones": [{"number": "+123456789"}],
    }
    result = await client.create_customer(new_customer)
    assert result.get("success") is True
    assert "id" in result
    return result["id"]
