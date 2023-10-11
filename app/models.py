from sqlalchemy.dialects.postgresql import UUID
import uuid
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from schemas import UserSchema
from sqlalchemy.orm import sessionmaker
from main import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = Column(String(20), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(60), nullable=False)
    banks = relationship("BankReq", backref="user", lazy=True)

    @staticmethod
    def new(us: UserSchema):
        new_user = User(
            id=us.id, username=us.username, email=us.email, password=us.password
        )
        db.session.add(new_user)
        db.session.commit()

    def __repr__(self):
        return "<User %r>" % self.username


class BankReq(db.Model):
    __tablename__ = "banks_req"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    bik = Column(Integer())
    bank_name = Column(String(50), unique=True, nullable=False)
    kor_score = Column(String(20), nullable=False)
    swift = Column(String(11), nullable=False)
    iban = Column(String(34), nullable=True)
    user_id = Column(UUID, ForeignKey("users.id"), nullable=False)

    def __repr__(self):
        return f"<Bank Req {self.bank_name} user_id {self.user_id}>"
