from datetime import datetime

from pydantic import BaseModel, EmailStr, Field


class PaginationParams(BaseModel):
    page: int = Field(1, ge=1)
    limit: int = Field(20, ge=1, le=100)


class CustomerFilter(BaseModel):
    name: str | None = None
    email: EmailStr | None = None
    registered_from: datetime | None = None
    registered_to: datetime | None = None
