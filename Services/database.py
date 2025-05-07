#Sevices/database.py
import sqlite3

server = ''
username = ''
password = ''
database = 'Hospital.db'
conexao = sqlite3.connect(database)
print("Banco de dados Hospital criado com sucesso!")