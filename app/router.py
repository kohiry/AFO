from main import app
from flask import Flask, render_template
from flask_login import login_user, current_user, logout_user, login_required
from services import UserManager
from flask_login import LoginManager


@app.route("/")
@app.route("/index")
def hello_world():
    return render_template("index.html")


login_manager = LoginManager(app)
login_manager.login_view = "login"
login_manager.login_message_category = "info"


@login_manager.user_loader
def load_user(user_id):
    return UserManager.get_by_id(user_id)


if __name__ == "__main__":
    app.run(debug=True)
