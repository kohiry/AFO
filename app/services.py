from models import User, BankReq
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
from typing import List
from schemas import UserSchema, BankSchema, LoginSchema, RegisterSchema


class BankManager:
    @staticmethod
    def get_bank_by_id(id: str) -> BankSchema:
        return BankManager.cast_bank_to_schema(BankReq.query.filter_by(id=id).first())

    @staticmethod
    def cast_bank_to_schema(bank: BankReq) -> BankSchema:
        return BankSchema(
            id=bank.id,
            bik=bank.bik,
            bank_name=bank.bank_name,
            kor_score=bank.kor_score,
            swift=bank.swift,
            iban=bank.iban,
            user_id=bank.user_id,
            is_active=bank.is_active,
        )


class UserCheck:
    @staticmethod
    def check(usr: LoginSchema) -> bool:
        user = User.query.filter_by(username=usr.username).first()
        if user:
            return check_password_hash(user.password, usr.password)
        else:
            return False


class UserManager:
    """Класс для взаимодействия с пользователем."""

    @staticmethod
    def get_by_name(username: str) -> bool:
        """Метод получения схемы юзера по его username."""
        return User.query.filter_by(username=username).first() is not None

    @staticmethod
    def get_by_name_not_bool(username: str) -> UserSchema:
        """Метод получения схемы юзера по его username."""
        return CastUserAndUserSchema(
            User.query.filter_by(username=username).first()
        ).db_to_schema()

    @staticmethod
    def get_by_id(user_id: str) -> UserSchema:
        """Метод получения схемы юзера по его id."""
        return CastUserAndUserSchema(User.query.get(user_id)).db_to_schema()

    @staticmethod
    def get_banks(user_id: str) -> List[BankSchema]:
        banks_schema = []
        for bank in User.get_banks(user_id):
            banks_schema.append(BankManager.cast_bank_to_schema(bank))
        return banks_schema

    @staticmethod
    def set_active_bank(bank_id: str, user_id: str):
        User.set_active_bank(bank_id, user_id)


class BankCRUD:
    @staticmethod
    def create(req: BankSchema):
        req.id = uuid.uuid4()
        BankReq.new(req)

    @staticmethod
    def delete(id: str):
        BankReq.delete(id)

    @staticmethod
    def update(req: BankSchema):
        BankReq.update(req)


class UserCRUD:
    @staticmethod
    def register_to_user(reg: RegisterSchema):
        user = UserSchema(
            id=uuid.uuid4(),
            username=reg.username,
            password=reg.password,
        )
        UserCRUD.create(user)

    @staticmethod
    def create(us: UserSchema):
        us.password = generate_password_hash(us.password)
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
            id=self._user.id,
            password=self._user.password,
            username=self._user.username,
        )
        return user_schema
