from models import User
from schemas import UserSchema


class UserManager:
    """Класс для взаимодействия с пользователем."""

    def get_by_id(user_id: str) -> UserSchema:
        """Метод получения схемы юзера по его id."""
        return User.check_user(user_id)


class CastUserAndUserSchema:
    """Преобразование типов Схемы юзера и Модели юзера в друг друга."""

    def __init__(self, user: User):
        self._user = user

    def db_to_schema(self) -> UserSchema:
        """Преобразование модели в схему."""
        user_schema = UserSchema(
            email=self._user.email,
            id=self._user.id,
            password=self._user.password,
            username=self._user.username,
        )
        return user_schema
