from flask import Flask
from models import db
from services import bcrypt
# from controllers import stuff

app = Flask(__name__)

app.config.from_object("config.Development")

# Database, Bcrypt, and JWT initializing
db.init_app(app)
bcrypt.init_app(app)
jwt.init_app(app) 

# Blueprints
app.register_blueprint(auth_blueprint, url_prefix="/auth")
app.register_blueprint(food_modify_controller, url_prefix="/food")

if __name__ == "__main__":
    app.run()
