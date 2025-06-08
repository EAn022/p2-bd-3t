import sqlite3
from Models.Pacientes import Paciente

def conectaBD():
    conexao = sqlite3.connect("Hospital.db")
    return conexao

def incluirPaciente(paciente):
    conexao = conectaBD()
    cursor = conexao.cursor()
    try:
        cursor.execute("""
            INSERT INTO pessoas (nome, CPF, data_nasc)
            VALUES (?, ?, ?)
        """, (
            paciente.get_nome(),
            paciente.get_cpf(),
            paciente.get_data_nasc()
        ))

        id_pessoa = cursor.lastrowid

        cursor.execute("""
            INSERT INTO pacientes (id_pessoa)
            VALUES (?)
        """, (id_pessoa,))


        conexao.commit()

        print("Paciente inserido com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao inserir paciente: {e}")
    finally:
        conexao.close()

def consultarPaciente():
    conexao = conectaBD()
    cursor = conexao.cursor()
    
    try:
        cursor.execute(
            '''
                SELECT pa.id, p.nome, p.CPF, p.data_nasc
                FROM pacientes pa
                JOIN pessoas p ON pa.id_pessoa = p.id;
            '''   
            )
        rows = cursor.fetchall()
    
        dados = []
        
        for row in rows:
            id, nome, cpf, data_nasc = row
            dados.append({
                "id": id,
                "nome": nome,
                "cpf": cpf,
                "data_nasc": data_nasc
            })
        return dados
    
    except sqlite3.Error as e:
        print(f"Erro ao consultar pacientes: {e}")
        return []
    
    finally:
        conexao.close()
    
def excluirPaciente(id_pa):
    try:
        conexao = conectaBD()
        cursor = conexao.cursor()

        try:
            # Buscar o id da pessoa correspondente ao paciente
            cursor.execute(
                '''
                    SELECT p.id 
                    FROM pacientes pa
                    JOIN pessoas p ON pa.id_pessoa = p.id
                    WHERE pa.id = ?;
                ''', (id_pa) 
            )
            row = cursor.fetchone()  

            id_p = row[0]  # Pegar o valor do id da tupla

        except sqlite3.Error as e:
            print(f"Erro ao consultar paciente: {e}")
            return  # Interrompe se falhar na consulta

        # Excluir nas duas tabelas
        cursor.execute("DELETE FROM pacientes WHERE id = ?", (id_pa,))
        cursor.execute("DELETE FROM pessoas WHERE id = ?", (id_p,))
        conexao.commit()

        print(f"Paciente com id {id_pa} excluído com sucesso!")

    except sqlite3.Error as e:
        print(f"Erro ao excluir paciente: {e}")
    finally:
        if conexao:
            conexao.close()


def alterarPaciente(paciente):
    try:
        conexao = conectaBD()
        cursor = conexao.cursor()
        
        # Consulta para pegar o ID da pessoa vinculada ao paciente
        cursor.execute("""
            SELECT p.id 
            FROM pacientes pa
            JOIN pessoas p ON pa.id_pessoa = p.id
            WHERE pa.id = ?;
        """, (paciente.get_id(),))
        
        resultado = cursor.fetchone()

        if not resultado:
            print("Paciente não encontrado.")
            return

        id_pessoa = resultado[0]  

        # Atualiza os dados na tabela pessoas
        cursor.execute("""
            UPDATE pessoas
            SET nome = ?, CPF = ?, data_nasc = ?
            WHERE id = ?;
        """, (
            paciente.get_nome(),
            paciente.get_cpf(),
            paciente.get_data_nasc(),
            id_pessoa
        ))

        conexao.commit()
        print(f"Paciente com código {paciente.get_id()} alterado com sucesso!")

    except sqlite3.Error as e:
        print(f"Erro ao alterar paciente: {e}")
    finally:
        if conexao:
            conexao.close()
