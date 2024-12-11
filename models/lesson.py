from extensions import db
from uuid import uuid4

class Lesson(db.Model):
    lesson_id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid4()))
    student_id = db.Column(db.String(36), db.ForeignKey('students.student_id'), nullable=False)
    teacher_id = db.Column(db.String(36), db.ForeignKey('teachers.teacher_id'), nullable=False)
    subject_id = db.Column(db.String(36), db.ForeignKey('subjects.subject_id'), nullable=False)
    datetime = db.Column(db.DateTime, nullable=False)