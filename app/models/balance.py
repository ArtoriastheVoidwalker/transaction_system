from sqlalchemy import Column, Integer, ForeignKey, DateTime, Float, String
from sqlalchemy.orm import relationship
from app.db.base_class import Base
from datetime import datetime as dt

from app.models import User


class Balance(Base):

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float, nullable=False)
    currency = Column(String, nullable=False)
    rebalancing_at = Column(DateTime, nullable=True, default=dt.now)

    # last_transaction_id = Column(Integer, ForeignKey("transaction.id", ondelete='CASCADE'), nullable=True, index=True)
    # last_transaction = relationship("Transaction", back_populates="balances", primaryjoin=last_transaction_id == Transaction.id)

    user_id = Column(Integer, ForeignKey("user.id", ondelete='CASCADE'), nullable=True, index=True)
    user = relationship("User", back_populates="balances")

    # transactions = relationship(
    #     "Transaction",
    #     back_populates="balance",
    #     cascade="all, delete",
    #     passive_deletes=True
    # )
