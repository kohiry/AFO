from pydentic import BaseModel, Field, EmailStr


class UserSchema(BaseModel):
    id: str  # uuid
    username: str
    email: EmailStr = Field(examples=["marcelo@mail.com"])
    password: str
