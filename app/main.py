from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

from app.api.v1.routers import customers, orders, payments
from app.core.logging import logger, setup_logging
from app.core.middleware import LoggingMiddleware
from app.core.request_id import RequestIDMiddleware
from app.core.security import get_api_key

setup_logging()


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    yield


app = FastAPI(title="RetailCRM Integration Service", lifespan=lifespan)

# метрики
Instrumentator().instrument(app).expose(app)

# Middleware
app.add_middleware(RequestIDMiddleware)
app.add_middleware(LoggingMiddleware)

# Routers
app.include_router(customers.router, prefix="/api/v1", tags=["customers"])
app.include_router(orders.router, prefix="/api/v1", tags=["orders"])
app.include_router(payments.router, prefix="/api/v1", tags=["payments"])


@app.get("/health", dependencies=[Depends(get_api_key)])
async def health_check() -> dict[str, str]:
    logger.info("health_check_called", request_id="test")
    return {"status": "ok"}
