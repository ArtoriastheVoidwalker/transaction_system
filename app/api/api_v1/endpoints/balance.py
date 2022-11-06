import uuid
from datetime import datetime as dt
from fastapi import HTTPException
from typing import Any
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.celery_app import update_balance
from app import crud, schemas, models
from app.api import deps


router = APIRouter()


@router.get("/{user_id}")
async def get_balance(
    user_id: int,
    db: Session = Depends(deps.get_db),
) -> Any:

    balance = crud.balance.get_by_user_id(db, user_id=user_id)

    if balance is not None:
        return balance
    else:
        raise HTTPException(status_code=404, detail='User is not found')


@router.post("/create_balance/{user_id}")
async def create_balance(
    *,
    user_id: int,
    db: Session = Depends(deps.get_db),
    balance_data: schemas.BalanceCreate
) -> Any:

    if crud.balance.check_balance(db=db, currency=balance_data.currency) is None:
        return crud.balance.create(db=db, user_id=user_id, obj_in=balance_data)
    else:
        raise HTTPException(status_code=403, detail=f"Balance with this currency is already active")


@router.patch("/replenish_balance/{balance_id}/{amount}")
async def replenish_balance(
    balance_id: int,
    amount: float,
    db: Session = Depends(deps.get_db),
) -> Any:

    balance = crud.balance.get(db, id=balance_id)

    if balance is not None:
        new_amount = balance.amount + amount

        update_balance.apply_async(args=[new_amount, balance.id])
        raise HTTPException(status_code=200, detail=f"Balance updated successfully")

    else:
        raise HTTPException(status_code=404, detail='Balance is not found')


@router.patch("/remove_from_balance/{user_id}/{balance_id}/{amount}")
async def remove_from_balance(
    user_id: int,
    balance_id: int,
    amount: float,
    db: Session = Depends(deps.get_db),
) -> Any:
    balance = crud.balance.get_by_users_balance(db, user_id=user_id, balance_id=balance_id)
    if balance is not None:
        if balance.amount - amount >= 0:
            new_amount = balance.amount - amount

            update_balance.apply_async(args=[new_amount, balance.id])
            raise HTTPException(status_code=200, detail=f"Balance updated successfully")

        else:
            raise HTTPException(status_code=403, detail='There are not enough funds on the balance to write off')
    else:
        raise HTTPException(status_code=404, detail='Balance is not found')
