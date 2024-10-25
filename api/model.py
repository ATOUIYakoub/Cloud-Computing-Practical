from sqlalchemy import  Column,  Integer, String
from db_setup import Base

class StudentModel(Base):
    __tablename__ = "stdents"
    student_id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    module_code = Column(String(10), nullable=False, index=True)
    
