"""Конфиг для хранения важныx переменных."""
import os


class DBConfig:
    """Класс конфига базы данных.
    Здесь хранятся переменные postgresql
    """

    POSTGRES_DB = "users"
    POSTGRES_USERNAME = "root2"
    POSTGRES_PASSWORD = "root3"
    POSTGRES_HOST = "localhost"
    POSTGRES_PORT = "5432"

    @staticmethod
    def get_db_data() -> dict:
        """Возвращает все данные о базе данных в виде словаря."""
        data = {
            "pass": DBConfig.POSTGRES_PASSWORD,
            "name": DBConfig.POSTGRES_USERNAME,
            "db": DBConfig.POSTGRES_DB,
            "host": DBConfig.POSTGRES_HOST,
            "port": DBConfig.POSTGRES_PORT,
        }
        return data

    @staticmethod
    def get_db_url() -> str:
        """Возвращает ссылку на postgresql."""
        conf = DBConfig.get_db_data()
        return f"postgresql+psycopg2://{conf['name']}:{conf['pass']}@{conf['host']}:{conf['port']}/{conf['db']}"
