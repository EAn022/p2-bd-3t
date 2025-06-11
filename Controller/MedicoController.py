import sqlite3
from Models.Medicos import Medico

def conectaBD():
    conexao = sqlite3.connect("Hospital.db")
    return conexao

def incluirMedico(medico):
    conexao = conectaBD()
    cursor = conexao.cursor()
    try:
        cursor.execute("""
            INSERT INTO pessoas (nome, CPF, data_nasc)
            VALUES (?, ?, ?)
        """, (
            medico.get_nome(),
            medico.get_cpf(),
            medico.get_data_nasc()
        ))

        id_pessoa = cursor.lastrowid

        cursor.execute("""
            INSERT INTO funcionarios (id_pessoa, salario, cargo)
            VALUES (?, ?, ?)
        """, (
            id_pessoa,
            medico.get_salario(),
            medico.get_cargo()
        ))

        id_funcionario = cursor.lastrowid

        cursor.execute("""
            INSERT INTO medicos (id_funcionario, crm, especialidade)
            VALUES (?, ?, ?)
        """, (
            id_funcionario,
            medico.get_crm(),
            medico.get_especialidade()
        ))
   
        conexao.commit()

        print("Médico inserido com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao inserir médico: {e}")
    finally:
        conexao.close()

def consultarMedico():
    conexao = conectaBD()
    cursor = conexao.cursor()
    
    try:
        cursor.execute(
            '''
                SELECT m.id, m.crm, m.especialidade, f.salario, f.cargo, p.nome, p.CPF, p.data_nasc
                FROM medicos m
                JOIN funcionarios f ON m.id_funcionario = f.id
                JOIN pessoas p ON  f.id_pessoa = p.id;
            '''   
            )
        rows = cursor.fetchall()
        
        # Lista para armazenar os dados dos funcionários
        dados = []
        
        for row in rows:
            # print(row)
            id, crm, especialidade, salario, cargo, nome, cpf, data_nasc = row
            # Adiciona os dados do funcionário à lista
            dados.append({
                "id": id,
                "crm": crm,
                "especialidade": especialidade,
                "salario": salario,
                "cargo": cargo,
                "nome": nome,
                "cpf": cpf,
                "data_nasc": data_nasc
            })
        return dados
    
    except sqlite3.Error as e:
        print(f"Erro ao consultar médicos: {e}")
        return []
    
    finally:
        conexao.close()
    
def excluirMedico(id_m):
    try:
        conexao = conectaBD()
        cursor = conexao.cursor()

        try:
            cursor.execute(
                '''
                    SELECT f.id, p.id 
                    FROM medicos m
                    JOIN funcionarios f ON m.id_funcionario = f.id
                    JOIN pessoas p ON  f.id_pessoa = p.id
                    WHERE m.id = ?;
                ''', (id_m,)   
                )
            rows = cursor.fetchall()       

            for row in rows:
                id_f, id_p = row
            
            id_f = str(id_f)
            id_p = str(id_p)

        except sqlite3.Error as e:
            print(f"Erro ao consultar médicos: {e}")


        cursor.execute("DELETE FROM medicos WHERE id = ?", (id_m,))
        cursor.execute("DELETE FROM funcionarios WHERE id = ?", (id_f,))
        cursor.execute("DELETE FROM pessoas WHERE id = ?", (id_p,))
        conexao.commit()
        print(f"Medico com id {id} excluído com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao excluir medico: {e}")
    finally:
        if conexao:
            conexao.close()

def alterarMedico(medico):
    try:
        conexao = conectaBD()
        cursor = conexao.cursor()
        
        # Consulta para pegar os IDs necessários
        cursor.execute("""
            SELECT f.id, p.id
            FROM medicos m
            JOIN funcionarios f ON m.id_funcionario = f.id
            JOIN pessoas p ON f.id_pessoa = p.id
            WHERE m.id = ?;
        """, 
        (medico.get_id(),))
        resultado = cursor.fetchone()

        # Verifica se os ids foram retornados
        if not resultado:
            print("Médico não encontrado.")
            return

        # Armazena os ids em variaveis distintas
        id_funcionario, id_pessoa = resultado

        cursor.execute("""
            UPDATE medicos
            SET crm = ?, especialidade = ?
            WHERE id = ?;
        """, (
            medico.get_crm(),
            medico.get_especialidade(),
            medico.get_id()
        ))

        cursor.execute("""
            UPDATE funcionarios
            SET salario = ?, cargo = ?
            WHERE id = ?;
        """, (
            medico.get_salario(),
            medico.get_cargo(),
            id_funcionario
        ))

        cursor.execute("""
            UPDATE pessoas
            SET nome = ?, CPF = ?, data_nasc = ?
            WHERE id = ?;
        """, (
            medico.get_nome(),
            medico.get_cpf(),
            medico.get_data_nasc(),
            id_pessoa
        ))

        conexao.commit()
        print(f"Médico com código {medico.get_id()} alterado com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao alterar médico: {e}")
    finally:
        if conexao:
            conexao.close()