from models import User, BankReq
from schemas import UserSchema, BankSchema


class UserManager:
    """Класс для взаимодействия с пользователем."""

    @staticmethod
    def get_by_id(user_id: str) -> UserSchema:
        """Метод получения схемы юзера по его id."""
        return CastUserAndUserSchema(User.query.get(user_id)).db_to_schema()


class BankCRUD:
    @staticmethod
    def create(req: BankSchema):
        BankReq.new(req)

    @staticmethod
    def delete(id: str):
        BankReq.delete(id)

    @staticmethod
    def update(req: BankSchema):
        BankReq.update(req)


class UserCRUD:
    @staticmethod
    def create(us: UserSchema):
        User.new(us)

    def delete(id: str):
        User.delete(id)


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
