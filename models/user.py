from datetime import datetime
from . import db

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(500), nullable=False)
    name = db.Column(db.String(30), nullable=False)
    surname = db.Column(db.String(50), nullable=False)
    created = db.Column(db.DateTime)
    modified = db.Column(db.DateTime)

    def __init__(self, email, password, name, surname=None, created, modified):
        self.email = email
        self.password = password
        self.name = name
        self.surname = surname
        self.created = created
        self.modified = modified

    def save():
        db.session.add()
        db.session.commit()
        return f("{self.name} added successfully.")

    @staticmethod
    def is_user(email):
        return User.query.filter_by(email=email).first()