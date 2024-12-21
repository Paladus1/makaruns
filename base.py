import sqlite3


connection = sqlite3.connect("macarons.db")
cursor = connection.cursor()


request = """
CREATE TABLE IF NOT EXISTS macarons (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255) NOT NULL,
    flavor VARCHAR(255),
    description TEXT,
    price INTEGER,
    image VARCHAR(255)
);
"""
cursor.execute(request)


insert_request = """
INSERT INTO macarons (name, flavor, description, price, image)
VALUES (?, ?, ?, ?, ?);
"""

macarons_data = [
    ("Макарун з полуницею", "Полуниця", "Ніжний десерт з натуральним полуничним смаком.", 150, "macaron1.jpg"),
    ("Макарун з шоколадом", "Шоколад", "Насичений шоколадний смак з хрусткою скоринкою.", 160, "macaron2.jpg"),
    ("Макарун з ваніллю", "Ваніль", "Класичний макарун з легким ароматом ванілі.", 140, "macaron3.jpg"),
    ("Макарун з фісташками", "Фісташки", "Ароматний макарун з кремовою начинкою з фісташок.", 170, "macaron4.jpg"),
    ("Макарун з лимоном", "Лимон", "Свіжий лимонний смак з легкою кислинкою.", 145, "macaron5.jpg"),
]

for macaron in macarons_data:
    cursor.execute(insert_request, macaron)

connection.commit()

cursor.execute("SELECT * FROM macarons")

rows = cursor.fetchall()

for row in rows:
    print(row)

connection.close()
