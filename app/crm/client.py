import json
from typing import Any
from urllib.parse import urljoin

import httpx

from app.core.logging import logger
from app.core.request_id import get_request_id


class RetailCRMClient:
    def __init__(
        self,
        base_url: str,
        api_key: str | None,
        site: str | None,
        timeout: float = 10.0,
    ):
        if not api_key:
            raise ValueError("RetailCRM API key is required")
        self.base_url = base_url.rstrip("/") + "/"
        self.api_key = api_key
        self.site = site
        self._client = httpx.AsyncClient(timeout=timeout)

    def _build_url(self, path: str) -> str:
        return urljoin(self.base_url, path)

    async def _request(
        self,
        method: str,
        path: str,
        *,
        params: dict[str, Any] | None = None,
        data: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        url = self._build_url(path)
        params = dict(params or {})
        if self.site:
            params.setdefault("site", self.site)

        headers = {"X-API-KEY": self.api_key}

        request_id = get_request_id()
        logger.info(
            "retailcrm_request",
            method=method,
            url=url,
            params=params,
            data=data,
            request_id=request_id,
        )

        try:
            resp = await self._client.request(
                method, url, params=params, data=data, headers=headers
            )
        except httpx.HTTPError as e:
            logger.error(
                "retailcrm_http_error", error=str(e), url=url, request_id=request_id
            )
            raise

        if resp.status_code >= 400:
            body = resp.text
            logger.error(
                "retailcrm_response_error",
                status_code=resp.status_code,
                body=body,
                url=url,
                request_id=request_id,
            )
            raise httpx.HTTPStatusError(
                f"RetailCRM responded with {resp.status_code}",
                request=resp.request,
                response=resp,
            )

        data = resp.json()
        logger.info(
            "retailcrm_response",
            status_code=resp.status_code,
            body=data,
            url=url,
            request_id=request_id,
        )
        return data

    async def list_customers(
        self, filters: dict[str, Any] | None = None, page: int = 1, limit: int = 20
    ) -> dict[str, Any]:
        params: dict[str, Any] = {"page": page, "limit": limit}
        if filters:
            params.update({f"filter[{k}]": v for k, v in filters.items()})
        return await self._request("GET", "customers", params=params)

    async def create_customer(self, customer: dict[str, Any]) -> dict[str, Any]:
        payload = {"customer": json.dumps(customer)}
        return await self._request("POST", "customers/create", data=payload)

    async def list_orders(
        self, filters: dict[str, Any] | None = None, page: int = 1, limit: int = 20
    ) -> dict[str, Any]:
        params: dict[str, Any] = {"page": page, "limit": limit}
        if filters:
            params.update({f"filter[{k}]": v for k, v in filters.items()})
        return await self._request("GET", "orders", params=params)

    async def create_order(self, order: dict[str, Any]) -> dict[str, Any]:
        payload = {"order": json.dumps(order)}
        return await self._request("POST", "orders/create", data=payload)

    async def create_payment(self, payment: dict[str, Any]) -> dict[str, Any]:
        payload = {"payment": json.dumps(payment, ensure_ascii=False)}
        logger.info("retailcrm_payload", payload=payload["payment"])
        return await self._request("POST", "orders/payments/create", data=payload)
