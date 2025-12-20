from typing import Annotated
from fastapi import Depends
from app.crm.client import RetailCRMClient
from app.core.config import settings


def get_crm_client() -> RetailCRMClient:
    return RetailCRMClient(
        base_url=settings.retailcrm_base_url,
        api_key=settings.retailcrm_api_key,
        site=settings.retailcrm_site,
        timeout=settings.http_timeout,
    )


CRMClientDep = Annotated[RetailCRMClient, Depends(get_crm_client)]