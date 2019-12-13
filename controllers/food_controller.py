from flask import Blueprint, request, Response, json
from flask_jwt_extended import jwt_required, get_jwt_identity

from services.food_service import new_recipe, edit_recipe

food_blueprint = Blueprint("food_api", __name__)

@food_blueprint.route("/new", methods=["POST"])
@jwt_required
def create_recipe():
    user = get_jwt_identity()
    data = request.json
    return create_recipe(data, user)

@food_blueprint.route("/all", methods=["GET"])
@jwt_required
def all_recipes():
    pass