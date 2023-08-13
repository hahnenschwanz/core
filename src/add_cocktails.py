import sqlite3

from models.cocktail import Cocktail

DATABASE_FILE = "database.db"


con = sqlite3.connect(DATABASE_FILE)
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS cocktails (id integer PRIMARY KEY, name text UNIQUE, imagefile text)")
cur.execute("CREATE TABLE IF NOT EXISTS ingredients (id integer PRIMARY KEY, name text UNIQUE, imagefile text, alcoholic boolean)")
cur.execute("CREATE TABLE IF NOT EXISTS recipe_entries (id integer PRIMARY KEY, ingredient_id integer, cocktail_id integer, amount float, FOREIGN KEY(ingredient_id) REFERENCES ingredients(id), FOREIGN KEY(cocktail_id) REFERENCES cocktails(id))")
cur.execute("CREATE TABLE IF NOT EXISTS cups (id integer PRIMARY KEY, user_id integer, FOREIGN KEY(user_id) REFERENCES users(id))")
cur.execute("CREATE TABLE IF NOT EXISTS users (id integer PRIMARY KEY, name text UNIQUE)")
cur.execute("CREATE TABLE IF NOT EXISTS tags (id integer PRIMARY KEY, name text UNIQUE)")
cur.execute("CREATE TABLE IF NOT EXISTS tag_entries (id integer PRIMARY KEY, tag_id integer, cocktail_id integer, FOREIGN KEY(tag_id) REFERENCES tags(id), FOREIGN KEY(cocktail_id) REFERENCES cocktails(id))")
# A Sex on the Beach cocktail contains 2 cl Vodka, 2 cl Peach Schnapps, 4 cl Orange Juice, 4 cl Cranberry Juice
sex_on_the_beach = Cocktail(
    id=1,
    name="Sex on the Beach",
    imageUrl="https://www.thecocktaildb.com/images/media/drink/lijtw51551455287.jpg",
    tags=["IBA", "ContemporaryClassic"],
    recipe=[
        ("Vodka", 0.02),
        ("Peach Schnapps", 0.02),
        ("Orange Juice", 0.04),
        ("Cranberry Juice", 0.04)
    ]
)

cur.execute("INSERT INTO ingredients VALUES (NULL,?,?,?)", ("Vodka", "vodka.txt", True))
cur.execute("INSERT INTO ingredients VALUES (NULL,?,?,?)", ("Peach Schnapps", "peach_schnapps.txt", True))
cur.execute("INSERT INTO ingredients VALUES (NULL,?,?,?)", ("Orange Juice", "orange_juice.txt", False))
cur.execute("INSERT INTO ingredients VALUES (NULL,?,?,?)", ("Cranberry Juice", "cranberry_juice.txt", False))
con.commit()

cur.execute("INSERT INTO tags VALUES (NULL,?)", ("IBA",))
cur.execute("INSERT INTO tags VALUES (NULL,?)", ("ContemporaryClassic",))
con.commit()


cur.execute("INSERT INTO cocktails VALUES (?,?,?)", (1, sex_on_the_beach.name, sex_on_the_beach.imageUrl))
cur.execute("INSERT INTO tag_entries VALUES (NULL,?,?)", (1, 1))
cur.execute("INSERT INTO tag_entries VALUES (NULL,?,?)", (2, 1))
cur.execute("INSERT INTO recipe_entries VALUES (NULL,?,?,?)", (1, 1, 0.02))
cur.execute("INSERT INTO recipe_entries VALUES (NULL,?,?,?)", (2, 1, 0.02))
cur.execute("INSERT INTO recipe_entries VALUES (NULL,?,?,?)", (3, 1, 0.04))
cur.execute("INSERT INTO recipe_entries VALUES (NULL,?,?,?)", (4, 1, 0.04))
con.commit()