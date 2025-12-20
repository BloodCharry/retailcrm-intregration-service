from decimal import Decimal

from pydantic import BaseModel


class PaymentCreate(BaseModel):
    order_id: int
    amount: Decimal
    type: str


class Payment(BaseModel):
    id: int
    order_id: int
    amount: Decimal
    type: str
