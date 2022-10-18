"""Models for Scheduler app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Teacher(db.Model):
    """Teacher."""

    __tablename__ = 'teachers'

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    name = db.Column(db.Text,
                     nullable=False,
                     unique=True)

    schedule = db.relationship('Timeslot', backref="teacher")


class Student(db.Model):
    """Student."""

    __tablename__ = 'students'

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    name = db.Column(db.Text,
                     nullable=False,
                     unique=True)

    schedule = db.relationship('Timeslot', backref="student")


class Timeslot(db.Model):
    """Timeslot."""

    __tablename__ = 'timeslots'

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    booked = db.Column(db.Boolean, nullable=False)
    datetime = db.Column(db.DateTime, nullable=False, unique=True)
    is_first_timeslot = db.Column(db.Boolean, nullable=False)
    lesson_duration = db.Column(db.Integer, nullable=False)
    teacher_id = db.Column(db.Integer,
                           db.ForeignKey("teachers.id"),
                           primary_key=True)
    student_id = db.Column(db.Integer,
                           db.ForeignKey("students.id"),
                           primary_key=True)


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
