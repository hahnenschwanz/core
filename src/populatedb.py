#!/usr/bin/python3 

import requests, json
from pprint import pprint

from db import db

def normalize_amount(amount, unit)
    if unit == "cl":
        return amount * 10
    elif unit == "dl":
        return amount * 100
    elif unit == "l":
        return amount * 1000
    else:
        return amount

def the_cocktaildb_scraper():
    pass

def ipa_cocktails():
    url = "https://raw.githubusercontent.com/teijo/iba-cocktails/master/recipes.json"
    r = requests.get(url)
    if r.status_code != 200:
        raise Exception("Could not fetch cocktails from IBA")
    
    for cocktail in r.json():
        ingredients = []
        for ingredient in cocktail["ingredients"]:
            if "unit" in ingredient:
                amount = normalize_amount(ingredient["amount"], ingredient["unit"])
                ingredients.append({
                    "name": ingredient["name"],
                    "amount": amount
                })
        for ingredient in ingredients:
            db.ingredient_create(ingredient["name"])
            db.ingredient_entry_create(ingredient["name"], cocktail["name"], ingredient["amount"])
        db.cocktail_create(cocktail["name"], None)

