from sqlalchemy import create_engine, Column, Integer, String, Text, Boolean, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

from database import engine

Base = declarative_base()


class Applicants(Base):
    __tablename__ = 'applicants'

    applicant_id = Column(Text, primary_key=True)
    hsc_roll = Column(Text)
    hsc_reg = Column(Text)
    hsc_board = Column(Text)
    hsc_year = Column(Text)
    hsc_result = Column(Text)
    hsc_group = Column(Text)

    name = Column(Text)
    email = Column(Text)
    college = Column(Text)
    phone_number = Column(Text)
    father_name = Column(Text)
    mother_name = Column(Text)


class University(Base):
    __tablename__ = 'universities'

    university_id = Column(Text, primary_key=True)
    university_name = Column(Text)
    university_image = Column(Text)  # abs path of the image
    university_intro = Column(Text)


class AdmissionGroup(Base):
    __tablename__ = 'admission_groups'

    admission_group_id = Column(Text, primary_key=True)
    university_id = Column(Text)
    group_name = Column(Text)
    exam_datetime = Column(Text)  # datetime
    application_fee = Column(Integer)


class Payment(Base):
    __tablename__ = 'payment'

    transaction_id = Column(Text, primary_key=True)
    applicant_id = Column(Text)
    student_id = Column(Text)
    payment_amount = Column(Text)
    payment_status = Column(Text)
    payment_time = Column(Date)


class Application(Base):
    __tablename__ = 'application'

    application_id = Column(Text, primary_key=True)
    applicant_id = Column(Text)
    status = Column(Text)
    university_id = Column(Text)
    admission_group_id = Column(Text)
    transaction_id = Column(Text)


class Exam(Base):
    __tablename__ = 'exam'

    exam_id = Column(Text)
    venue_id = Column(Text)
    venue_name = Column(Text)
    students = Column(Text)  # list
    applicantions = Column(Text)  # list
    university_id = Column(Text)
    admission_group_id = Column(Text)


# Base.metadata.create_all(engine)


if __name__ == '__main__':
    Applicants.__table__.drop(engine)
    Applicants.__table__.create(engine)
