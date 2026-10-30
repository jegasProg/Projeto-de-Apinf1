import sqlite3

db = sqlite3.connect("banco_de_dados.db")

cursor = db.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER,
    curso TEXT
)
""")

cursor.execute("""
Insert INTO usuarios (nome, idade, curso) 
VALUES (?,?,?)
""", ("João", 20, "Engenharia"))


db.commit()

cursor.execute("SELECT * FROM usuarios")
usuarios = cursor.fetchall()

for usuario in usuarios:
    print(usuario)


db.close()