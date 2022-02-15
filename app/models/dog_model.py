from sqlalchemy import Column, Integer, String
from dataclasses import dataclass
from app.configs.database import db

@dataclass
class DogModel(db.Model):
    id: int
    name: str
    breed: str
    age: int

    __tablename__ = "dogs"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    breed = Column(String, nullable=False)
    age = Column(Integer)