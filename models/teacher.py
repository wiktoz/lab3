from extensions import db
from uuid import uuid4
from sqlalchemy.orm import validates

class Teacher(db.Model):
    __tablename__ = "teachers"
    teacher_id = db.Column(db.String(36), primary_key=True, default=uuid4)
    name = db.Column(db.String(60), nullable=False)
    surname = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(120), unique=True)
    description = db.Column(db.String(300))
    subjects = db.relationship("Subject")
    rate = db.Column(db.Float)
    phone = db.Column(db.String(15))
    price = db.Column(db.Integer)
    currency = db.Column(db.String(3))

    @validates("rate")
    def validate_rate(self, _, value):
        if value < 0.0 or value > 5.0:
            raise ValueError("Rate is not in range <0,5>")
        return value