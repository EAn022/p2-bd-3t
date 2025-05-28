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
    
# def excluirFuncionario(codigo):
#     try:
#         conexao = conectaBD()
#         cursor = conexao.cursor()
#         cursor.execute("DELETE FROM funcionario WHERE codigo = ?", (codigo,))
#         conexao.commit()
#         print(f"Funcionario com codigo {codigo} excluído com sucesso!")
#     except sqlite3.Error as e:
#         print(f"Erro ao excluir funcionario: {e}")
#     finally:
#         if conexao:
#             conexao.close()

# def alterarFuncionario(funcionario):
#     try:
#         conexao = conectaBD()
#         cursor = conexao.cursor()
#         cursor.execute('''
#             UPDATE funcionario 
#             SET codigo = ?, nome = ?, tipo = ?, diasTrabalhados = ?, valorDia = ?, salarioBase = ?, comissao = ?
#             WHERE codigo = ?
#         ''', (
#             funcionario["Código"],
#             funcionario["Nome"],
#             funcionario["Tipo"],
#             funcionario["Dias Trabalhados"],
#             funcionario["Valor Dia"],
#             funcionario["Salário Base"],
#             funcionario["Comissão"],
#             funcionario["Código"]
#         ))
#         conexao.commit()
#         print(f"Funcionário com código {funcionario['Código']} alterado com sucesso!")
#     except sqlite3.Error as e:
#         print(f"Erro ao alterar Funcionário: {e}")
#     finally:
#         if conexao:
#             conexao.close()