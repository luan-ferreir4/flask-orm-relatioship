from dataclasses import dataclass
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, backref
from app.configs.database import db
from app.models.dog_model import DogModel


@dataclass
class OwnerModel(db.Model):
    id: int
    name: str
    gender: str
    dog: DogModel

    __tablename__ = "owners"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(String, nullable=False)
    gender = Column(String, nullable=False)
    dog_id = Column(
        Integer, 
        ForeignKey("dogs.id"),
        nullable=False,
        unique=True
    )

    dog = relationship(
        'DogModel',
        backref=backref('owner', uselist=False)
    )