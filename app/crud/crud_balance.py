from datetime import datetime as dt
from typing import Any, Union, Dict, Optional
from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models import Balance
from app.schemas import BalanceCreate, BalanceUpdate


class CRUDBalance(CRUDBase[Balance, BalanceCreate, BalanceUpdate]):

    def get_by_user_id(self, db: Session, *, user_id: str) -> Any:
        return db.query(Balance).filter(Balance.user_id == user_id).all()

    def get_by_users_balance(self, db: Session, *, user_id: str, balance_id: str) -> Optional[Balance]:
        return db.query(Balance).filter(Balance.user_id == user_id, Balance.id == balance_id).first()

    def check_balance(self, db: Session, *, currency: str) -> Optional[Balance]:
        return db.query(Balance).filter(Balance.currency == currency).first()

    def create(self, db: Session, user_id: int, obj_in: BalanceCreate) -> Balance:
        db_obj = Balance(
            rebalancing_at=dt.now(),
            user_id=user_id,
            currency=obj_in.currency,
            amount=obj_in.amount
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(self, db: Session, *, balance_id: int,
               obj_in: Union[BalanceUpdate, Dict[str, Any]]) -> Balance:
        db_obj = self.get(db, id=balance_id)

        if db_obj is None:
            return False

        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)

        return super().update(db, db_obj=db_obj, obj_in=update_data)


balance = CRUDBalance(Balance)
