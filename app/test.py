import pytest
from schemas import UserSchema, BankSchema
from services import UserCRUD, BankCRUD
import uuid


def test_user_creation():
    # Генерируем уникальный UUID для пользователя
    user_id = uuid.uuid4()

    # Создаем объект UserSchema
    user_data = UserSchema(
        id=user_id,
        email="hi@mail.ru",
        username="hello",
        password="123",
        banks=[],
    )

    # Вызываем функцию создания пользователя и проверяем, что она не вызывает исключений
    try:
        UserCRUD.create(user_data)
        UserCRUD.delete(user_data.id)
    except Exception as e:
        pytest.fail(f"User creation failed: {e}")


def test_req_creation_and_upd():
    # Генерируем уникальный UUID для пользователя
    user_id = uuid.uuid4()

    # Создаем объект UserSchema
    user_data = UserSchema(
        id=user_id,
        email="hi@mail.ru",
        username="hello",
        password="123",
        banks=[],
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
