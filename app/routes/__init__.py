from flask import Blueprint, Flask
from app.routes.dogs_route import bp_dogs
from app.routes.owner_route import bp_owner

bp = Blueprint('api',__name__,url_prefix='/api')

def init_app(app: Flask):
    bp.register_blueprint(bp_dogs)
    bp.register_blueprint(bp_owner)

    app.register_blueprint(bp)