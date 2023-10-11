"""В этом файле хранятся основные переменные приложения."""

from flask import Flask
from config import DBConfig, Config
from flask_wtf.csrf import CSRFProtect
from flask_bcrypt import Bcrypt


app = Flask(__name__)
app.config["SECRET_KEY"] = Config.get_secret()
app.config["SQLALCHEMY_DATABASE_URI"] = DBConfig.get_db_url()
csrf = CSRFProtect(app)
bcrypt = Bcrypt(app)

# app.config["SECRET_KEY"] = Config.get_secret_key()
# BankReq.Base.metadata.create_all(bind=engine)
