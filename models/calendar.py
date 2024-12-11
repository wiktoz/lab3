from extensions import db
from uuid import uuid4
from enum import Enum
from sqlalchemy.orm import validates

class DayTypes(Enum):
    workday = "workday"
    weekend = "weekend"

class Calendar(db.Model):
    __tablename__ = "calendars"
    calendar_id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid4()))
    teacher_id = db.Column(db.String(36), db.ForeignKey('teachers.teacher_id'), nullable=False)
    available_from = db.Column(db.Time, nullable=False)
    available_to = db.Column(db.Time, nullable=False)
    day_type = db.Column(db.String(30), nullable=False)

    @validates("day_type")
    def validate_day_type(self, _, value):
        day_values = list(DayTypes)
        day_names = [subject.value for subject in day_values]

        if isinstance(value, DayTypes):
            value = value.value 

        if value not in day_names:
            raise ValueError("Day type is not valid")
        return value  