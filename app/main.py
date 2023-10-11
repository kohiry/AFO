"""В этом файле хранятся основные переменные приложения."""

from flask import Flask
from config import DBConfig

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = DBConfig.get_db_url()
# app.config["SECRET_KEY"] = Config.get_secret_key()
# BankReq.Base.metadata.create_all(bind=engine)
