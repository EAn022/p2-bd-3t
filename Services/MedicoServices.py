import sqlite3

conexao = sqlite3.connect('Hospital.db')

cursor = conexao.cursor()

cursor.execute(
    '''
        CREATE TABLE medicos (
            id INTEGER PRIMARY KEY,
            crm TEXT NOT NULL,
            especialidade TEXT NOT NULL,

);
    '''
)

cursor.close()
print("Tabela MÉDICO criada com sucesso")