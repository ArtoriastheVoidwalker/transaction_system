from typing import Any

from fastapi import APIRouter, Depends, HTTPException, File, UploadFile
from sqlalchemy.orm import Session
from datetime import datetime as dt

from app import crud, models, schemas
from app.api import deps
# from app.core.celery_app import celery_app

router = APIRouter()


@router.post("/registartion", response_model=schemas.User)
async def registartion(
    *,
    db: Session = Depends(deps.get_db),
    user_data: schemas.UserCreate
) -> Any:

    if crud.user.uniqueness_check(db=db, phone=user_data.phone) is True:
        user = crud.user.create(db, user_data)
        crud.balance.create(db=db, user_id=user.id, obj_in=schemas.BalanceCreate(
            amount=0.0, currency='usd', rebalancing_at=dt.now()))

        return user
