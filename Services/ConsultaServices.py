import sqlite3

conexao = sqlite3.connect('Hospital.db')

cursor = conexao.cursor()

cursor.execute(
    '''
        CREATE TABLE consultas (
            id INTEGER PRIMARY KEY,
            data_consulta DATE,
            observacoes TEXT NOT NULL,

);
    '''
)

cursor.close()
print("Tabela CONSULTA criada com sucesso")