from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Cocktail(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    description = db.Column(db.String)
    imageUrl = db.Column(db.String)
    ingredients = db.relationship('CocktailIngredient', backref='cocktail', lazy=True)
    orders = db.relationship('Order', backref='cocktail', lazy=False)
    tags = db.relationship('CocktailTag', backref='cocktail', lazy=False)


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    cocktails = db.relationship('CocktailTag', backref='tag', lazy=False)

class CocktailTag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cocktail_id = db.Column(db.Integer, db.ForeignKey('cocktail.id'), nullable=False)
    tag_id = db.Column(db.Integer, db.ForeignKey('tag.id'), nullable=False)
    tag = db.relationship('Tag', backref='tag', lazy=True)

class Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    imageUrl = db.Column(db.String)
    alcoholic = db.Column(db.Boolean)

class CocktailIngredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cocktail_id = db.Column(db.Integer, db.ForeignKey('cocktail.id'), nullable=False)
    ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredient.id'), nullable=False)
    amount = db.Column(db.Float)
    unit = db.Column(db.String)
    ingredient = db.relationship('Ingredient', backref='ingredient', lazy=True)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String)
    cup = db.relationship('Cup', backref='user', lazy=True)
    orders = db.relationship('Order', backref='user', lazy=True)

class Cup(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    orders = db.relationship('Order', backref='cup', lazy=False)
    user = db.relationship('User', backref='cup', lazy=True)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cup_id = db.Column(db.Integer, db.ForeignKey('cup.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    cocktail_id = db.Column(db.Integer, db.ForeignKey('cocktail.id'), nullable=False)
    status = db.Column(db.String)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    cocktail = db.relationship('Cocktail', backref='order', lazy=True)
