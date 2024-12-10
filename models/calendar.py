from extensions import db
from uuid import uuid4

class Calendar(db.Model):
    __tablename__ = "calendars"
    calendar_id = db.Column(db.String(36), primary_key=True, default=uuid4)
    teacher_id = db.Column(db.String(36), db.ForeignKey('teachers.teacher_id'), nullable=False)
    available_from = db.Column(db.Time, nullable=False)
    available_to = db.Column(db.Time, nullable=False)
    
    