from fastapi import FastAPI
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import model
from db_setup import SessionLocal, engine
from schema import StudentSchemaCreate, StudentSchemaReturn
from typing import List


app = FastAPI()

model.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/student/add", response_model=StudentSchemaReturn)
def add_new_student(student: StudentSchemaCreate, db: Session = Depends(get_db)):
    new_student = model.StudentModel(
        student_id=student.student_id,
        first_name=student.first_name,
        last_name=student.last_name,
        module_code=student.module_code
    )
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student


@app.get("/student/all", response_model=List[StudentSchemaReturn])
def read_items(db: Session = Depends(get_db)):
    students = db.query(model.StudentModel).all()
    return students
