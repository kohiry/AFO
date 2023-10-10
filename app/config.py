"""Конфиг для хранения важныx переменных."""


class DBConfig:
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
        return DBConfig.POSTGRES_DB

    @staticmethod
    def get_db_username() -> str:
        """Возвращает имя пользователя базы данных."""
        return DBConfig.POSTGRES_USERNAME

    @staticmethod
    def get_db_pswd() -> str:
        """Возвращает пaроль к базе данных."""
        return DBConfig.POSTGRES_PASSWORD

    @staticmethod
    def get_db_data() -> dict:
        """Возвращает все данные о базе данных в виде словаря."""
        data = {
            "pass": DBConfig.get_db_pswd(),
            "name": DBConfig.get_db_username(),
            "db": DBConfig.get_db_name(),
            "host": DBConfig.POSTGRES_HOST,
            "port": DBConfig.POSTGRES_PORT,
        }
        return data

    @staticmethod
    def get_db_url() -> str:
        conf = DBConfig.get_db_data()
        return f"postgresql://{conf['name']}:{conf['pass']}@{conf['host']}/{conf['db']}"
