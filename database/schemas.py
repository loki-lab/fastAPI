from pydantic import BaseModel
from datetime import date


class Customer(BaseModel):
    id: int
    name: str
    birthday: date
    phone: str
    email: str
    status: str
    address: str


class CustomerCreate(BaseModel):
    name: str
    birthday: date
    phone: str
    email: str
    status: str
    address: str


class Subject(BaseModel):
    name: str


class CourseRegistration(BaseModel):
    id_subject: int
    id_customer: int
