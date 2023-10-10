from main import app, login_manager
from flask_login import login_user, current_user, logout_user, login_required
from models import User


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route("/")
@app.route("/index")
def hello_world():
    return "aboba"
