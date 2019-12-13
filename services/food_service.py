from models.food import Food, FoodSchema
from datetime import datetime

food_schema = FoodSchema()

def new_recipe(data, user):
    new_recipe = Food(
        brand = data["brand"],
        food_form = data["food_form"],
        packaging_type = data["packaging_type"],
        protein = data["protein"],
        lifestage = data["lifestage"],
        breed_size = data["breed_size"],
        special_diet = data["special_diet"],
        created = datetime.utcnow(),
        created_by = user,
        updated = datetime.utcnow(),
        updated_by = user
    )
    try:
        new_recipe.save()
        message = {
            "Message": f'Food recipe stored successfully'
        }
        return message, 200
    except Exception as e:
        return str(e), 400

def edit_recipe(food_id, data):
    recipe_id = Food.get_food_item(food_id)
    updated = food_id.update()

