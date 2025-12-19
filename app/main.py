from fastapi import Depends, FastAPI

from app.core.logging import logger, setup_logging
from app.core.middleware import LoggingMiddleware
from app.core.request_id import RequestIDMiddleware
from app.core.security import get_api_key

setup_logging()

app = FastAPI(
    title="RetailCRM Integration Service",
    version="0.1.0",
)

# Middleware
app.add_middleware(RequestIDMiddleware)
app.add_middleware(LoggingMiddleware)


@app.get("/health", dependencies=[Depends(get_api_key)])
async def health_check() -> dict[str, str]:
    logger.info("health_check_called", request_id="test")
    return {"status": "ok"}
