from typing import Any, Dict, Optional, Union, List
from sqlalchemy.orm import Session
from fastapi import HTTPException
from datetime import datetime as dt

from app.crud.base import CRUDBase
from app.models import User, Balance
from app.schemas import UserCreate, UserUpdate


class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):

    def uniqueness_check(self, db: Session, *, phone: str):
        if db.query(User).filter(User.phone == phone).first() is None:
            return True
        else:
            raise HTTPException(status_code=403, detail='Phone is already exist')

    def create(self, db: Session, obj_in: UserCreate) -> User:

        db_user = User(
            phone=obj_in.phone,
            password=obj_in.password,
            full_name=obj_in.full_name,
            birth_date=obj_in.birth_date,
            created_at=dt.now()
        )

        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user


user = CRUDUser(User)
