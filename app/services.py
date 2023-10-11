from models import User, BankReq
from typing import List
from schemas import UserSchema, BankSchema


class UserManager:
    """Класс для взаимодействия с пользователем."""

    @staticmethod
    def get_by_id(user_id: str) -> UserSchema:
        """Метод получения схемы юзера по его id."""
        return CastUserAndUserSchema(User.query.get(user_id)).db_to_schema()

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

    @staticmethod
    def get_banks(user_id: str) -> List[BankSchema]:
        banks_schema = []
        for bank in User.get_banks(user_id):
            banks_schema.append(UserManager.cast_bank_to_schema(bank))
        return banks_schema

    @staticmethod
    def set_active_bank(bank_id: str, user_id: str):
        User.set_active_bank(bank_id, user_id)


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
