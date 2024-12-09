from extensions import db
from uuid import uuid4
from enum import Enum

class Subjects(Enum):
    maths = "matematyka"
    physics = "fizyka"
    chemistry = "chemia"
    history = "historia"
    wos = "WoS"
    biology = "biologia"
    geography = "geografia"


class Teacher(db.Model):
    __tablename__ = "teachers"
    teacher_id = db.Column(db.String(36), primary_key=True, default=uuid4)
    name = db.Column(db.String(60), nullable=False)
    surname = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(120), unique=True)
    description = db.Column(db.String(300))
    subjects = db.Column(db.Enum(Subjects), nullable=False)
    rate = db.Column(db.Integer)
    phone = db.Column(db.String(15))
    price = db.Column(db.Integer)
    currency = db.Column(db.String(3))

