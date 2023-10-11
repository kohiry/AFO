from schemas import UserSchema
from services import UserCRUD
import uuid

UserCRUD.create(
    UserSchema(
        id=uuid.uuid4(),
        email="hi@mail.ru",
        username="hello",
        password="123",
        banks=[],
    )
)
