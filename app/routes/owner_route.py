from flask import Blueprint
from app.controllers import owners_controller

bp_owner = Blueprint('owner',__name__,url_prefix='/owners') 

bp_owner.post('')(owners_controller.create_owner)
bp_owner.get('')(owners_controller.get_all_owners)
bp_owner.get('/<int:id>')(owners_controller.get_owner_by_id)