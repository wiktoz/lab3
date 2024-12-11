from extensions import db
from models.teacher import Teacher
from models.lesson import Lesson
from models.subject import Subject
from models.calendar import Calendar
from models.student import Student
from models.subject import Subjects
from models.calendar import DayTypes
from sqlalchemy import func, extract
from datetime import date

class DBTest:
    def F1():
        result = (
            db.session.query(func.count(func.distinct(Lesson.student_id)))
            .join(Calendar, Lesson.teacher_id == Calendar.teacher_id)
            .filter(Calendar.day_type == DayTypes.workday.value)
            .all()
        )

        result = result[0][0]        

        print("[*] Testing F1 requirement")
        assert result == 3
        print(f"\t[+] F1 requirement passed. Expected 3, got {result}\n")

    def F2():
        result = (
            db.session.query(Lesson.teacher_id)
            .filter(extract('dow', Lesson.datetime).in_([5, 6, 7]))
            .distinct()
            .count()
        )

        print("[*] Testing F2 requirement")
        assert result == 1
        print(f"\t[+] F2 requirement passed. Expected 1, got {result}\n")


    def F3():
        result = (
            db.session.query(Student, func.count(Lesson.lesson_id).label('lesson_count'))
            .join(Lesson, Student.student_id == Lesson.student_id)
            .group_by(Student)
            .order_by(func.count(Lesson.lesson_id).desc())
            .first()
        )

        print("[*] Testing F3 requirement")
        print(f"\t[+] {result}\n")

    def F4():
        result = (
            db.session.query(
                Subject.name,
                func.count(Lesson.lesson_id).label("lesson_count")
            )
            .join(Lesson, Subject.subject_id == Lesson.subject_id)
            .group_by(Subject.subject_id, Subject.name)
            .order_by(func.count(Lesson.lesson_id).desc())
            .first()
        )

        print("[*] Testing F4 requirement")
        print(f"\t[+] {result}\n")


    def F5():
        print("[*] Testing F5 requirement")

        maths_subject = (
            db.session.query(Subject)
            .filter(Subject.name == "matematyka")
            .first()
        )

        if not maths_subject:
            print("[*] The subject 'matematyka' does not exist.")
            return

        result = (
            db.session.query(func.count(Lesson.lesson_id))
            .filter(Lesson.subject_id == maths_subject.subject_id)
            .scalar()
        )

        assert result == 7
        print(f"\t[+] F5 requirement passed. Expected 7, got {result}\n")


    def F6():
        result = (
            db.session.query(func.count(Lesson.lesson_id))
            .filter(extract('dow', Lesson.datetime) == 3)
            .scalar()
        )

        print("[*] Testing F6 requirement")
        assert result == 3
        print(f"\t[+] F6 requirement passed. Expected 3, got {result}\n")



    def F7():
        teacher_email = "m.brzoz@wum.edu.pl"
        lesson_date = date(2024, 12, 16)

        teacher = db.session.query(Teacher).filter(Teacher.email == teacher_email).first()

        if not teacher:
            print("[*] Teacher does not exist.")
            return

        result = (
            db.session.query(func.count(Lesson.lesson_id))
            .filter(Lesson.teacher_id == teacher.teacher_id, func.date(Lesson.datetime) == lesson_date)
            .scalar()
        )

        print("[*] Testing F7 requirement")
        assert result == 3
        print(f"\t[+] F7 requirement passed. Expected 3, got {result}\n")
