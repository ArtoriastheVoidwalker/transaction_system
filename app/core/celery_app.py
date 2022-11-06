import logging
from datetime import datetime as dt

from celery import Celery

from app import crud, schemas
from app.core.logger import logger
from app.db.session import SessionLocal


celery_app = Celery("worker")
celery_app.config_from_object('app.core.celery_config')


@celery_app.task
def update_balance(new_amount, balance_id):

    db = SessionLocal()

    crud.balance.update(
        db,
        balance_id=balance_id,
        obj_in=schemas.BalanceUpdate(amount=new_amount,
                                     rebalancing_at=dt.now())
    )
    db.close()
    logger.success(f"Balance {balance_id} has been updated and is {new_amount}")

    return f"Balance {balance_id} has been updated and is {new_amount}"
