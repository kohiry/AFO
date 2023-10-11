from pydantic import BaseModel, Field, EmailStr
from typing import List
from uuid import UUID


class LoginSchema(BaseModel):
    username: str
    password: str


class RegisterSchema(BaseModel):
    username: str
    email: EmailStr = Field(examples=["marcelo@mail.com"])
    password: str


class BankSchema(BaseModel):
    id: UUID
    bank_name: str
    bik: str
    kor_score: str
    swift: str
    iban: str
    user_id: UUID
    is_active: bool = False


class UserSchema(BaseModel):
    id: UUID
    username: str
    email: EmailStr = Field(examples=["marcelo@mail.com"])
    password: str
    banks: List[BankSchema]
