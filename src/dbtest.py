from flask import Flask, jsonify

from db import db, Cocktail, Ingredient, CocktailIngredient, Tag, CocktailTag

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

db.init_app(app)

with app.app_context():
    db.create_all()

blue_kolibri = {
    "name": "Blue Kolibri",
    "description": "",
    "imageURL": "",
    "tags": ["Süß","Fruchtig"],
    "recipe": [
        ("Cranberrysaft", 0.08),
        ("Ananassaft", 0.06),
        ("Tequila", 0.02),
        ("Vodka", 0.04),
        ("Blue Curacao", 0.02)
    ]
}

def add_cocktail_to_db(cocktail_data):
    try:
        with app.app_context():
            # Create Cocktail
            cocktail = Cocktail(
                name=cocktail_data["name"],
                description=cocktail_data["description"],
                imageUrl=cocktail_data["imageURL"]
            )
            db.session.add(cocktail)
            db.session.flush()  # This ensures cocktail.id is available

            # Create or retrieve tags
            tags = []
            for tag_name in cocktail_data["tags"]:
                tag = Tag.query.filter_by(name=tag_name).first()
                if not tag:
                    tag = Tag(name=tag_name)
                    db.session.add(tag)
                tags.append(tag)

            # Create ingredients and CocktailIngredients
            cocktail_ingredients = []
            for ingredient_name, amount in cocktail_data["recipe"]:
                ingredient = Ingredient.query.filter_by(name=ingredient_name).first()
                if not ingredient:
                    ingredient = Ingredient(name=ingredient_name, alcoholic=True)
                    db.session.add(ingredient)
                    db.session.flush()  # This ensures cocktail.id is available
                cocktail_ingredient = CocktailIngredient(
                    cocktail_id=cocktail.id,
                    ingredient_id=ingredient.id,
                    amount=amount,
                    unit="l"
                )
                cocktail_ingredients.append(cocktail_ingredient)
            db.session.flush()  # This ensures cocktail.id is available

            # Associate tags and ingredients with the cocktail
            for tag in tags:
                db.session.add(CocktailTag(cocktail_id=cocktail.id, tag_id=tag.id))
            
            for cocktail_ingredient in cocktail_ingredients:
                db.session.add(cocktail_ingredient)
            #cocktail.ingredients.extend(cocktail_ingredients)

            db.session.commit()
    except Exception as e:
        db.session.rollback()

@app.route("/")
def create_tables():
    try:
        mojito = Cocktail(name="Mojito", description="A refreshing Cuban cocktail made with white rum, lime and mint.",  imageUrl="https://www.thecocktaildb.com/images/media/drink/metwgh1606770327.jpg")
        old_fashioned = Cocktail(name="Old Fashioned", description="A classic cocktail made with bourbon, bitters, sugar and water.", imageUrl="https://www.thecocktaildb.com/images/media/drink/vrwquq1478252802.jpg")
        db.session.add (mojito)
        db.session.add (old_fashioned)


        white_rum =Ingredient(name="White rum", alcoholic=True)
        lime = Ingredient(name="Lime", alcoholic=False)
        mint = Ingredient(name="Mint", alcoholic=False)
        bourbon =Ingredient(name="Bourbon", alcoholic=True)
        bitters = Ingredient(name="Bitters", alcoholic=False)
        sugar = Ingredient(name="Sugar", alcoholic=False)
        water = Ingredient(name="Water", alcoholic=False)
        sweet = Tag(name="Sweet")
        sour = Tag(name="Sour")
        db.session.add(white_rum)
        db.session.add(lime)
        db.session.add(mint)
        db.session.add(bourbon)
        db.session.add(bitters)
        db.session.add(sugar)
        db.session.add(water)
        db.session.add(sweet)
        db.session.add(sour)

        db.session.flush()

        print (mojito.id)
        db.session.add(CocktailIngredient(cocktail_id=mojito.id, ingredient_id=white_rum.id, amount=0.02, unit="l"))
        db.session.add(CocktailIngredient(cocktail_id=mojito.id, ingredient_id=lime.id, amount=0.02, unit="l"))
        db.session.add(CocktailIngredient(cocktail_id=mojito.id, ingredient_id=mint.id, amount=0.02, unit="l"))
        db.session.add(CocktailIngredient(cocktail_id=old_fashioned.id, ingredient_id=bourbon.id, amount=0.02, unit="l"))
        db.session.add(CocktailIngredient(cocktail_id=old_fashioned.id, ingredient_id=bitters.id, amount=0.02, unit="l"))
        db.session.add(CocktailIngredient(cocktail_id=old_fashioned.id, ingredient_id=sugar.id, amount=0.02, unit="l"))
        db.session.add(CocktailIngredient(cocktail_id=old_fashioned.id, ingredient_id=water.id, amount=0.02, unit="l"))
        db.session.add(CocktailTag(cocktail_id=mojito.id, tag_id=sweet.id))
        db.session.add(CocktailTag(cocktail_id=mojito.id, tag_id=sour.id))
        db.session.add(CocktailTag(cocktail_id=old_fashioned.id, tag_id=sweet.id))
        db.session.commit()

        # or add it with a function
    except Exception as e:
        print(e)
        db.session.rollback()

    
    # or add it with a function (alcoholic not working)
    add_cocktail_to_db(blue_kolibri)

    cocktails = db.session.execute(db.select(Cocktail)).unique().scalars().all()
    rs = []
    for cocktail in cocktails:
        r = {
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

        rs.append(r)
    return jsonify(rs)





if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=3000)