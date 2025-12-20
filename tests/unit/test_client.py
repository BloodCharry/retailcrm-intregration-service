import pytest
import httpx
from app.crm.client import RetailCRMClient


@pytest.mark.asyncio
async def test_client_requires_api_key():
    with pytest.raises(ValueError):
        RetailCRMClient(base_url="https://example.com/api/v5", api_key=None)


@pytest.mark.asyncio
async def test_list_customers_adds_api_key(monkeypatch):
    client = RetailCRMClient("https://example.com/api/v5", "testkey")

    async def fake_request(method, url, params=None, json=None):
        return httpx.Response(200, json={"ok": True, "params": params})

    monkeypatch.setattr(client._client, "request", fake_request)

    result = await client.list_customers(filters={"email": "test@example.com"})
    assert result["ok"] is True
    assert result["params"]["apiKey"] == "testkey"
