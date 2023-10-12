from sqlalchemy.dialects.postgresql import UUID
import uuid
from sqlalchemy import Column, String, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from schemas import UserSchema, BankSchema
from main import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = Column(String(20), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String, nullable=False)
    banks = relationship(
        "BankReq", backref="user", foreign_keys="BankReq.user_id", lazy=True
    )

    @staticmethod
    def set_active_bank(bank_id: str, user_id: str):
        bank: BankReq = BankReq.query.filter_by(id=bank_id).first()
        if bank:
            old_bank = BankReq.query.filter_by(is_active=True, user_id=user_id).first()
            if old_bank:
                old_bank.is_active = False
            bank.is_active = True

            db.session.commit()

    @staticmethod
    def delete(id: str):
        user = User.query.filter_by(id=id).first()
        if user:
            db.session.delete(user)
            db.session.commit()

    @staticmethod
    def get_banks(id: str):
        return BankReq.query.filter_by(
            user_id=id
        ).all()  # по хорошему пару записей только, мало ли их очень много..

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
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    is_active = Column(Boolean, default=False)

    @staticmethod
    def new(req: BankSchema):
        new_req = BankReq(
            id=req.id,
            bik=req.bik,
            bank_name=req.bank_name,
            kor_score=req.kor_score,
            swift=req.swift,
            iban=req.iban,
            user_id=req.user_id,
        )
        db.session.add(new_req)
        db.session.commit()

    @staticmethod
    def delete(id: str):
        req = BankReq.query.filter_by(id=id).first()
        if req:
            db.session.delete(req)
            db.session.commit()

    @staticmethod
    def update(req: BankSchema):
        existing_req = BankReq.query.get(req.id)

        if existing_req:
            # Обновите атрибуты объекта на основе данных из BankSchema
            existing_req.bik = req.bik
            existing_req.bank_name = req.bank_name
            existing_req.kor_score = req.kor_score
            existing_req.swift = req.swift
            existing_req.iban = req.iban
            existing_req.user_id = req.user_id

            # Сохраните изменения в базе данных
            db.session.commit()

    def __repr__(self):
        return f"<Bank Req {self.bank_name} user_id {self.user_id}>"
