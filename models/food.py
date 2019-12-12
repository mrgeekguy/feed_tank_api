from datetime import datetime
from marshmallow import Schema, fields

from . import db

class Food(db.Model):
    __tablename__ = "dog_food"
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(75), nullable=False)
    food_form = db.Column(db.String(30), nullable=False)
    packaging_type = db.Column(db.String(30), nullable=False)
    protein = db.Column(db.String(25), nullable=False)
    lifestage = db.Column(db.String(25), nullable=False)
    breed_size = db.Column(db.String(25), nullable=False)
    special_diet = db.Column(db.String(75), nullable=False)
    created = db.Column(db.DateTime)
    created_by = db.Column(db.Integer, db.ForeignKey("users.id"))
    updated = db.Column(db.DateTime)
    updated_by = db.Column(db.Integer, db.ForeignKey("users.id"))

    def __init__(self, brand, food_form, packaging_type, protein, lifestage, breed_size, special_diet, created, created_by, updated, updated_by):
        self.brand = brand
        self.food_form = food_form
        self.packaging_type = packaging_type
        self.protein = protein
        self.lifestage = lifestage
        self.breed_size = breed_size
        self.special_diet = special_diet
        self.created = created
        self.created_by = created_by
        self.updated = updated
        self.updated_by = updated_by

    def save():
        db.session.add()
        db.session.commit()
        return f"Created food entry."

    def update(self, food, change_data):
        for key, item in change_data.items():
            setattr(food, key, item)
        self.updated = datetime.utcnow()
        db.session.commit()
        return food

    def delete():
        db.session.delete()
        db.session.commit()

    @staticmethod
    def get_food_item(food_id):
        return Food.query.filter_by(id=food_id).first()

    @staticmethod
    def get_user_of_post(food_id):
        return Food.query.filter_by(id=food_id).first().user() # TODO LOOK AT IT!!!!!!!!!!

class FoodSchema(Schema):
    id = fields.Int(dump_only=True)
    brand = fields.Str(required=True)
    food_form = fields.Str(required=True)
    packaging_type = fields.Str(required=True)
    protein = fields.Str(required=True)
    lifestage = fields.Str(required=True)
    breed_size = fields.Str(required=True)
    special_diet = fields.Str(required=True)
    created = fields.DateTime(dump_only=True)
    # created_by int fields with user_id
    updated = fields.DateTime(dump_only=True)
    # updated_by







