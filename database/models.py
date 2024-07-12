from sqlalchemy import Column, Integer, String, Date, ForeignKey
from .database import Base


class CustomerObject(Base):
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    birth_date = Column(Date, index=True)
    phone = Column(String(10), index=True)
    email = Column(String(255), index=True)
    status = Column(String(100), index=True)
    address = Column(String(255), index=True)


class Subject(Base):
    __tablename__ = 'subject'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)


class CourseRegistration(Base):
    __tablename__ = 'course_registration'
    id = Column(Integer, primary_key=True, index=True)
    id_subject = Column(Integer, ForeignKey('subject.id'), index=True)
    id_customer = Column(Integer, ForeignKey('customer.id'), index=True)

