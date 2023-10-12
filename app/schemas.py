from pydantic import BaseModel, Field, EmailStr
from typing import List
from uuid import UUID


class LoginSchema(BaseModel):
    username: str
    password: str


class RegisterSchema(BaseModel):
    username: str
    password: str


class BankSchema(BaseModel):
    id: UUID = None
    bank_name: str
    bik: str
    kor_score: str
    swift: str
    iban: str = None
    user_id: UUID
    is_active: bool = False


class UserSchema(BaseModel):
    id: UUID
    username: str
    password: str
