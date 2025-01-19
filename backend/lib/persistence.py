import datetime
from typing import Iterable

from sqlalchemy import Column, Integer, DateTime, String, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.orm import sessionmaker

class Base(DeclarativeBase):
    pass

class Calculation(Base):
    __tablename__ = 'calculations'

    id = Column(Integer, primary_key=True, autoincrement=True)
    expression: Mapped[str] = mapped_column(String)
    created_date = Column(DateTime)
    result: Mapped[str] = mapped_column(String)


# Database connection setup
DATABASE_URL = "sqlite:///example.db"  # Replace with your DB URL if not using SQLite
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

# Create tables
Base.metadata.create_all(engine)

def add_calculation(expression: str, result: str):
    with SessionLocal() as session:
        calculation = Calculation(
            expression=expression,
            created_date=datetime.datetime.now(datetime.UTC),
            result=result)
        session.add(calculation)
        session.commit()

def fetch_calculations() -> Iterable[Calculation]:
    with SessionLocal() as session:
        return session.query(Calculation).all()


