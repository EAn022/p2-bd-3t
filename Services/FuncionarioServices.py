import sqlite3

conexao = sqlite3.connect("Hospital.db")

cursor = conexao.cursor()

cursor.execute(
    '''
        CREATE TABLE funcionarios(
            id INTEGER NOT NULL PRIMARY KEY,
            id_pessoa NOT NULL,
            salario FLOAT NOT NULL,
            cargo TEXT NOT NULL,
            FOREIGN KEY (id_pessoa) REFERENCES pessoas(id)
        );
    '''

)

cursor.close()
print("Tabela FUNCIONARIOS criada com sucesso!")