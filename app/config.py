"""Конфиг для хранения важныx переменных."""


class Config:
    """Класс конфиг.
    Здесь хранятся переменные postgresql
    """

    POSTGRES_DB = "users"
    POSTGRES_USERNAME = "root2"
    POSTGRES_PASSWORD = "root3"
    POSTGRES_HOST = "localhost"
    POSTGRES_PORT = "5432"

    @staticmethod
    def get_db_name() -> str:
        """Возвращает название базы данных."""
        return Config.POSTGRES_DB

    @staticmethod
    def get_db_username() -> str:
        """Возвращает имя пользователя базы данных."""
        return Config.POSTGRES_USERNAME

    @staticmethod
    def get_db_pswd() -> str:
        """Возвращает пaроль к базе данных."""
        return Config.POSTGRES_PASSWORD

    @staticmethod
    def get_db_data() -> dict:
        """Возвращает все данные о базе данных в виде словаря."""
        data = {
            "pass": Config.get_db_pswd(),
            "name": Config.get_db_username(),
            "db": Config.get_db_name(),
            "host": Config.POSTGRES_HOST,
            "port": Config.POSTGRES_PORT,
        }
        return data
