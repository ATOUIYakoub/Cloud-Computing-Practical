from pydantic import BaseModel

class StudentSchema(BaseModel):
    student_id: int
    first_name: str
    last_name: str
    module_code: str


class StudentSchemaCreate(StudentSchema):
    pass

class StudentSchemaReturn(StudentSchema):
    student_id: int
    first_name: str
    last_name: str
    module_code: str

    class Config:
        orm_mode = True 
