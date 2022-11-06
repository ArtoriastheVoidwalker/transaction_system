from typing import Generator, Union, Optional, Any

from fastapi.security import OAuth2PasswordBearer


from app.core.config import settings
from app.db.session import SessionLocal


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
