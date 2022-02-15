from flask import jsonify, request, session
from http import HTTPStatus
from sqlalchemy.orm import Session
from app.configs.database import db
from app.models.owner_model import OwnerModel


def create_owner():
    session: Session = db.session

    data = request.get_json()

    new_owner = OwnerModel(**data)

    session.add(new_owner)
    session.commit()

    return jsonify(new_owner), HTTPStatus.CREATED


def get_all_owners():
    session: Session = db.session
    owners_list = session.query(OwnerModel).all()
    return jsonify(owners_list), HTTPStatus.OK


def get_owner_by_id(id: int):
    session: Session = db.session
    owner = session.query(OwnerModel).get(id)
    return jsonify(owner), HTTPStatus.OK
