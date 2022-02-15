from flask import jsonify, request, current_app
from http import HTTPStatus
from sqlalchemy.orm.session import Session
from app.configs.database import db
from app.models.dog_model import DogModel


def create_dog():
    session: Session = db.session
    data = request.get_json()

    new_dog = DogModel(**data)

    # current_app.db.session.add(new_dog)
    # current_app.db.session.commit()
    
    # session.add(new_dog)
    # session.commit()
    
    return jsonify(new_dog), HTTPStatus.CREATED


def get_all_dogs():
    session: Session = db.session

    dogs_list = session.query(DogModel).all()

    return jsonify(dogs_list), HTTPStatus.OK

def get_dog_by_id(id: int):
    session: Session = db.session

    dog = session.query(DogModel).get(id)

    return jsonify(dog), HTTPStatus.OK
