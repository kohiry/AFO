import pytest
from schemas import UserSchema, BankSchema, LoginSchema
from services import UserCRUD, BankCRUD, UserManager, UserCheck
from models import BankReq
import uuid


def test_user_login_bad():
    user_id = uuid.uuid4()
    user_data = UserSchema(
        id=user_id,
        username="hello",
        password="123",
    )
    user2_data = LoginSchema(
        username="hello",
        password="123",
    )
    user3_data = LoginSchema(
        username="hello",
        password="1234",
    )
    user4_data = LoginSchema(
        username="helloo",
        password="123",
    )
    try:
        UserCRUD.create(user_data)
        assert UserCheck.check(user2_data) is True
        assert UserCheck.check(user3_data) is False
        assert UserCheck.check(user4_data) is False

    except Exception as e:
        pytest.fail(f"Bad request: {e}")

    UserCRUD.delete(user_data.id)


def test_active_bank():
    # Генерируем уникальный UUID для пользователя
    user_id = uuid.uuid4()

    # Создаем объект UserSchema
    user_data = UserSchema(
        id=user_id,
        username="hello",
        password="123",
    )

    req = BankSchema(
        id=uuid.uuid4(),
        bank_name="много денег банк(с)",
        bik=1,
        kor_score="2",
        swift="3",
        iban="4",
        user_id=user_data.id,
    )
    req2 = BankSchema(
        id=uuid.uuid4(),
        bank_name="мало денег банк(с)",
        bik=1,
        kor_score="2",
        swift="3",
        iban="4",
        user_id=user_data.id,
    )

    # Вызываем функцию создания пользователя и проверяем, что она не вызывает исключений
    try:
        UserCRUD.create(user_data)
        BankCRUD.create(req)
        BankCRUD.create(req2)

        UserManager.set_active_bank(req.id, user_data.id)
        active_bank = BankReq.query.filter_by(
            is_active=True, user_id=user_data.id
        ).first()
        assert active_bank is not None
        assert active_bank.id == req.id
        UserManager.set_active_bank(req2.id, user_data.id)
        active_bank = BankReq.query.filter_by(
            is_active=True, user_id=user_data.id
        ).first()
        assert active_bank is not None
        assert active_bank.id != req.id
        assert active_bank.id == req2.id

    except Exception as e:
        pytest.fail(f"Bad request: {e}")

    BankCRUD.delete(req.id)
    BankCRUD.delete(req2.id)
    UserCRUD.delete(user_data.id)


def test_user_creation():
    # Генерируем уникальный UUID для пользователя
    user_id = uuid.uuid4()

    # Создаем объект UserSchema
    user_data = UserSchema(
        id=user_id,
        username="hello",
        password="123",
    )

    # Вызываем функцию создания пользователя и проверяем, что она не вызывает исключений
    try:
        UserCRUD.create(user_data)
        UserCRUD.delete(user_data.id)
    except Exception as e:
        pytest.fail(f"User creation failed: {e}")


def test_bank_list():
    # Генерируем уникальный UUID для пользователя
    user_id = uuid.uuid4()

    # Создаем объект UserSchema
    user_data = UserSchema(
        id=user_id,
        username="hello",
        password="123",
    )

    req = BankSchema(
        id=uuid.uuid4(),
        bank_name="много денег банк(с)",
        bik=1,
        kor_score="2",
        swift="3",
        iban="4",
        user_id=user_data.id,
    )
    req2 = BankSchema(
        id=uuid.uuid4(),
        bank_name="мало денег банк(с)",
        bik=1,
        kor_score="2",
        swift="3",
        iban="4",
        user_id=user_data.id,
    )

    # Вызываем функцию создания пользователя и проверяем, что она не вызывает исключений
    try:
        UserCRUD.create(user_data)
        BankCRUD.create(req)
        BankCRUD.create(req2)
        bank_list = UserManager.get_banks(user_data.id)
        assert bank_list is not None and len(bank_list) == 2
        assert type(bank_list[0]) == BankSchema

    except Exception as e:
        pytest.fail(f"Bad request: {e}")

    BankCRUD.delete(req.id)
    BankCRUD.delete(req2.id)
    UserCRUD.delete(user_data.id)


def test_req_creation_and_upd():
    # Генерируем уникальный UUID для пользователя
    user_id = uuid.uuid4()

    # Создаем объект UserSchema
    user_data = UserSchema(
        id=user_id,
        username="hello",
        password="123",
    )

    # Создаем объект UserSchema
    req = BankSchema(
        id=uuid.uuid4(),
        bank_name="много денег банк(с)",
        bik=1,
        kor_score="2",
        swift="3",
        iban="4",
        user_id=user_data.id,
    )

    # Вызываем функцию создания пользователя и проверяем, что она не вызывает исключений
    try:
        UserCRUD.create(user_data)
        BankCRUD.create(req)
        req.bank_name = "мало денег банк(с)"
        BankCRUD.update(req)

    except Exception as e:
        pytest.fail(f"Bad request: {e}")

    BankCRUD.delete(req.id)
    UserCRUD.delete(user_data.id)


if __name__ == "__main__":
    pytest.main([__file__])
