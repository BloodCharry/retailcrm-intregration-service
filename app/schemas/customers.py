from datetime import datetime

from pydantic import BaseModel, EmailStr


class CustomerCreate(BaseModel):
    firstName: str
    email: EmailStr
    phone: str | None = None


class Customer(BaseModel):
    id: int
    firstName: str | None
    lastName: str | None
    email: EmailStr | None
    createdAt: datetime
