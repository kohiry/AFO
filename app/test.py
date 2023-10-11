import pytest
from schemas import UserSchema
from services import UserCRUD
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


if __name__ == "__main__":
    pytest.main([__file__])
