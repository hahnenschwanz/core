from flask import Blueprint, jsonify
from db import db, Cocktail, CocktailIngredient, Ingredient, Tag

cocktail_bp = Blueprint("cocktail", __name__)

def normalize_amount(amount, unit)
    if unit == "cl":
        return amount * 10
    elif unit == "dl":
        return amount * 100
    elif unit == "l":
        return amount * 1000
    else:
        return amount

@cocktail_bp.route("/api/cocktail", methods=["GET"])
def cocktail_list():
    cocktails = db.session.execute(db.select(Cocktail)).scalars().all()
    results = []
    for cocktail in cocktails:
        result = {
            "id": cocktail.id,
            "name": cocktail.name,
            "description": cocktail.description,
            "imageUrl": "https://www.thecocktaildb.com/images/media/drink/5noda61589575158.jpg",
            "tags": [cocktail_tag.tag.name for cocktail_tag in cocktail.tags],
            "ingredients": [ {
                "id": cocktail_ingredient.ingredient.id,
                "name": cocktail_ingredient.ingredient.name,
                "imageUrl": cocktail_ingredient.ingredient.imageUrl,
                "amount": cocktail_ingredient.amount,
                "manual": False
            } for cocktail_ingredient in cocktail.ingredients],
            "alcoholic": any([cocktail_ingredient.ingredient.alcoholic for cocktail_ingredient in cocktail.ingredients])
        }

        results.append(result)
    return jsonify(results)

@cocktail_bp.route("/api/cocktail/<int:id>", methods=["GET"])
def cocktail_get(id):
    cocktail = db.session.execute(db.select(Cocktail).where(Cocktail.id == id)).scalar()
    if cocktail is None:
        return jsonify({"error": "cocktail not found"}), 404
    result = {
        "id": cocktail.id,
        "name": cocktail.name,
        "description": cocktail.description,
        "imageUrl": cocktail.imageUrl,
        "tags": [cocktail_tag.tag.name for cocktail_tag in cocktail.tags],
        "ingredients": [ {
            "id": cocktail_ingredient.ingredient.id,
            "name": cocktail_ingredient.ingredient.name,
            "imageUrl": cocktail_ingredient.ingredient.imageUrl,
            "amount": cocktail_ingredient.amount
        } for cocktail_ingredient in cocktail.ingredients],
        "alcoholic": any([cocktail_ingredient.ingredient.alcoholic for cocktail_ingredient in cocktail.ingredients])
    }
    return jsonify(result)

@cocktail_bp.route("/api/cocktail/<int:id>", methods=["DELETE"])
def cocktail_delete(id):
    cocktail = db.session.execute(db.select(Cocktail).where(Cocktail.id == id)).scalar()
    if cocktail is None:
        return jsonify({"error": "cocktail not found"}), 404
    db.session.delete(cocktail)
    db.session.commit()
    return jsonify({"success": "cocktail deleted"})

@cocktail_bp.route("/api/cocktail", methods=["POST"])
def cocktail_create():
    data = request.get_json()
    name = data.get("name")
    description = data.get("description")
    imageUrl = data.get("imageUrl")
    recipe = data.get("recipe")
    if name is None or description is None or imageUrl is None or recipe is None:
        return jsonify({"error": "missing data"}), 400
    cocktail = Cocktail(name=name, description=description, imageUrl=imageUrl)
    db.session.add(cocktail)
    db.session.commit()
    for ingredient in recipe:
        ingredient_id = ingredient.get("id")
        amount = ingredient.get("amount")
        if ingredient_id is None or amount is None:
            return jsonify({"error": "missing data"}), 400
        cocktail_ingredient = CocktailIngredient(cocktail_id=cocktail.id, ingredient_id=ingredient_id, amount=amount)
        db.session.add(cocktail_ingredient)
    db.session.commit()
    return jsonify({"success": "cocktail created"})