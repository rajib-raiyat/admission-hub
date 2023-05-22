from sqlalchemy import Column, Integer, Text, Date, VARCHAR, Float
from sqlalchemy.orm import declarative_base

from database import engine

Base = declarative_base()


class Applicants(Base):
    __tablename__ = 'applicants'

    applicant_id = Column(VARCHAR(36), primary_key=True)
    hsc_roll = Column(Text)
    hsc_reg = Column(Text)
    hsc_board = Column(Text)
    hsc_year = Column(Text)
    hsc_result = Column(Float)
    hsc_group = Column(Text)

    name = Column(Text)
    email = Column(Text)
    college = Column(Text)
    phone_number = Column(Text)
    father_name = Column(Text)
    mother_name = Column(Text)
    username = Column(Text)
    password = Column(Text)


class University(Base):
    __tablename__ = 'universities'

    university_id = Column(VARCHAR(36), primary_key=True)
    university_name = Column(Text)
    university_image = Column(Text)
    university_intro = Column(Text)
    username = Column(Text)
    password = Column(Text)


class AdmissionGroup(Base):
    __tablename__ = 'admission_groups'

    admission_group_id = Column(VARCHAR(36), primary_key=True)
    university_id = Column(VARCHAR(36))
    group_name = Column(Text)
    exam_datetime = Column(Text)
    exam_time = Column(Text)
    application_fee = Column(Integer)
    exam_venue = Column(Text)
    min_req = Column(Float)
    hsc_group = Column(Text)


class Payment(Base):
    __tablename__ = 'payment'

    transaction_id = Column(VARCHAR(36), primary_key=True)
    applicant_id = Column(VARCHAR(36))
    student_id = Column(VARCHAR(36))
    payment_amount = Column(Text)
    payment_status = Column(Text)
    payment_time = Column(Date)
    groups = Column(Text)


class Application(Base):
    __tablename__ = 'application'

    application_id = Column(VARCHAR(36), primary_key=True)
    applicant_id = Column(VARCHAR(36))
    status = Column(Text)
    university_id = Column(VARCHAR(36))
    admission_group_id = Column(VARCHAR(36))
    transaction_id = Column(VARCHAR(36))


class Result(Base):
    __tablename__ = 'result'

    exam_id = Column(VARCHAR(36), primary_key=True)
    applicant_id = Column(VARCHAR(36))
    admission_group_id = Column(VARCHAR(36))
    university_id = Column(VARCHAR(36))
    university_name = Column(Text)
    exam_name = Column(Text)

    result = Column(VARCHAR(36))
    position = Column(VARCHAR(36))


if __name__ == '__main__':
    Base.metadata.create_all(engine)

    for i in [Applicants, University, AdmissionGroup, Payment, Application, Result]:
        i.__table__.drop(engine)
        i.__table__.create(engine)
