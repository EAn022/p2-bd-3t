import sqlite3

conexao = sqlite3.connect('Hospital.db')

cursor = conexao.cursor()

cursor.execute(
    '''
        CREATE TABLE medicos (
            id INTEGER PRIMARY KEY,
            crm TEXT NOT NULL,
            especialidade TEXT NOT NULL,
            id_funcinario INTEGER NOT NULL,
            FOREIGN KEY (id_funcionario) REFERENCES funcionarios (id)

);
    '''
)

cursor.close()
print("Tabela MÉDICO criada com sucesso")