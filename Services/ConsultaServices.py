import sqlite3

conexao = sqlite3.connect('Hospital.db')

cursor = conexao.cursor()

cursor.execute(
    '''
        CREATE TABLE consultas (
            id INTEGER PRIMARY KEY,
            data_consulta DATE,
            observacoes TEXT NOT NULL,
            id_paciente INTEGER NOT NULL,
            id_medico INTEGER NOT NULL,
            FOREIGN KEY (id_paciente) REFERENCES pacientes(id),
            FOREIGN KEY (id_medico) REFERENCES medicos(id)

);
    '''
)

cursor.close()
print("Tabela CONSULTA criada com sucesso")