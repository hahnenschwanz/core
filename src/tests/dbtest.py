from flask import Flask, jsonify

from db import db, Cocktail, Ingredient, CocktailIngredient

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/")
def create_tables():
    try:
        db.session.add(Cocktail(name="Mojito", description="A refreshing Cuban cocktail made with white rum, lime and mint.",  imageUrl="https://www.thecocktaildb.com/images/media/drink/metwgh1606770327.jpg"))
        db.session.add(Cocktail(name="Old Fashioned", description="A classic cocktail made with bourbon, bitters, sugar and water.", imageUrl="https://www.thecocktaildb.com/images/media/drink/vrwquq1478252802.jpg"))
        db.session.add(Ingredient(name="White rum"))
        db.session.add(Ingredient(name="Lime"))
        db.session.add(Ingredient(name="Mint"))
        db.session.add(Ingredient(name="Bourbon"))
        db.session.add(Ingredient(name="Bitters"))
        db.session.add(Ingredient(name="Sugar"))
        db.session.add(Ingredient(name="Water"))
        db.session.add(CocktailIngredient(cocktail_id=1, ingredient_id=1, amount="0.02"))
        db.session.add(CocktailIngredient(cocktail_id=1, ingredient_id=2, amount="0.02"))
        db.session.add(CocktailIngredient(cocktail_id=1, ingredient_id=3, amount="0.02"))
        db.session.add(CocktailIngredient(cocktail_id=2, ingredient_id=4, amount="0.02"))
        db.session.add(CocktailIngredient(cocktail_id=2, ingredient_id=5, amount="0.02"))
        db.session.add(CocktailIngredient(cocktail_id=2, ingredient_id=6, amount="0.02"))
        db.session.add(CocktailIngredient(cocktail_id=2, ingredient_id=7, amount="0.02"))
        db.session.commit()
    except Exception as e:
        db.session.rollback()
    cocktails = db.session.execute(db.select(Cocktail)).scalars().all()
    rs = []
    for cocktail in cocktails:
        r = {
            "id": cocktail.id,
            "name": cocktail.name,
            "description": cocktail.description,
            "imageUrl": cocktail.imageUrl,
            "ingredients": [ {
                "id": cocktail_ingredient.ingredient.id,
                "name": cocktail_ingredient.ingredient.name,
                "imageUrl": cocktail_ingredient.ingredient.imageUrl,
                "amount": cocktail_ingredient.amount
            } for cocktail_ingredient in cocktail.ingredients],
            "alcoholic": any([cocktail_ingredient.ingredient.alcoholic for cocktail_ingredient in cocktail.ingredients])
        }

        rs.append(r)
    return jsonify(rs)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=3000)