from extensions import db
from uuid import uuid4
from enum import Enum
from sqlalchemy.orm import validates

class Subjects(Enum):
    maths = "matematyka"
    physics = "fizyka"
    chemistry = "chemia"
    history = "historia"
    wos = "WoS"
    biology = "biologia"
    geography = "geografia"

class Subject(db.Model):
    __tablename__ = "subjects"
    subject_id = db.Column(db.String(36), primary_key=True, default=uuid4)
    name = db.Column(db.String(60), nullable=False)

    @validates("name")
    def validate_name(self, _, value):
        if value not in Subjects._value2member_map_:
            raise ValueError("Subject is not valid")