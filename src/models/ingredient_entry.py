import uuid

class Ingredient:
    def __init__(self, name, imageUrl, tags, type):
        self.id = str(uuid.uuid4())
        self.name = name
        self.imageUrl = imageUrl
        self.tags = tags
        self.type = type