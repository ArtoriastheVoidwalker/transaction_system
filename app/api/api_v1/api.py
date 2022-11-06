from fastapi import APIRouter

from .endpoints import (
    user, balance
)


api_router = APIRouter()
api_router.include_router(balance.router, prefix="/balances", tags=["balances"])
api_router.include_router(user.router, prefix="/users", tags=["users"])

