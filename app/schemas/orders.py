from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel


class OrderItem(BaseModel):
    offer_id: int
    quantity: int
    price: Decimal


class OrderCreate(BaseModel):
    number: str
    customer_id: int | None = None
    items: list[OrderItem]


class Order(BaseModel):
    id: int
    number: str
    customer_id: int | None
    createdAt: datetime
