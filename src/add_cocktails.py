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

#Cocktails
desire = Cocktail(
    id=1,
    name="Desire",
    imageURL="",
    tags=["Frisch","Sauer"],
    recipe=[
        ("Gin", 0.04),
        ("Tonic Water", 0.13),
        ("Pfirsichlikör", 0.02),
        ("Zitronensaft", 0.02)
    ]
)
kiss43 = Cocktail(
    id=2,
    name="43er Kiss",
    imageURL="",
    tags=["Süß"],
    recipe=[
        ("Orangensaft", 0.10),
        ("Licor 43", 0.04),
        ("Zitronensaft", 0.02),
        ("Kirschsaft", 0.04)
    ]
)
cream43 = Cocktail(
    id=3,
    name="Cream 43",
    imageURL="",
    tags=["Süß","Sahne"],
    recipe=[
        ("Orangensaft", 0.07),
        ("Licor 43", 0.04),
        ("Maracuja", 0.07),
        ("Sahne", 0.02)
    ]
)
blue_kolibri = Cocktail(
    id=4,
    name="Blue Kolibri",
    imageURL="",
    tags=["Süß","Fruchtig"],
    recipe=[
        ("Cranberrysaft", 0.08),
        ("Ananassaft", 0.06),
        ("Tequila", 0.02),
        ("Vodka", 0.04),
        ("Blue Curacao", 0.02)
    ]
)
batida_kiba = Cocktail(
    id=5,
    name="Batida de Kiba",
    imageURL="",
    tags=["Süß"],
    recipe=[
        ("Bannanennektar", 0.09),
        ("Kirschsaft", 0.05),
        ("Batida de Coco", 0.04),
        ("Bacardi", 0.02)
    ]
)
swimmingpool = Cocktail(
    id=6,
    name="Swimmingpool",
    imageURL="",
    tags=["Classic","Stark","Süß","Sahne"],
    recipe=[
        ("Ananassaft", 0.08),
        ("Batida de Coco", 0.04),
        ("Vodka", 0.02),
        ("Blue Curacao", 0.01),
        ("Bacardi", 0.02),
        ("Sahne", 0.03) 
    ]
)
sex_on_the_beach = Cocktail(
    id=7,
    name="Sex on the Beach",
    imageURL="",
    tags=["Classic","Fruchtig"],
    recipe=[
        ("Cranberrysaft", 0.08),
        ("Orangensaft", 0.06),
        ("Vodka", 0.04),
        ("Pfirsichlikör", 0.02)
    ]
)
long_beach = Cocktail(
    id=8,
    name="Long Beach",
    imageURL="",
    tags=["Extra Stark"],
    recipe=[
        ("Orangensaft", 0.04),
        ("Kirschsaft", 0.06),
        ("Zitronensaft", 0.02),
        ("Bacardi", 0.02),
        ("Gin", 0.02),
        ("Vodka", 0.02),
        ("Tequila", 0.02)
    ]
)
tequilla_sunrise = Cocktail(
    id=9,
    name="Tequilla Sunrise",
    imageURL="",
    tags=["Classic","Fruchtig"],
    recipe=[
        ("Orangensaft", 0.14),
        ("Granadinensyrup", 0.02),
        ("Tequila", 0.04)
    ]
)
pina_colada = Cocktail(
    id=10,
    name="Pina Colada",
    imageURL="",
    tags=["Classic","Süß","Sahne"],
    recipe=[
        ("Batida de Coco", 0.04),
        ("Ananassaft", 0.10),
        ("Bacardi", 0.02),
        ("Sahne", 0.02)
    ]
)
alex = Cocktail(
    id=11,
    name="Alex",
    imageURL="",
    tags=["Exlusiv","Fruchtig","Frisch"],
    recipe=[
        ("Cranberrysaft", 0.06),
        ("Ananassaft", 0.06),
        ("Gin", 0.04),
        ("Granadinensyrup", 0.04),
        ("Zitronensaft", 0.02)
    ]
)
alexi = Cocktail(
    id=12,
    name="Alexi",
    imageURL="",
    tags=["Exlusiv","Fruchtig","Frisch"],
    recipe=[
        ("Cranberrysaft", 0.08),
        ("Ananassaft", 0.10),
        ("Granadinensyrup", 0.02),
        ("Zitronensaft", 0.02)
    ]
)
kiba = Cocktail(
    id=13,
    name="KiBa",
    imageURL="",
    tags=["Süß"],
    recipe=[
        ("Bannanennektar", 0.12),
        ("Kirschsaft", 0.08)
    ]
)
sweet_orange = Cocktail(
    id=14,
    name="Sweet Orange",
    imageURL="",
    tags=["Süß","Sahne"],
    recipe=[
        ("Orangensaft", 0.08),
        ("Ananassaft", 0.04),
        ("Bannanennektar", 0.04),
        ("Sahne", 0.04)
    ]
)
beach_beauty = Cocktail(
    id=15,
    name="Beach Beauty",
    imageURL="",
    tags=["Fruchtig"],
    recipe=[
        ("Tonic Water", 0.10),
        ("Orangensaft", 0.08),
        ("Granadinensyrup", 0.02)
    ]
)
vodka_o = Cocktail(
    id=16,
    name="Vodka-O",
    imageURL="",
    tags=["Longdrink"],
    recipe=[
        ("Orangensaft", 0.16),
        ("Vodka", 0.04)
    ]
)
licor43_o = Cocktail(
    id=17,
    name="43iger O-Saft",
    imageURL="",
    tags=["Longdrink","Süß"],
    recipe=[
        ("Orangensaft", 0.15),
        ("Licor 43", 0.05)
    ]
)
licor43_o_sahne = Cocktail(
    id=18,
    name="43iger O-Saft mit Sahne",
    imageURL="",
    tags=["Longdrink","Sahne"],
    recipe=[
        ("Orangensaft", 0.13),
        ("Licor 43", 0.04),
        ("Sahne", 0.03)
    ]
)
gin_tonic = Cocktail(
    id=19,
    name="Gin Tonic",
    imageURL="",
    tags=["Longdrink"],
    recipe=[
        ("Tonic Water", 0.12),
        ("Gin", 0.04)
    ]
)


