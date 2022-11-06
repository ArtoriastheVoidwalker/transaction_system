from pydantic import BaseModel
from typing import Optional

from .user import (
    User, Users, UserCreate, UserUpdate,
)

from .balance import (
    Balance, BalanceBase, BalanceCreate, BalanceUpdate, BalanceInDBBase
)


class DefaultResponseSchema(BaseModel):

    status_code: Optional[int] = 200
    success: Optional[bool] = True
