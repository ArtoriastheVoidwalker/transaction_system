from sqlalchemy.orm import Session
from random import randint

from app import crud, schemas
from app.core.config import settings


def init_db(db: Session) -> None:

    user = crud.user.get_by_phone(db, phone=settings.FIRST_SUPERUSER)

    if not user:
        user_in = schemas.UserCreate(
            phone=settings.FIRST_SUPERUSER,
            password=settings.FIRST_SUPERUSER_PASSWORD,
            full_name=settings.FIRST_SUPERUSER_FULL_NAME,
            sex=settings.FIRST_SUPERUSER_SEX,
            inn=str(randint(1000000, 9999999)),
            passport=str(randint(1000000, 9999999)),
            birth_date='2000-09-11',
            source='current',
            is_active=True
        )
        user = crud.user.create(db, obj_in=user_in)

    # user = crud.user.get_by_phone(db, phone=settings.TEST_USER)

    # if not user:
    #     user_in = schemas.UserCreate(
    #         phone=settings.TEST_USER,
    #         password=settings.TEST_USER_PASSWORD,
    #         full_name=settings.TEST_USER_FULL_NAME,
    #         sex=settings.TEST_USER_SEX,
    #         birth_date='2000-09-11',
    #         source='current',
    #         is_active=True
    #     )
    #     user = crud.user.create(db, obj_in=user_in)

    # user = crud.user.get_by_phone(db, phone=settings.TEST_VALIDATE)

    # if not user:
    #     user_in = schemas.UserCreate(
    #         phone=settings.TEST_VALIDATE,
    #         password=settings.TEST_VALIDATE_PASSWORD,
    #         full_name=settings.TEST_VALIDATE_FULL_NAME,
    #         is_signed=settings.TEST_VALIDATE_IS_SIGNED,
    #         sex=settings.TEST_VALIDATE_SEX,
    #         birth_date='2000-09-11',
    #         source='current',
    #         is_active=True
    #     )
    #     user = crud.user.create(db, obj_in=user_in)

    # user = crud.user.get_by_phone(db, phone=settings.LOGIN_USER)

    # if not user:
    #     user_in = schemas.UserCreate(
    #         phone=settings.LOGIN_USER,
    #         password=settings.LOGIN_USER_PASSWORD,
    #         full_name=settings.LOGIN_USER_FULL_NAME,
    #         sex=settings.LOGIN_USER_SEX,
    #         birth_date='2000-09-11',
    #         source='current',
    #         is_active=True
    #     )
    #     user = crud.user.create(db, obj_in=user_in)
