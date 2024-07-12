from sqlalchemy.orm import Session
from database import models, schemas


def create_customer(db: Session, customer: schemas.CustomerCreate):
    db_customer = models.CustomerObject(
        name=customer.name,
        phone=customer.phone,
        birth_date=customer.birthday,
        email=customer.email,
        status=customer.status,
        address=customer.address)
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)

    return db_customer


def get_customer_by_id(db: Session,
                       customer_id: int
                       ):
    return db.query(models.CustomerObject).filter_by(id=customer_id).first()


def get_customers(db: Session):
    return db.query(models.CustomerObject).all()


def delete_customer(db: Session,
                    customer_id: int
                    ):
    db.delete(get_customer_by_id(db, customer_id))
    db.commit()

    return {"message": "Successfully deleted"}


def update_customer(db: Session,
                    customer_id: int,
                    name: str = None,
                    phone: str = None,
                    birth_date: str = None,
                    email: str = None,
                    status: str = None,
                    address: str = None
                    ):
    db_customer = get_customer_by_id(db, customer_id)
    if name is not None:
        db_customer.name = name

    if phone is not None:
        db_customer.phone = phone

    if birth_date is not None:
        db_customer.birth_date = birth_date

    if email is not None:
        db_customer.email = email

    if status is not None:
        db_customer.status = status

    if address is not None:
        db_customer.address = address

    db.commit()
    db.refresh(db_customer)

    return {"message": "Successfully updated"}


def register_subjects(db: Session,
                      customer_id: int,
                      subjects_id: int
                      ):
    if db.query(models.CourseRegistration).filter_by(id_subject=subjects_id,
                                                     id_customer=customer_id).first():
        return {"message": "Failed to register subjects"}

    db_register_subjects = models.CourseRegistration(
        id_subject=subjects_id,
        id_customer=customer_id
    )

    db.add(db_register_subjects)
    db.commit()
    return {"message": "Successfully registered"}


def create_subject(db: Session,
                   name_subject: str):
    db_subjects = models.Subject(
        name=name_subject
    )
    db.add(db_subjects)
    db.commit()
    db.refresh(db_subjects)
    return {"message": "Successfully create Subject"}


def get_subject(db: Session):
    return db.query(models.Subject).all()


def get_register_subjects(db: Session):
    return db.query(models.CourseRegistration).all()
