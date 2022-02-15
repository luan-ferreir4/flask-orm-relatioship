from flask import Blueprint
from app.controllers import dogs_controller

bp_dogs = Blueprint('dogs',__name__,url_prefix='/dogs') 

bp_dogs.post('')(dogs_controller.create_dog)
bp_dogs.get('')(dogs_controller.get_all_dogs)
bp_dogs.get('/<int:id>')(dogs_controller.get_dog_by_id)