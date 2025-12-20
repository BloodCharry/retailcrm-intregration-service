from app.api.v1.deps import get_crm_client
from app.crm.client import RetailCRMClient


def test_get_crm_client_returns_instance():
    client = get_crm_client()
    assert isinstance(client, RetailCRMClient)
    assert client.api_key is not None
