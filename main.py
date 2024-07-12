from fastapi import FastAPI, Depends
from database import models, schemas
import crud
from database.database import SessionLocal, engine
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)
app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/register")
async def register(customer: schemas.CustomerCreate, db: Session = Depends(get_db)):
    return crud.create_customer(db=db, customer=customer)


@app.get("/all_customer")
async def get_all_customer(db: Session = Depends(get_db)):
    return crud.get_customers(db=db)


@app.delete("/delete_customer")
async def delete_customer(customer_id, db: Session = Depends(get_db)):
    return crud.delete_customer(db=db, customer_id=customer_id)


@app.put("/update_customer")
def update_customer(customer_id: int,
                    name: str = None,
                    phone: str = None,
                    birth_date: str = None,
                    email: str = None,
                    status: str = None,
                    address: str = None,
                    db: Session = Depends(get_db)
                    ):
    return crud.update_customer(db=db,
                                customer_id=customer_id,
                                name=name,
                                phone=phone,
                                birth_date=birth_date,
                                email=email,
                                status=status,
                                address=address
                                )


@app.post("/register_subjects")
def register_subjects(customer_id: int, subject_id: int, db: Session = Depends(get_db)):
    return crud.register_subjects(db=db, customer_id=customer_id, subjects_id=subject_id)


@app.post("/create_subjects")
def create_subjects(name: str, db: Session = Depends(get_db)):
    return crud.create_subject(db=db, name_subject=name)


@app.get("/get_subjects")
def get_subjects(db: Session = Depends(get_db)):
    return crud.get_subject(db=db)


@app.get("/register_subjects")
def get_register_subjects(db: Session = Depends(get_db)):
    return crud.get_register_subjects(db=db)
