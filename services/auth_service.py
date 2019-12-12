from . import bcrypt

def generate_password_hash(password):
    return bcrypt.generate_password_hash(password).decode("utf-8")