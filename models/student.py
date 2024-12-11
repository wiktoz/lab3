from extensions import db
from uuid import uuid4

class Student(db.Model):
    __tablename__ = "students"
    student_id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid4()))
    name = db.Column(db.String(60), nullable=False)
    surname = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(120), unique=True)

    def __repr__(self):
        return (
            f"<Student(id={self.student_id}, name={self.name}, surname={self.surname}, email={self.email})>"
        )