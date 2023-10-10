from main import db
from flask_login import UserMixin
from services import CastUserAndUserSchema as castU
from schemas import UserSchema
from sqlalchemy.dialects.postgresql import UUID
import uuid


class User(db.Model, UserMixin):
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def check_user(self, user_id: str) -> UserSchema:
        return castU(self.query.get(user_id)).db_to_schema()
