from models import User
from schemas import UserSchema


class CastUserAndUserSchema:
    def __init__(self, user: User):
        self._user = user

    def db_to_schema(self):
        user_schema = UserSchema()
        user_schema.email = self._user.email
        user_schema.id = self._user.id
        user_schema.password = self._user.password
        user_schema.username = self._user.username
        return user_schema
