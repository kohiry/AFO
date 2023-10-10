from flask import Flask, render_template
from config import DBConfig, Config
from flask_login import login_user, current_user, logout_user, login_required
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_bcrypt import Bcrypt


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = DBConfig.get_db_url()
app.config["SECRET_KEY"] = Config.get_secret_key()


bcrypt = Bcrypt(app)
db = SQLAlchemy(app)
csrf = CSRFProtect(app)
