import sqlite3
import streamlit as st
import pandas as pd
import Controller.MedicoController as medicoController
from Models.Medicos import Medico

def show_medicos_page():
    st.title('Cadastro de Médicos')

    # Menu de operações para Funcionário
    Page_Medico = st.sidebar.selectbox("Operações", ["Incluir", "Consultar", "Excluir", "Alterar"])

    if Page_Medico == "Incluir":   
        # Criar instâncias de medico, funcionario e pessoa
        medico = Medico(id="", id_funcionario="",  id_pessoa="", salario=0, cargo="", nome="", CPF="", data_nasc="", crm="", especialidade="")

        # Usar setters
        medico.set_nome(st.text_input("Digite seu nome: "))
        medico.set_cpf(st.text_input("Digite seu cpf: "))
        medico.set_data_nasc(st.text_input("Digite a data de nascimento (DD/MM/YYYY)"))
        medico.set_cargo(st.text_input("Digite seu cargo"))
        medico.set_crm(st.text_input("Digite seu CRM"))
        medico.set_especialidade(st.text_input("Digite sua especialidade"))
        medico.set_salario(st.number_input("Digite seu salário", min_value=0.0, format="%.2f"))

        # Botão para inserir
        if st.button("Inserir"):
            medicoController.incluirMedico(medico)
            st.success("Medico adicionado com sucesso!")


    elif Page_Medico == "Consultar":
        if st.button("Consultar"):
            dados = medicoController.consultarMedico()
        
            if dados:           
                tb = pd.DataFrame(dados, columns=["id", "nome", "cargo", "crm","especialidade", "salario", "cpf", "data_nasc"]) 
                st.header("Lista de Médicos")
                st.dataframe(tb, width=1000)

            else:
                st.info("Nenhum Funcionário cadastrado.")


    elif Page_Medico == "Excluir":
        st.subheader("Excluir Medico")
        dados = medicoController.consultarMedico()

        if dados:
            df = pd.DataFrame(dados, columns=["id", "nome", "cargo", "crm","especialidade", "salario", "cpf", "data_nasc"])
            st.table(df)

            id = st.number_input("Digite o código do médico que deseja excluir", min_value=1, step=1)
            id = str(id)
            if st.button("Excluir"):
                try:
                    medicoController.excluirMedico(id)
                    st.success(f"Funcionário com código {id} excluído com sucesso!")
                    st.rerun()
                except Exception as e:
                    st.error(f"Erro ao excluir médico: {e}")
        else:
            st.info("Nenhum médico cadastrado.")


    elif Page_Medico == "Alterar":
        st.subheader("Alterar Médico")
        dados = medicoController.consultarMedico()

        if dados:
            df = pd.DataFrame(dados, columns=["id", "nome", "cargo", "crm","especialidade", "salario", "cpf", "data_nasc"])
            st.table(df)

            id_alterar = st.number_input("Digite o código do funcionário que deseja alterar", min_value=0, step=1)

            try:
                conexao = medicoController.conectaBD()
                cursor = conexao.cursor()

                cursor.execute(
                ''' 
                    SELECT m.id, m.crm, m.especialidade, f.salario, f.cargo, p.nome, p.CPF, p.data_nasc
                    FROM medicos m
                    JOIN funcionarios f ON m.id_funcionario = f.id
                    JOIN pessoas p ON  f.id_pessoa = p.id
                    WHERE m.id = ?;
                ''',   
                (str(id_alterar),))

                resultado = cursor.fetchone()

                if not resultado:
                    st.error("Médico não encontrado.")
                else:
                    id, crm, especialidade, salario, cargo, nome, cpf, data_nasc = resultado

                    with st.form(key="form_alterar_medico"):
                        nome = st.text_input("Nome", value=nome)
                        cpf = st.text_input("CPF", value=cpf)
                        data_nasc = st.text_input("Data de nascimento (DD/MM/YYYY)", value=data_nasc)
                        cargo = st.text_input("Cargo", value=cargo)
                        crm = st.text_input("CRM", value=crm)
                        especialidade = st.text_input("Especialidade", value=especialidade)
                        salario = st.number_input("Salário", value=float(salario), format="%.2f")

                        if st.form_submit_button("Salvar Alterações"):
                            medico_atualizado = Medico(
                                id=id,
                                id_funcionario="",
                                id_pessoa="",
                                nome=nome,
                                CPF=cpf,
                                data_nasc=data_nasc,
                                cargo=cargo,
                                crm=crm,
                                especialidade=especialidade,
                                salario=salario
                            )

                            try:
                                medicoController.alterarMedico(medico_atualizado)
                                st.success("Médico alterado com sucesso!")
                                st.rerun()
                            except Exception as e:
                                st.error(f"Erro ao alterar médico: {e}")

            except sqlite3.Error as e:
                st.error(f"Erro ao encontrar médico: {e}")
            finally:
                if conexao:
                    conexao.close()
        else:
            st.info("Nenhum médico cadastrado.")
