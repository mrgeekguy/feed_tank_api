from flask import Flask
from models import db
from controllers import jwt
from controllers.auth_controller import auth_blueprint
from controllers.food_controller import food_blueprint
from services import bcrypt

app = Flask(__name__)

app.config.from_object("config.Development")

# Database, Bcrypt, and JWT initializing
db.init_app(app)
bcrypt.init_app(app)
jwt.init_app(app) 

# Blueprints
app.register_blueprint(auth_blueprint, url_prefix="/auth")
app.register_blueprint(food_blueprint, url_prefix="/food")

if __name__ == "__main__":
    app.run()
