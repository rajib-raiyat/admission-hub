from sqlalchemy import Column, Integer, Text, Date, DateTime, VARCHAR, ForeignKey, Float, DOUBLE_PRECISION
from sqlalchemy.ext.declarative import declarative_base

from database import engine

Base = declarative_base()


class Applicants(Base):
    __tablename__ = 'applicants'

    applicant_id = Column(VARCHAR(36), primary_key=True)
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
    username = Column(Text)
    password = Column(Text)


class University(Base):
    __tablename__ = 'universities'

    university_id = Column(VARCHAR(36), primary_key=True)
    university_name = Column(Text)
    university_image = Column(Text)
    university_intro = Column(Text)


class AdmissionGroup(Base):
    __tablename__ = 'admission_groups'

    admission_group_id = Column(VARCHAR(36), primary_key=True)
    university_id = Column(VARCHAR(36), ForeignKey(University.university_id, ondelete='CASCADE'))
    group_name = Column(Text)


class Payment(Base):
    __tablename__ = 'payment'

    transaction_id = Column(VARCHAR(36), primary_key=True)
    payment_amount = Column(Text)
    payment_status = Column(Text)
    payment_time = Column(Date)


class Exam(Base):
    __tablename__ = 'exam'

    exam_id = Column(VARCHAR(36), primary_key=True)
    admission_group_id = Column(VARCHAR(36), ForeignKey(AdmissionGroup.admission_group_id, ondelete='CASCADE'))
    venue_id = Column(VARCHAR(36))
    venue_name = Column(Text)
    exam_datetime = Column(Text)
    application_deadline = Column(DateTime)
    exam_fee = Column(Integer)


class Application(Base):
    __tablename__ = 'application'

    application_id = Column(VARCHAR(36), primary_key=True)
    applicant_id = Column(VARCHAR(36), ForeignKey(Applicants.applicant_id, ondelete='CASCADE'))
    exam_id = Column(VARCHAR(36), ForeignKey(Exam.exam_id, ondelete='CASCADE'))
    transaction_id = Column(VARCHAR(36), ForeignKey(Payment.transaction_id, ondelete='SET NULL'))
    status = Column(Text)

    marks = Integer()


if __name__ == '__main__':
    Base.metadata.create_all(engine)

    for i in [Applicants, University, AdmissionGroup, Payment, Application, Exam]:
        i.__table__.drop(engine)
        i.__table__.create(engine)
