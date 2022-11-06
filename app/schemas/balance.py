from datetime import datetime as dt

from typing import Optional, List
from pydantic import BaseModel


# Shared properties
class BalanceBase(BaseModel):
    amount: float = 0.0
    currency: str = 'usd'
    rebalancing_at: dt


# Properties to receive via API on creation
class BalanceCreate(BaseModel):
    amount: float = 0.0
    currency: str = 'usd'
    rebalancing_at: dt


class BalanceUpdate(BaseModel):
    amount: float = None
    rebalancing_at: dt


class BalanceInDBBase(BalanceBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


class Balance(BalanceInDBBase):
    pass
    # payment_code: str = None

