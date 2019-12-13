from models.user import User
from .auth_service import generate_password_hash
from services import bcrypt

def create_user(data):
    if not User.is_user(email):
        password = generate_password_hash(password)
        new_user = User(email, password, name, surname)
        return new_user.save()
    else:
        return f"There is an account already associated with this email."

def delete_user(id):
    if U:
        pass
        
