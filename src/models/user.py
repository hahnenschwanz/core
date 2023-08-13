import uuid

class User:
    def __init__(self, name):
        self.id = str(uuid.uuid4())
        self.name = name
        self.cups = []

    def __init__(self, id, name, cups):
        self.id = id
        self.name = name
        self.cups = cups