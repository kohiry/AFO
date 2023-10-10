"""В этом файле хранятся основные переменные приложения."""

from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from config import DBConfig, Config

app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = DBConfig.get_db_url()
# app.config["SECRET_KEY"] = Config.get_secret_key()

# db = SQLAlchemy(app)
