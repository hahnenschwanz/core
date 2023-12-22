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
    imageUrl="/images/desire.jpg",
    tags=["Frisch","Sauer"],
    recipe=[
        ("Gin", 0.04),
        ("Tonic Water", 0.13),
        ("Granadinensyrup", 0.02),
        ("Zitronensaft", 0.02)
    ]
)
kiss43 = Cocktail(
    id=2,
    name="43er Kiss",
    imageUrl="/images/43er-kiss.jpg",
    tags=["Süß"],
    recipe=[
        ("Licor 43", 0.04),
        ("Orangensaft", 0.10),
        ("Zitronensaft", 0.02),
        ("Kirschsaft", 0.04)
    ]
)
cream43 = Cocktail(
    id=3,
    name="Cream 43",
    imageUrl="/images/43er-cream.jpg",
    tags=["Süß","Sahne"],
    recipe=[
        ("Licor 43", 0.04),
        ("Orangensaft", 0.07),
        ("Maracuja", 0.07),
        ("Sahne", 0.02)
    ]
)
blue_kolibri = Cocktail(
    id=4,
    name="Blue Kolibri",
    imageUrl="/images/blue-kolibri.jpg",
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
    imageUrl="/images/kiba.jpg",
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
    imageUrl="/images/swimming-pool.jpg",
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
    imageUrl="/images/sex-on-the-beach.jpg",
    tags=["Classic","Fruchtig"],
    recipe=[
        ("Cranberrysaft", 0.08),
        ("Orangensaft", 0.06),
        ("Vodka", 0.04),
        ("Granadinensyrup", 0.02)
    ]
)
long_beach = Cocktail(
    id=8,
    name="Long Beach",
    imageUrl="/images/long-beach.jpg",
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
    name="Tequila Sunrise",
    imageUrl="/images/tequila-sunrise.jpg",
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
    imageUrl="/images/pina-colada.jpg",
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
    imageUrl="/images/alex.jpg",
    tags=["Exlusiv","Fruchtig","Frisch"],
    recipe=[
        ("Cranberrysaft", 0.06),
        ("Ananassaft", 0.06),
        ("Gin", 0.04),
        ("Granadinensyrup", 0.02),
        ("Zitronensaft", 0.02)
    ]
)
alexi = Cocktail(
    id=12,
    name="Alexi",
    imageUrl="/images/alex.jpg",
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
    imageUrl="/images/kiba.jpg",
    tags=["Süß"],
    recipe=[
        ("Bannanennektar", 0.12),
        ("Kirschsaft", 0.08)
    ]
)
sweet_orange = Cocktail(
    id=14,
    name="Sweet Orange",
    imageUrl="/images/sweet-orange.jpg",
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
    imageUrl="/images/beach-beauty.jpg",
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
    imageUrl="/images/vodka-o.jpg",
    tags=["Longdrink"],
    recipe=[
        ("Orangensaft", 0.16),
        ("Vodka", 0.04)
    ]
)
licor43_o = Cocktail(
    id=17,
    name="43iger O-Saft",
    imageUrl="/images/43er-o-saft.jpg",
    tags=["Longdrink","Süß"],
    recipe=[
        ("Orangensaft", 0.15),
        ("Licor 43", 0.05)
    ]
)
licor43_o_sahne = Cocktail(
    id=18,
    name="43iger O-Saft mit Sahne",
    imageUrl="/images/43er-o-saft-sahne.jpg",
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
    imageUrl="/images/gin-tonic.jpg",
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

# desire
cur.execute("INSERT INTO cocktails VALUES (?,?,?)", (1, desire.name, desire.imageUrl))
cur.execute("INSERT INTO tag_entries VALUES (NULL,?,?)", (12, 1))
cur.execute("INSERT INTO tag_entries VALUES (NULL,?,?)", (9, 1))
cur.execute("INSERT INTO recipe_entries VALUES (NULL,?,?,?)", (6, 1, 0.04))
cur.execute("INSERT INTO recipe_entries VALUES (NULL,?,?,?)", (11, 1, 0.13))
cur.execute("INSERT INTO recipe_entries VALUES (NULL,?,?,?)", (9, 1, 0.02))
cur.execute("INSERT INTO recipe_entries VALUES (NULL,?,?,?)", (10, 1, 0.02))
con.commit()

# kiss43
cur.execute("INSERT INTO cocktails VALUES (?,?,?)", (2, kiss43.name, kiss43.imageUrl))
cur.execute("INSERT INTO tag_entries VALUES (NULL,?,?)", (5, 2))
cur.execute("INSERT INTO recipe_entries VALUES (NULL,?,?,?)", (13, 2, 0.10))
cur.execute("INSERT INTO recipe_entries VALUES (NULL,?,?,?)", (1, 2, 0.04))
cur.execute("INSERT INTO recipe_entries VALUES (NULL,?,?,?)", (10, 2, 0.02))
cur.execute("INSERT INTO recipe_entries VALUES (NULL,?,?,?)", (15, 2, 0.04))
con.commit()

# cream43
cur.execute("INSERT INTO cocktails VALUES (?,?,?)", (3, cream43.name, cream43.imageUrl))
cur.execute("INSERT INTO tag_entries VALUES (NULL,?,?)", (5, 3))
cur.execute("INSERT INTO tag_entries VALUES (NULL,?,?)", (7, 3))
cur.execute("INSERT INTO recipe_entries VALUES (NULL,?,?,?)", (1, 3, 0.04))
cur.execute("INSERT INTO recipe_entries VALUES (NULL,?,?,?)", (18, 3, 0.02))
cur.execute("INSERT INTO recipe_entries VALUES (NULL,?,?,?)", (16, 3, 0.07))
cur.execute("INSERT INTO recipe_entries VALUES (NULL,?,?,?)", (13, 3, 0.07))
con.commit()

# blue_kolibri
cur.execute("INSERT INTO cocktails VALUES (?,?,?)", (4, blue_kolibri.name, blue_kolibri.imageUrl))
cur.execute("INSERT INTO tag_entries VALUES (NULL,?,?)", (5, 4))
cur.execute("INSERT INTO tag_entries VALUES (NULL,?,?)", (6, 4))
cur.execute("INSERT INTO recipe_entries VALUES (NULL,?,?,?)", (2, 4, 0.02))
cur.execute("INSERT INTO recipe_entries VALUES (NULL,?,?,?)", (4, 4, 0.04))
cur.execute("INSERT INTO recipe_entries VALUES (NULL,?,?,?)", (5, 4, 0.02))
cur.execute("INSERT INTO recipe_entries VALUES (NULL,?,?,?)", (14, 4, 0.06))
cur.execute("INSERT INTO recipe_entries VALUES (NULL,?,?,?)", (12, 4, 0.08))
con.commit()

# batida_kiba
cur.execute("INSERT INTO cocktails VALUES (?,?,?)", (5, batida_kiba.name, batida_kiba.imageUrl))
cur.execute("INSERT INTO tag_entries VALUES (NULL,?,?)", (5, 5)),
cur.execute("INSERT INTO recipe_entries VALUES (NULL,?,?,?)", (3, 5, 0.04))
cur.execute("INSERT INTO recipe_entries VALUES (NULL,?,?,?)", (8, 5, 0.02))
cur.execute("INSERT INTO recipe_entries VALUES (NULL,?,?,?)", (17, 5, 0.09))
cur.execute("INSERT INTO recipe_entries VALUES (NULL,?,?,?)", (15, 5, 0.05))
con.commit()

# swimmingpool
cur.execute("INSERT INTO cocktails VALUES (?,?,?)", (6, swimmingpool.name, swimmingpool.imageUrl))
cur.execute("INSERT INTO tag_entries VALUES (NULL,?,?)", (2, 6))
cur.execute("INSERT INTO tag_entries VALUES (NULL,?,?)", (10, 6))
cur.execute("INSERT INTO tag_entries VALUES (NULL,?,?)", (5, 6))
cur.execute("INSERT INTO tag_entries VALUES (NULL,?,?)", (7, 6))

cur.execute("INSERT INTO recipe_entries VALUES (NULL,?,?,?)", (3, 6, 0.04))
cur.execute("INSERT INTO recipe_entries VALUES (NULL,?,?,?)", (4, 6, 0.02))
cur.execute("INSERT INTO recipe_entries VALUES (NULL,?,?,?)", (5, 6, 0.02))
cur.execute("INSERT INTO recipe_entries VALUES (NULL,?,?,?)", (18, 6, 0.03))
cur.execute("INSERT INTO recipe_entries VALUES (NULL,?,?,?)", (8, 6, 0.02))
cur.execute("INSERT INTO recipe_entries VALUES (NULL,?,?,?)", (14, 6, 0.08))
con.commit()

# sex_on_the_beach
cur.execute("INSERT INTO cocktails VALUES (?,?,?)", (7, sex_on_the_beach.name, sex_on_the_beach.imageUrl))
cur.execute("INSERT INTO tag_entries VALUES (NULL,?,?)", (2, 7))
cur.execute("INSERT INTO tag_entries VALUES (NULL,?,?)", (6, 7))
cur.execute("INSERT INTO recipe_entries VALUES (NULL,?,?,?)", (4, 7, 0.04))
cur.execute("INSERT INTO recipe_entries VALUES (NULL,?,?,?)", (9, 7, 0.02))
cur.execute("INSERT INTO recipe_entries VALUES (NULL,?,?,?)", (13, 7, 0.06))
cur.execute("INSERT INTO recipe_entries VALUES (NULL,?,?,?)", (12, 7, 0.08))

con.commit()

# long_beach
cur.execute("INSERT INTO cocktails VALUES (?,?,?)", (8, long_beach.name, long_beach.imageUrl))
cur.execute("INSERT INTO tag_entries VALUES (NULL,?,?)", (10, 8)),
cur.execute("INSERT INTO recipe_entries VALUES (NULL,?,?,?)", (13, 8, 0.04))
cur.execute("INSERT INTO recipe_entries VALUES (NULL,?,?,?)", (15, 8, 0.06))
cur.execute("INSERT INTO recipe_entries VALUES (NULL,?,?,?)", (10, 8, 0.02))
cur.execute("INSERT INTO recipe_entries VALUES (NULL,?,?,?)", (8, 8, 0.02))
cur.execute("INSERT INTO recipe_entries VALUES (NULL,?,?,?)", (6, 8, 0.02))
cur.execute("INSERT INTO recipe_entries VALUES (NULL,?,?,?)", (4, 8, 0.02))
cur.execute("INSERT INTO recipe_entries VALUES (NULL,?,?,?)", (2, 8, 0.02))
con.commit()

# tequilla_sunrise
cur.execute("INSERT INTO cocktails VALUES (?,?,?)", (9, tequilla_sunrise.name, tequilla_sunrise.imageUrl))
cur.execute("INSERT INTO tag_entries VALUES (NULL,?,?)", (2, 9))
cur.execute("INSERT INTO tag_entries VALUES (NULL,?,?)", (6, 9))
cur.execute("INSERT INTO recipe_entries VALUES (NULL,?,?,?)", (13, 9, 0.14))
cur.execute("INSERT INTO recipe_entries VALUES (NULL,?,?,?)", (2, 9, 0.04))
cur.execute("INSERT INTO recipe_entries VALUES (NULL,?,?,?)", (9, 9, 0.02))
con.commit()

# pina_colada
cur.execute("INSERT INTO cocktails VALUES (?,?,?)", (10, pina_colada.name, pina_colada.imageUrl))
cur.execute("INSERT INTO tag_entries VALUES (NULL,?,?)", (2, 10))
cur.execute("INSERT INTO tag_entries VALUES (NULL,?,?)", (5, 10))
cur.execute("INSERT INTO tag_entries VALUES (NULL,?,?)", (7, 10))
cur.execute("INSERT INTO recipe_entries VALUES (NULL,?,?,?)", (3, 10, 0.04))
cur.execute("INSERT INTO recipe_entries VALUES (NULL,?,?,?)", (18, 10, 0.02))
cur.execute("INSERT INTO recipe_entries VALUES (NULL,?,?,?)", (8, 10, 0.02))
cur.execute("INSERT INTO recipe_entries VALUES (NULL,?,?,?)", (14, 10, 0.10))
con.commit()

# alex
cur.execute("INSERT INTO cocktails VALUES (?,?,?)", (11, alex.name, alex.imageUrl))
#cur.execute("INSERT INTO tag_entries VALUES (NULL,?,?)", (3, 11))
cur.execute("INSERT INTO tag_entries VALUES (NULL,?,?)", (6, 11))
cur.execute("INSERT INTO tag_entries VALUES (NULL,?,?)", (12, 11))
cur.execute("INSERT INTO recipe_entries VALUES (NULL,?,?,?)", (12, 11, 0.06))
cur.execute("INSERT INTO recipe_entries VALUES (NULL,?,?,?)", (14, 11, 0.06))
cur.execute("INSERT INTO recipe_entries VALUES (NULL,?,?,?)", (6, 11, 0.04))
cur.execute("INSERT INTO recipe_entries VALUES (NULL,?,?,?)", (10, 11, 0.02))
cur.execute("INSERT INTO recipe_entries VALUES (NULL,?,?,?)", (9, 11, 0.02))
con.commit()

# alexi
cur.execute("INSERT INTO cocktails VALUES (?,?,?)", (12, alexi.name, alexi.imageUrl))
#cur.execute("INSERT INTO tag_entries VALUES (NULL,?,?)", (3, 12))
cur.execute("INSERT INTO tag_entries VALUES (NULL,?,?)", (6, 12))
cur.execute("INSERT INTO tag_entries VALUES (NULL,?,?)", (12, 12))
cur.execute("INSERT INTO recipe_entries VALUES (NULL,?,?,?)", (12, 12, 0.08))
cur.execute("INSERT INTO recipe_entries VALUES (NULL,?,?,?)", (14, 12, 0.10))
cur.execute("INSERT INTO recipe_entries VALUES (NULL,?,?,?)", (10, 12, 0.02))
cur.execute("INSERT INTO recipe_entries VALUES (NULL,?,?,?)", (9, 12, 0.02))
con.commit()

# kiba
cur.execute("INSERT INTO cocktails VALUES (?,?,?)", (13, kiba.name, kiba.imageUrl))
cur.execute("INSERT INTO tag_entries VALUES (NULL,?,?)", (5, 13)),
cur.execute("INSERT INTO recipe_entries VALUES (NULL,?,?,?)", (17, 13, 0.12))
cur.execute("INSERT INTO recipe_entries VALUES (NULL,?,?,?)", (15, 13, 0.08))
con.commit()

# sweet_orange
cur.execute("INSERT INTO cocktails VALUES (?,?,?)", (14, sweet_orange.name, sweet_orange.imageUrl))
cur.execute("INSERT INTO tag_entries VALUES (NULL,?,?)", (5, 14))
cur.execute("INSERT INTO tag_entries VALUES (NULL,?,?)", (7, 14))
cur.execute("INSERT INTO recipe_entries VALUES (NULL,?,?,?)", (18, 14, 0.04))
cur.execute("INSERT INTO recipe_entries VALUES (NULL,?,?,?)", (17, 14, 0.04))
cur.execute("INSERT INTO recipe_entries VALUES (NULL,?,?,?)", (14, 14, 0.04))
cur.execute("INSERT INTO recipe_entries VALUES (NULL,?,?,?)", (13, 14, 0.08))
con.commit()

# beach_beauty
cur.execute("INSERT INTO cocktails VALUES (?,?,?)", (15, beach_beauty.name, beach_beauty.imageUrl))
cur.execute("INSERT INTO tag_entries VALUES (NULL,?,?)", (6, 15)),
cur.execute("INSERT INTO recipe_entries VALUES (NULL,?,?,?)", (11, 15, 0.10))
cur.execute("INSERT INTO recipe_entries VALUES (NULL,?,?,?)", (13, 15, 0.08))
cur.execute("INSERT INTO recipe_entries VALUES (NULL,?,?,?)", (9, 15, 0.02))
con.commit()

# vodka_o
cur.execute("INSERT INTO cocktails VALUES (?,?,?)", (16, vodka_o.name, vodka_o.imageUrl))
cur.execute("INSERT INTO tag_entries VALUES (NULL,?,?)", (1, 16)),
cur.execute("INSERT INTO recipe_entries VALUES (NULL,?,?,?)", (4, 16, 0.04))
cur.execute("INSERT INTO recipe_entries VALUES (NULL,?,?,?)", (13, 16, 0.16))
con.commit()

# licor43_o
cur.execute("INSERT INTO cocktails VALUES (?,?,?)", (17, licor43_o.name, licor43_o.imageUrl))
cur.execute("INSERT INTO tag_entries VALUES (NULL,?,?)", (1, 17))
cur.execute("INSERT INTO tag_entries VALUES (NULL,?,?)", (5, 17))
cur.execute("INSERT INTO recipe_entries VALUES (NULL,?,?,?)", (1, 17, 0.05))
cur.execute("INSERT INTO recipe_entries VALUES (NULL,?,?,?)", (13, 17, 0.15))
con.commit()

# licor43_o_sahne
cur.execute("INSERT INTO cocktails VALUES (?,?,?)", (18, licor43_o_sahne.name, licor43_o_sahne.imageUrl))
cur.execute("INSERT INTO tag_entries VALUES (NULL,?,?)", (1, 18))
cur.execute("INSERT INTO tag_entries VALUES (NULL,?,?)", (7, 18))
cur.execute("INSERT INTO recipe_entries VALUES (NULL,?,?,?)", (18, 18, 0.03))
cur.execute("INSERT INTO recipe_entries VALUES (NULL,?,?,?)", (1, 18, 0.04))
cur.execute("INSERT INTO recipe_entries VALUES (NULL,?,?,?)", (13, 18, 0.13))
con.commit()

# gin_tonic
cur.execute("INSERT INTO cocktails VALUES (?,?,?)", (19, gin_tonic.name, gin_tonic.imageUrl))
cur.execute("INSERT INTO tag_entries VALUES (NULL,?,?)", (1, 19)),
cur.execute("INSERT INTO recipe_entries VALUES (NULL,?,?,?)", (6, 19, 0.04))
cur.execute("INSERT INTO recipe_entries VALUES (NULL,?,?,?)", (11, 19, 0.12))
con.commit()
