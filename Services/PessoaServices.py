import sqlite3

conexao = sqlite3.connect('Hospital.db')

cursor = conexao.cursor()

cursor.execute(
    '''
        CREATE TABLE pessoas(
            id INTEGER NOT NULL PRIMARY KEY,
            nome TEXT NOT NULL,
            CPF TEXT NOT NULL,  
            data_nasc DATE  
        );
    '''

)

cursor.close()
print("Tabela PESSOAS criada com sucesso")