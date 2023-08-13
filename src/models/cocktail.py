import uuid
from .ingredient import Ingredient

class Cocktail(object):
    def __init__(self, name, imageUrl, tags: list[str], recipe: list([(Ingredient,float)])):
        self.id = str(uuid.uuid4())
        self.name = name
        self.imageUrl = imageUrl
        self.tags = tags
        self.recipe = recipe
    def __init__(self, id, name, imageUrl, tags: list[str], recipe: list[(Ingredient,float)]):
        self.id = id
        self.name = name
        self.imageUrl = imageUrl
        self.tags: list[str] = tags
        self.recipe: list[(Ingredient,float)] = recipe
    def __repr__(self):
        return f"Cocktail({self.name}, {self.imageUrl}, {self.tags}, {self.recipe})"
    def __str__(self):
        self.__repr__()
    def serialize(self):
        return {
            "id": str(self.id),
            "name": self.name,
            "imageUrl": self.imageUrl,
            "tags": self.tags,
            "alcoholic": True,
            #"hidden": False,
            "ingredients": [{
                                "id": r[0].id,
                                "name": r[0].name,
                                "amount": r[1],
                                "manual": False
                            } for r in self.recipe]
        }
    
    