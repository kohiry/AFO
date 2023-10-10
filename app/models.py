from main import db
from flask_login import UserMixin
from services import CastUserAndUserSchema as castU
from schemas import UserSchema
from sqlalchemy.dialects.postgresql import UUID
import uuid


class User(db.Model, UserMixin):
    __table__ = "users"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    books = db.relationship("BankReq", backref="bank_req", lazy=True)

    def check_user(self, user_id: str) -> UserSchema:
        return castU(self.query.get(user_id)).db_to_schema()


class BankReq(db.Model):
    __tablename__ = "banks_req"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    bik = db.Column(db.Integer())
    bank_name = db.Column(db.String(50), unique=True, nullable=False)
    kor_score = db.Column(db.String(20), nullable=False)
    swift = db.Column(db.String(11), nullable=False)
    iban = db.Column(db.String(34), nullable=True)
    user_id = db.Column(UUID, db.ForeignKey("authors.id"), nullable=False)
