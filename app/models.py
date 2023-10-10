from main import db
from flask_login import UserMixin
from services import CastUserAndUserSchema as castU
from schemas import UserSchema


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def check_user(self, user_id: str) -> UserSchema:
        return castU(self.query.get(int(user_id))).db_to_schema()
