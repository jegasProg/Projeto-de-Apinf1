import sqlite3

db = sqlite3.connect("banco_de_dados.db")

cursor = db.cursor()

print("Base Criada")

db.close()