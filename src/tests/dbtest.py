from flask import Flask, jsonify

from db import db, Cocktail, Ingredient, CocktailIngredient, Tag, CocktailTag

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/")
def create_tables():
    try:
        mojito = db.session.add(Cocktail(name="Mojito", description="A refreshing Cuban cocktail made with white rum, lime and mint.",  imageUrl="https://www.thecocktaildb.com/images/media/drink/metwgh1606770327.jpg"))
        old_fashioned = db.session.add(Cocktail(name="Old Fashioned", description="A classic cocktail made with bourbon, bitters, sugar and water.", imageUrl="https://www.thecocktaildb.com/images/media/drink/vrwquq1478252802.jpg"))

        white_rum = db.session.add(Ingredient(name="White rum"))
        lime = db.session.add(Ingredient(name="Lime"))
        mint = db.session.add(Ingredient(name="Mint"))
        bourbon = db.session.add(Ingredient(name="Bourbon"))
        bitters = db.session.add(Ingredient(name="Bitters"))
        sugar = db.session.add(Ingredient(name="Sugar"))
        water = db.session.add(Ingredient(name="Water"))

        sweet = db.session.add(Tag(name="Sweet"))
        sour = db.session.add(Tag(name="Sour"))
        db.session.commit()

        db.session.add(CocktailIngredient(cocktail_id=mojito.id, ingredient_id=white_rum.id, amount=0.02))
        db.session.add(CocktailIngredient(cocktail_id=mojito.id, ingredient_id=lime.id, amount=0.02))
        db.session.add(CocktailIngredient(cocktail_id=mojito.id, ingredient_id=mint.id, amount=0.02))
        db.session.add(CocktailIngredient(cocktail_id=old_fashioned.id, ingredient_id=bourbon.id, amount=0.02))
        db.session.add(CocktailIngredient(cocktail_id=old_fashioned.id, ingredient_id=bitters.id, amount=0.02))
        db.session.add(CocktailIngredient(cocktail_id=old_fashioned.id, ingredient_id=sugar.id, amount=0.02))
        db.session.add(CocktailIngredient(cocktail_id=old_fashioned.id, ingredient_id=water.id, amount=0.02))
        db.session.add(CocktailTag(cocktail_id=mojito.id, tag_id=sweet.id))
        db.session.add(CocktailTag(cocktail_id=mojito.id, tag_id=sour.id))
        db.session.add(CocktailTag(cocktail_id=old_fashioned.id, tag_id=sweet.id))
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