from main import app
from services import UserManager
from schemas import UserSchema
from typing import Optional


@app.route("/")
@app.route("/index")
def hello_world():
    return "aboba"
