import sqlite3
from models.cocktail import Cocktail
from models.ingredient import Ingredient
from config import DATABASE_FILE

class Database(object):
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        self.conn = sqlite3.connect(DATABASE_FILE, check_same_thread=False)

        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS cocktails (id integer PRIMARY KEY, name text UNIQUE, imagefile text)")
        self.cur.execute("CREATE TABLE IF NOT EXISTS ingredients (id integer PRIMARY KEY, name text UNIQUE, imagefile text, alcoholic boolean)")
        self.cur.execute("CREATE TABLE IF NOT EXISTS recipe_entries (id integer PRIMARY KEY, ingredient_id integer, cocktail_id integer, amount float, FOREIGN KEY(ingredient_id) REFERENCES ingredients(id), FOREIGN KEY(cocktail_id) REFERENCES cocktails(id))")
        self.cur.execute("CREATE TABLE IF NOT EXISTS cups (id integer PRIMARY KEY, user_id integer, FOREIGN KEY(user_id) REFERENCES users(id))")
        self.cur.execute("CREATE TABLE IF NOT EXISTS users (id integer PRIMARY KEY, name text UNIQUE)")
        self.cur.execute("CREATE TABLE IF NOT EXISTS tags (id integer PRIMARY KEY, name text UNIQUE)")
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
        cocktails = []
        self.cur.execute("SELECT c.id, c.name, c.imagefile FROM cocktails c")        
        cocktail_rows = self.cur.fetchall()
        if cocktail_rows is not None:
            for row in cocktail_rows:
                self.cur.execute("SELECT t.name FROM tags t JOIN tag_entries te ON t.id = te.tag_id WHERE te.cocktail_id = ?", (row[0],))
                tag_rows = self.cur.fetchall()
                tags = []
                for tag_row in tag_rows:
                    tags.append(tag_row[0])
                self.cur.execute("SELECT i.id, i.name, i.imagefile, i.alcoholic, r.amount FROM ingredients i JOIN recipe_entries r ON i.id = r.ingredient_id WHERE r.cocktail_id = ?", (row[0],))
                ingredient_rows = self.cur.fetchall()
                ingredients = []
                for ingredient_row in ingredient_rows:
                    ingredient = Ingredient(ingredient_row[0], ingredient_row[1], ingredient_row[2], ingredient_row[3])
                    ingredients.append((ingredient, ingredient_row[4]))
                cocktails.append(Cocktail(row[0], row[1], row[2], tags, ingredients))
            return cocktails
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

    


db = Database()