import sqlite3

conexao = sqlite3.connect('Hospital.db')

cursor = conexao.cursor()

cursor.execute(
    '''
        CREATE TABLE medicos(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            id_funcionario INTEGER NOT NULL,
            crm TEXT NOT NULL,
            especialidade TEXT NOT NULL,  
            FOREIGN KEY (id_funcionario) REFERENCES funcionarios(id)
        );
    '''

)

cursor.close()
print("Tabela MEDICOS criada com sucesso")
