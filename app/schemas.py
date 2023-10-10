from pydentic import BaseModel, Field, EmailStr
from uuid import UUID


class UserSchema(BaseModel):
    id: UUID
    username: str
    email: EmailStr = Field(examples=["marcelo@mail.com"])
    password: str
