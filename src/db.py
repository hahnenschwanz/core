import sqlite3
from models.cocktail import Cocktail

class Database(object):
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Database, cls).__new__(
                                cls, *args, **kwargs)
        return cls._instance

    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS cocktails (id INTEGER PRIMARY KEY, name text, imagefile text, ingredients integer)")
        self.cur.execute("CREATE TABLE IF NOT EXISTS ingredients (id INTEGER PRIMARY KEY, name text)")
        self.cur.execute("CREATE TABLE IF NOT EXISTS ingredient_entries (id INTEGER PRIMARY KEY, ingredient_id integer, cocktail_id integer, amount integer)")
        self.conn.commit()
    def ingredient_create(self, name):
        self.cur.execute("INSERT INTO ingredients VALUES (NULL,?)", (name,))
        self.conn.commit()
    
    def ingredient_update(self, id, name):
        self.cur.execute("UPDATE ingredients SET name = ? WHERE id = ?", (name, id))
        self.conn.commit()
    
    def ingredient_entry_create(self, ingredient_id, cocktail_id, amount):
        self.cur.execute("INSERT INTO ingredient_entries VALUES (NULL,?,?,?)", (ingredient_id, cocktail_id, amount))
        self.conn.commit()

    def ingredient_entry_update(self, id, ingredient_id, cocktail_id, amount):
        self.cur.execute("UPDATE ingredient_entries SET ingredient_id = ?, cocktail_id = ?, amount = ? WHERE id = ?", (ingredient_id, cocktail_id, amount, id))
        self.conn.commit()
    
    def ingredient_entry_delete(self, id):
        self.cur.execute("DELETE FROM ingredient_entries WHERE id = ?", (id,))
        self.conn.commit()

    def cocktail_create(self, cocktail: Cocktail):
        self.cur.execute("INSERT INTO cocktails VALUES (NULL,?,?,?)", (cocktail.name, cocktail.imageUrl, cocktail.ingredients))
        self.conn.commit()
    
    def cocktail_update(self, cocktail: Cocktail):
        cocktail_id = self.cur.execute("UPDATE cocktails SET name = ?, imagefile = ?, ingredients = ? WHERE id = ?", (cocktail.name, cocktail.imageUrl, cocktail.ingredients, cocktail.id))
        self.conn.commit()
        return cocktail_id
    
    def get_cocktails(self) -> list[Cocktail]:
        self.cur.execute("SELECT * FROM cocktails")
        result = self.cur.fetchall()
        if result is not None:
            return [Cocktail(name, imageUrl, tags, ingredients) for id, name, imageUrl, tags, ingredients in result]
        else:
            return None

    
    def get_cocktail(self, id) -> Cocktail:
        self.cur.execute("SELECT * FROM cocktails WHERE id=?", (id,))
        result = self.cur.fetchone()
        if result is not None:
            id, name, imageUrl, tags, ingredients = result
            return Cocktail(name, imageUrl, tags, ingredients)
        else:
            return None
    
    def get_user_from_cup(self, cup):
        self.cur.execute("SELECT user_id FROM cups WHERE id = ?", (cup,))
        rows = self.cur.fetchall()
        return rows[0][0]
    
    def user_create(self, user):
        self.cur.execute("INSERT INTO users VALUES (NULL,?,?)", (user.name, user.cups))
        self.conn.commit()
        

    def __del__(self):
        self.conn.close()

    


db = Database("db.sqlite")