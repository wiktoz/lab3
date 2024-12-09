from extensions import db
from uuid import uuid4

class Student(db.Model):
    __tablename__ = "teachers"
    student_id = db.Column(db.String(36), primary_key=True, default=uuid4)
    name = db.Column(db.String(60), nullable=False)
    surname = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(120), unique=True)