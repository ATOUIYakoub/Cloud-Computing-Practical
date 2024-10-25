from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLAlchemy settings for SQLite database
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:password@database:5432/student"
# Example connection string for PostgreSQL
DATABASE_URL = "postgresql://postgres:password@database:5432/student"


# Create the SQLAlchemy engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
