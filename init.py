from extensions import db
from models.teacher import Teacher
from models.lesson import Lesson
from models.subject import Subject
from models.calendar import Calendar
from models.student import Student
from models.subject import Subjects
from models.calendar import DayTypes
from datetime import time, datetime

class DBManager:
    def init_db():
        subjects = [
            Subject(name=Subjects.biology.value),
            Subject(name=Subjects.chemistry.value),
            Subject(name=Subjects.geography.value),
            Subject(name=Subjects.history.value),
            Subject(name=Subjects.maths.value),
            Subject(name=Subjects.physics.value),
            Subject(name=Subjects.wos.value)
        ]

        db.session.add_all(subjects)
        db.session.commit()

        biology = Subject.query.filter_by(name=Subjects.biology.value).first()
        chemistry = Subject.query.filter_by(name=Subjects.chemistry.value).first()
        geography = Subject.query.filter_by(name=Subjects.geography.value).first()
        history = Subject.query.filter_by(name=Subjects.history.value).first()
        maths = Subject.query.filter_by(name=Subjects.maths.value).first()
        physics = Subject.query.filter_by(name=Subjects.physics.value).first()
        wos = Subject.query.filter_by(name=Subjects.wos.value).first()


        teachers = [
            Teacher(name="John", surname="Doe", email="john.doe@mit.edu", description="Physics professor", subjects=[physics, maths], rate=5.0, phone="+1 (339) 555-1234", price=100, currency="USD"),
            Teacher(name="Marie", surname="Boulot", email="marie.boulot@epfl.ch", description="Advanced chemistry engineer postgraduate", subjects=[maths,chemistry], rate=5.0, phone="+41 79 584 83 22", price=80, currency="CHF"),
            Teacher(name="Jacek", surname="Bąk", email="j.bak@uw.edu.pl", description="Philosophy and history teacher", subjects=[history, wos], rate=4.0, phone="+48 788 788 788", price=150, currency="PLN"),
            Teacher(name="Marcin", surname="Brzozowski", email="m.brzoz@wum.edu.pl", description="Doctor with experience", subjects=[chemistry, biology], rate=4.5, phone="+48 897 987 234", price=200, currency="PLN"),
            Teacher(name="Barbara", surname="Mak", email="barbara.mak@uw.edu.pl", description="Faculty of Geography at University of Warsaw", subjects=[maths,geography], rate=3.5, phone="+48 592 235 521", price=70, currency="PLN"),
        ]

        db.session.add_all(teachers)
        db.session.commit()

        students = [
            Student(name="Joe", surname="Rajewsky", email="joe.rajewsky@gmail.com"),
            Student(name="Mark", surname="Johnson", email="mark.johnson@gmail.com"),
            Student(name="John", surname="Wick", email="john.wick@gmail.com"),
        ]

        db.session.add_all(students)
        db.session.commit()

        teacher1 = Teacher.query.filter_by(email="john.doe@mit.edu").first()
        teacher2 = Teacher.query.filter_by(email="marie.boulot@epfl.ch").first()
        teacher3 = Teacher.query.filter_by(email="j.bak@uw.edu.pl").first()
        teacher4 = Teacher.query.filter_by(email="m.brzoz@wum.edu.pl").first()
        teacher5 = Teacher.query.filter_by(email="barbara.mak@uw.edu.pl").first()

        student1 = Student.query.filter_by(email="joe.rajewsky@gmail.com").first()
        student2 = Student.query.filter_by(email="mark.johnson@gmail.com").first()
        student3 = Student.query.filter_by(email="john.wick@gmail.com").first()


        calendars = [
            Calendar(teacher_id=teacher1.teacher_id, available_from=time(8,0), available_to=time(13,0), day_type=DayTypes.workday.value),
            Calendar(teacher_id=teacher1.teacher_id, available_from=time(10,0), available_to=time(13,0), day_type=DayTypes.weekend.value),
            Calendar(teacher_id=teacher2.teacher_id, available_from=time(10,0), available_to=time(18,0), day_type=DayTypes.workday.value),
            Calendar(teacher_id=teacher3.teacher_id, available_from=time(9,0), available_to=time(15,0), day_type=DayTypes.workday.value),
            Calendar(teacher_id=teacher4.teacher_id, available_from=time(12,0), available_to=time(20,0), day_type=DayTypes.workday.value),
            Calendar(teacher_id=teacher5.teacher_id, available_from=time(15,0), available_to=time(18,0), day_type=DayTypes.workday.value),
            Calendar(teacher_id=teacher5.teacher_id, available_from=time(9,0), available_to=time(20,0), day_type=DayTypes.weekend.value)
        ]

        db.session.add_all(calendars)
        db.session.commit()

        lessons = [
            ### Lessons for student1
            Lesson(student_id=student1.student_id, teacher_id=teacher1.teacher_id, subject_id=maths.subject_id, datetime=datetime(2024, 12, 11, 10, 0)),
            Lesson(student_id=student1.student_id, teacher_id=teacher2.teacher_id, subject_id=maths.subject_id, datetime=datetime(2024, 12, 11, 10, 0)),
            Lesson(student_id=student1.student_id, teacher_id=teacher3.teacher_id, subject_id=history.subject_id, datetime=datetime(2024, 12, 11, 10, 0)),
            Lesson(student_id=student1.student_id, teacher_id=teacher4.teacher_id, subject_id=biology.subject_id, datetime=datetime(2024, 12, 16, 10, 0)),
            Lesson(student_id=student1.student_id, teacher_id=teacher5.teacher_id, subject_id=geography.subject_id, datetime=datetime(2024, 12, 13, 10, 0)),

            ### Lessons for student2
            Lesson(student_id=student2.student_id, teacher_id=teacher1.teacher_id, subject_id=maths.subject_id, datetime=datetime(2024, 12, 16, 10, 0)),
            Lesson(student_id=student2.student_id, teacher_id=teacher2.teacher_id, subject_id=maths.subject_id, datetime=datetime(2024, 12, 16, 10, 0)),
            Lesson(student_id=student2.student_id, teacher_id=teacher3.teacher_id, subject_id=wos.subject_id, datetime=datetime(2024, 12, 16, 10, 0)),
            Lesson(student_id=student2.student_id, teacher_id=teacher4.teacher_id, subject_id=chemistry.subject_id, datetime=datetime(2024, 12, 16, 10, 0)),
            Lesson(student_id=student2.student_id, teacher_id=teacher5.teacher_id, subject_id=geography.subject_id, datetime=datetime(2024, 12, 13, 10, 0)),

            ### Lessons for student3
            Lesson(student_id=student3.student_id, teacher_id=teacher1.teacher_id, subject_id=maths.subject_id, datetime=datetime(2024, 12, 16, 10, 0)),
            Lesson(student_id=student3.student_id, teacher_id=teacher2.teacher_id, subject_id=maths.subject_id, datetime=datetime(2024, 12, 16, 10, 0)),
            Lesson(student_id=student3.student_id, teacher_id=teacher3.teacher_id, subject_id=wos.subject_id, datetime=datetime(2024, 12, 16, 10, 0)),
            Lesson(student_id=student3.student_id, teacher_id=teacher4.teacher_id, subject_id=physics.subject_id, datetime=datetime(2024, 12, 16, 10, 0)),
            Lesson(student_id=student3.student_id, teacher_id=teacher5.teacher_id, subject_id=maths.subject_id, datetime=datetime(2024, 12, 13, 10, 0))
        ]

        db.session.add_all(lessons)
        db.session.commit()

    def clear_db():
        db.session.query(Teacher).delete()
        db.session.query(Student).delete()
        db.session.query(Subject).delete()
        db.session.query(Calendar).delete()
        db.session.query(Lesson).delete()
        db.session.query()
        db.session.commit()

        

