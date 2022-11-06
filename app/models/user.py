import enum
from datetime import datetime as dt

from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, Integer, String, DateTime, Date, Enum, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base
from app.core.config import settings

#
# if TYPE_CHECKING:
#     from .balance import Balance


class User(Base):

    id = Column(Integer, primary_key=True, index=True)
    phone = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    full_name = Column(String, nullable=False)
    birth_date = Column(Date, nullable=True)
    created_at = Column(DateTime, nullable=False, default=dt.now)

    balances = relationship(
        "Balance",
        back_populates="user",
        cascade="all, delete",
        passive_deletes=True
    )

    # transactions = relationship(
    #     "Transaction",
    #     back_populates="user",
    #     cascade="all, delete",
    #     passive_deletes=True
    # )



