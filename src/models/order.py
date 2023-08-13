import uuid

class Order:
    def __init__(self, user, cocktail):
        self.id = str(uuid.uuid4())
        self.cup = None
        self.user = user
        self.cocktail = cocktail
        self.timestamp = None