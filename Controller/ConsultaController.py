import sqlite3
from Models.Consultas import Consulta

def conectaBD():
    conexao = sqlite3.connect("Hospital.db")
    return conexao

def incluirConsulta(consulta):
    conexao = conectaBD()
    cursor = conexao.cursor()
    try:
        cursor.execute("""
            INSERT INTO consultas (data_consulta, observacoes, id_paciente, id_medico )
            VALUES (?, ?, ?, ?)
        """, (
           consulta.get_data_consulta(),
           consulta.get_observacoes(),
           consulta.get_id_paciente(),
           consulta.get_id_medico(),
    
        ))

   
        conexao.commit()

        print("Consulta inserido com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao inserir consulta: {e}")
    finally:
        conexao.close()

def consultarConsulta():
    conexao = conectaBD()
    cursor = conexao.cursor()
    
    try:
        cursor.execute(
            '''
                SELECT c.id, c.data_consulta, c.observacoes, c.id_paciente, pp.nome, c.id_medico, pf.nome
                FROM consultas c
                JOIN medicos m ON m.id = c.id_medico
                JOIN funcionarios f ON f.id = m.id_funcionario
                JOIN pessoas pf ON pf.id = f.id_pessoa
                JOIN pacientes p ON p.id = c.id_paciente
                JOIN pessoas pp ON pp.id = p.id_pessoa;

            '''   
            )
        rows = cursor.fetchall()
        
        # Lista para armazenar os dados das consultas
        dados = []
        
        for row in rows:
            # print(row)
            id, data_consulta, observacoes, id_paciente, nome_paciente, id_medico, nome_medico = row
            # Adiciona os dados da consulta à lista
            dados.append({
                "id": id,
                "data_consulta": data_consulta,
                "observacoes": observacoes,
                "id_paciente": id_paciente,
                "nome_paciente": nome_paciente,
                "id_medico": id_medico,
                "nome_medico": nome_medico
              
            })
        return dados
    
    except sqlite3.Error as e:
        print(f"Erro ao consultar consulta: {e}")
        return []
    
    finally:
        conexao.close()
    
def excluirConsulta(id_c):
    try:
        conexao = conectaBD()
        cursor = conexao.cursor()

        cursor.execute("DELETE FROM consultas WHERE id = ?", (id_c))
        conexao.commit()
        print(f"Consulta com id {id} excluída com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao excluir consulta: {e}")
    finally:
        if conexao:
            conexao.close()

def alterarConsulta(consulta):
    try:
        conexao = conectaBD()
        cursor = conexao.cursor()

        cursor.execute("""
            UPDATE consultas
            SET data_consulta = ?, observacoes = ?,  id_paciente = ?, id_medico = ?
            WHERE id = ?;
        """, (
            consulta.get_data_consulta(),
            consulta.get_observacoes(),
            consulta.get_id_paciente(),
            consulta.get_id_medico(),
            consulta.get_id(),
        ))

        conexao.commit()
        print(f"Consulta com código {consulta.get_id()} alterado com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao alterar consulta: {e}")
    finally:
        if conexao:
            conexao.close()