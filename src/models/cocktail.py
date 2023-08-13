import uuid

class Cocktail(object):
    def __init__(self, name, imageUrl, tags, ingredients):
        self.id = str(uuid.uuid4())
        self.name = name
        self.imageUrl = imageUrl
        self.tags = tags
        self.ingredients = ingredients
    def __repr__(self):
        return f"Cocktail({self.name}, {self.imageUrl}, {self.tags}, {self.ingredients})"
    def __str__(self):
        self.__repr__()
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "imageUrl": self.imageUrl,
            "tags": self.tags,
            "ingredients": self.ingredients
        }
    
    