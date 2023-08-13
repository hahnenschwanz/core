from enum import Enum
import uuid
 

class Ingredient:
    def __init__(self, name: str, imageUrl: str, alcoholic: bool):
        self.id = str(uuid.uuid4())
        self.name = name
        self.imageUrl = imageUrl
        self.alcoholic = alcoholic
    
    def __init__(self, id: str, name: str, imageUrl: str, alcoholic: bool):
        self.id = id
        self.name = name
        self.imageUrl = imageUrl
        self.alcoholic = alcoholic

    def __repr__(self):
        return f"Ingredient({self.name}, {self.imageUrl}, {self.alcoholic})"
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "imageUrl": self.imageUrl,
            "alcoholic": self.alcoholic
        }