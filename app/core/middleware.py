import time
from collections.abc import Awaitable, Callable

from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware

from app.core.logging import logger
from app.core.request_id import get_request_id


class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(
        self, request: Request, call_next: Callable[[Request], Awaitable[Response]]
    ) -> Response:
        start_time = time.time()
        client_host = request.client.host if request.client else "unknown"

        logger.info(
            "request_started",
            method=request.method,
            path=request.url.path,
            query=str(request.url.query),
            client=client_host,
            request_id=get_request_id(),
        )

        response = await call_next(request)

        duration = (time.time() - start_time) * 1000
        logger.info(
            "request_finished",
            method=request.method,
            path=request.url.path,
            status_code=response.status_code,
            duration_ms=round(duration, 2),
            request_id=get_request_id(),
        )
        return response
