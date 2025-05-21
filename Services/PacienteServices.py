import sqlite3

conexao = sqlite3.connect("Hospital.db")

cursor = conexao.cursor()

cursor.execute(
    '''
        CREATE TABLE pacientes(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            id_pessoa NOT NULL,
            FOREIGN KEY (id_pessoa) REFERENCES pessoas(id)
        );
    '''

)

cursor.close()
print("Tabela PACIENTES criada com sucesso!")