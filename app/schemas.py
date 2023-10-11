from pydantic import BaseModel, Field, EmailStr
from typing import List
from uuid import UUID


class BankSchema(BaseModel):
    id: UUID
    bank_name: str
    kor_score: str
    swift: str
    iban: str
    user_id: UUID


class UserSchema(BaseModel):
    id: UUID
    username: str
    email: EmailStr = Field(examples=["marcelo@mail.com"])
    password: str
    banks: List[BankSchema]
