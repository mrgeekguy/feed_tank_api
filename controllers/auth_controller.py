from flask import Blueprint, request
from flask_jwt_extended import create_access_token

from services import bcrypt
from services.user_service import create_user
from models.user import User

auth_blueprint = Blueprint("auth_api", __name__)

# Login route
@auth_blueprint.route("/login", methods=["POST"])
def login():
    body = request.json
    to_check = User.query.filter_by(email=body["email"]).first()
    if bcrypt.check_password_hash(to_check.password, body["password"]):
        access_token = create_access_token(to_check.id)
        return {
            "message": "Logged In"
            "token": access_token
        }
    else:
        return {
            "message": "Incorrect password"
        }

# Logout route
@auth_blueprint.route("/logout", methods=["POST"])
def logout():
    # TODO token deauthentication

# Registration route
@auth_blueprint.route("/register", methods=["POST"])
def register():
    body = request.json
    message = create_user(
        body["email"],
        bcrypt.generate_password_hash(body["password"]),
        body["name"]
        body["surname"]
    )

    return {
        "message": f"{name} has been added."
    }
