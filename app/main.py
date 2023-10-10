"""В этом файле хранятся основные переменные приложения."""

from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from config import DBConfig, Config
from flask_wtf.csrf import CSRFProtect
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = DBConfig.get_db_url()
app.config["SECRET_KEY"] = Config.get_secret_key()

login_manager = LoginManager(app)
login_manager.login_view = "login"
login_manager.login_message_category = "info"

bcrypt = Bcrypt(app)
db = SQLAlchemy(app)
csrf = CSRFProtect(app)
csrf.init_app(app)
