from sqlalchemy import create_engine, Column, Integer, String, Text, Boolean, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

from database import engine

Base = declarative_base()


class Student(Base):
    __tablename__ = 'applicants'

    student_id = Column(Text, primary_key=True)
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

#
# class University(Base):
#     __tablename__ = 'universities'
#
#     university_id = Column(Text, primary_key=True)
#     university_name = Column(Text)
#
#
# class Payment(Base):
#     __tablename__ = 'payment'
#
#     transaction_id = Column(Text, primary_key=True)
#     student_id = Column(Text)
#     payment_status = Column(Text)
#     payment_time = Column(Date)
#
#
# class Application(Base):
#     __tablename__ = 'application'
#
#     application_id = Column(Text, primary_key=True)
#     applicant_id = Column(Text)
#     status = Column(Text)
#     university_id = Column(Text)
#     transaction_id = Column(Text)
#
#
#
# Base.metadata.create_all(engine)


if __name__ == '__main__':
    Student.__table__.drop(engine)
    Student.__table__.create(engine)
