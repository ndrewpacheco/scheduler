from datetime import datetime
from models import db, connect_db, Teacher, Student, Timeslot


# #datetime(year, month, day)
# a = datetime(2018, 11, 28)
# print(a)

# # datetime(year, month, day, hour, minute, second, microsecond)
# b = datetime(2017, 11, 28, 23, 55, 59, 342380)
# print(b)

charlie = Student(name="Charlie")
andrew = Teacher(name="Andrew")

datetime_object = datetime(2023, 1, 1, 12, 00)
tmslt = Timeslot(booked=False, lesson_duration=30, datetime=datetime_object,
                 is_first_timeslot=True, teacher_id=1, student_id=1)


datetime_object = datetime(2023, 1, 1, 12, 30)
tmslt2 = Timeslot(booked=False,  lesson_duration=30, datetime=datetime_object,
                  is_first_timeslot=False, teacher_id=1, student_id=1)

db.session.add(charlie)
db.session.add(andrew)
db.session.add(tmslt)
db.session.add(tmslt2)

db.session.commit()
