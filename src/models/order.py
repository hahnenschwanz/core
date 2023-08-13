import uuid

class Order:
    def __init__(self, user_id, cocktail_id):
        self.id = str(uuid.uuid4())
        self.cup = None
        self.user_id = user_id
        self.cocktail_id = cocktail_id
        self.timestamp = None