#Add Ingredients
cur.execute("INSERT INTO ingredients VALUES (NULL,?,?,?)", ("Licor 43", "licor43.txt", True))
cur.execute("INSERT INTO ingredients VALUES (NULL,?,?,?)", ("Tequila", "tequila.txt", True))
cur.execute("INSERT INTO ingredients VALUES (NULL,?,?,?)", ("Batida de Coco", "batida_de_coco.txt", True))
cur.execute("INSERT INTO ingredients VALUES (NULL,?,?,?)", ("Vodka", "vodka.txt", True))
cur.execute("INSERT INTO ingredients VALUES (NULL,?,?,?)", ("Blue Curacao", "blue_curacao.txt", True))
cur.execute("INSERT INTO ingredients VALUES (NULL,?,?,?)", ("Gin", "gin.txt", True))
cur.execute("INSERT INTO ingredients VALUES (NULL,?,?,?)", ("Pfirsichlikör", ".pfirsichlikoer.txt", True))
cur.execute("INSERT INTO ingredients VALUES (NULL,?,?,?)", ("Bacardi", "bacardi.txt", True))
cur.execute("INSERT INTO ingredients VALUES (NULL,?,?,?)", ("Granadinensyrup", "granadinensyrup.txt", False))
cur.execute("INSERT INTO ingredients VALUES (NULL,?,?,?)", ("Zitronensaft", "zitronensaft.txt", False))
cur.execute("INSERT INTO ingredients VALUES (NULL,?,?,?)", ("Tonic Water", "tonic_water.txt", False))
cur.execute("INSERT INTO ingredients VALUES (NULL,?,?,?)", ("Cranberrysaft", "cranberrysaft.txt", False))
cur.execute("INSERT INTO ingredients VALUES (NULL,?,?,?)", ("Orangensaft", "orangensaft.txt", False))
cur.execute("INSERT INTO ingredients VALUES (NULL,?,?,?)", ("Ananassaft", "ananassaft.txt", False))
cur.execute("INSERT INTO ingredients VALUES (NULL,?,?,?)", ("Kirschsaft", "kirschsaft.txt", False))
cur.execute("INSERT INTO ingredients VALUES (NULL,?,?,?)", ("Maracuja", "maracuja.txt", False))
cur.execute("INSERT INTO ingredients VALUES (NULL,?,?,?)", ("Bannanennektar", "bannanennektar.txt", False))
cur.execute("INSERT INTO ingredients VALUES (NULL,?,?,?)", ("Sahne", "sahne.txt", False))


con.commit()

#Add Tags
cur.execute("INSERT INTO tags VALUES (NULL,?)", ("Longdrink",))
cur.execute("INSERT INTO tags VALUES (NULL,?)", ("Classic",))
cur.execute("INSERT INTO tags VALUES (NULL,?)", ("Exlusiv",))
cur.execute("INSERT INTO tags VALUES (NULL,?)", ("Neu",))
cur.execute("INSERT INTO tags VALUES (NULL,?)", ("Süß",))
cur.execute("INSERT INTO tags VALUES (NULL,?)", ("Fruchtig",))
cur.execute("INSERT INTO tags VALUES (NULL,?)", ("Sahne",))
cur.execute("INSERT INTO tags VALUES (NULL,?)", ("Bitter",))
cur.execute("INSERT INTO tags VALUES (NULL,?)", ("Sauer",))
cur.execute("INSERT INTO tags VALUES (NULL,?)", ("Stark",))
cur.execute("INSERT INTO tags VALUES (NULL,?)", ("Extra Stark",))
cur.execute("INSERT INTO tags VALUES (NULL,?)", ("Frisch",))

con.commit()

# Add the cocktail
cur.execute("INSERT INTO cocktails VALUES (?,?,?)", (1, sex_on_the_beach.name, sex_on_the_beach.imageUrl))
cur.execute("INSERT INTO tag_entries VALUES (NULL,?,?)", (1, 1))
cur.execute("INSERT INTO tag_entries VALUES (NULL,?,?)", (2, 1))
cur.execute("INSERT INTO recipe_entries VALUES (NULL,?,?,?)", (1, 1, 0.02))
cur.execute("INSERT INTO recipe_entries VALUES (NULL,?,?,?)", (2, 1, 0.02))
cur.execute("INSERT INTO recipe_entries VALUES (NULL,?,?,?)", (3, 1, 0.04))
cur.execute("INSERT INTO recipe_entries VALUES (NULL,?,?,?)", (4, 1, 0.04))
con.commit()