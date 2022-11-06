from datetime import date

from typing import Optional, List

from pydantic import BaseModel


# Shared properties
class UserBase(BaseModel):
    phone: str
    full_name: str = None
    birth_date: date = None
    created_at: date


# Properties to receive via API on creation
class UserCreate(BaseModel):
    phone: str
    password: str
    full_name: str = None
    birth_date: date = None
    created_at: date


# Properties to receive via API on update
class UserUpdate(UserBase):
    phone: str
    full_name: str = None
    birth_date: date = None
    password: Optional[str] = None

    class Config:
        use_enum_values = True


class UserInDBBase(UserBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


class User(UserInDBBase):
    pass


# class ExtendedUser(UserInDBBase):
#     sms_code: Optional[str] = None


class Users(BaseModel):
    users: List[User] = None
    amount: Optional[int]
