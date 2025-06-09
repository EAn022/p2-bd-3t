import sqlite3
import streamlit as st
import pandas as pd
import Controller.ConsultaController as ConsultaController
from Models.Consultas import Consulta

def show_consultas_page():
    st.title('Cadastro de Consultas')

    # Menu de operações para Funcionário
    Page_Consulta = st.sidebar.selectbox("Operações", ["Incluir", "Consultar", "Excluir", "Alterar"])

    if Page_Consulta == "Incluir":   
        consulta = Consulta(id="", id_paciente="",  id_medico="", data_consulta="", observacoes="")

        # Usar setters
        consulta.set_id_medico(st.number_input("Digite o código do médico", min_value=1, step=1))
        consulta.set_id_paciente(st.number_input("Digite o código do paciente", min_value=1, step=1))
        consulta.set_data_consulta(st.text_input("Digite a data da consulta (DD/MM/YYYY):"))
        consulta.set_observacoes(st.text_input("Digite as observações: "))
     
        # Botão para inserir
        if st.button("Inserir"):
            ConsultaController.incluirConsulta(consulta)
            st.success("Consulta adicionada com sucesso!")


    elif Page_Consulta == "Consultar":
        if st.button("Consultar"):
            dados = ConsultaController.consultarConsulta()

            if dados:           
                tb = pd.DataFrame(dados, columns=["id", "id_paciente", "nome_paciente", "id_medico", "nome_medico", "data_consulta", "observacoes"]) 
                st.header("Lista de Consultas")
                st.dataframe(tb, width=1000)

            else:
                st.info("Nenhuma Consulta cadastrado.")


    elif Page_Consulta == "Excluir":
        st.subheader("Excluir Consulta")
        dados = ConsultaController.consultarConsulta()

        if dados:
            df = pd.DataFrame(dados, columns=["id", "id_paciente", "nome_paciente", "id_medico", "nome_medico", "data_consulta", "observacoes"]) 
            st.table(df)

            id = st.number_input("Digite o código da consulta que deseja excluir", min_value=1, step=1)
            id = str(id)
            if st.button("Excluir"):
                try:
                    ConsultaController.excluirConsulta(id)
                    st.success(f"Consulta com código {id} excluída com sucesso!")
                    st.rerun()
                except Exception as e:
                    st.error(f"Erro ao excluir consulta: {e}")
        else:
            st.info("Nenhuma consulta cadastrado.")


    elif Page_Consulta == "Alterar":
        st.subheader("Alterar consulta")
        dados = ConsultaController.consultarConsulta()
        
        if dados:
            df = pd.DataFrame(dados, columns=["id", "id_paciente", "nome_paciente", "id_medico", "nome_medico", "data_consulta", "observacoes"]) 
            st.table(df)

            id_alterar = st.number_input("Digite o código do consulta que deseja alterar", min_value=0, step=1)

            try:
                conexao = ConsultaController.conectaBD()
                cursor = conexao.cursor()

                cursor.execute(
                ''' 
                    SELECT c.id, c.data_consulta, c.observacoes, c.id_paciente, pp.nome, c.id_medico, pf.nome
                    FROM consultas c
                    JOIN medicos m ON m.id = c.id_medico
                    JOIN funcionarios f ON f.id = m.id_funcionario
                    JOIN pessoas pf ON pf.id = f.id_pessoa
                    JOIN pacientes p ON p.id = c.id_paciente
                    JOIN pessoas pp ON pp.id = p.id_pessoa
                    WHERE c.id = ?;
                ''',   
                (str(id_alterar),))

                resultado = cursor.fetchone()
                print(resultado)

                if not resultado:
                    st.error("Consulta não encontrada.")
                else:
                    id, data_consulta, observacoes, id_paciente, nome_paciente, id_medico, nome_medico = resultado

                    with st.form(key="form_alterar_consulta"):
                        id_medico = st.number_input("Digite o código do médico", value=id_medico)
                        id_paciente = st.number_input("Digite o código do paciente", value=id_paciente)
                        data_consulta = st.text_input("Digite a data da consulta (DD/MM/YYYY):", value=data_consulta)
                        observacoes = st.text_input("Digite as observações: ", value=observacoes)

                        if st.form_submit_button("Salvar Alterações"):
                            consulta_atualizada = Consulta(
                                id=id,
                                id_paciente=id_paciente,
                                id_medico=id_medico,
                                data_consulta=data_consulta,
                                observacoes=observacoes
                                )

                            try:
                                ConsultaController.alterarConsulta(consulta_atualizada)
                                st.success("Consulta alterada com sucesso!")
                                st.rerun()
                            except Exception as e:
                                st.error(f"Erro ao alterar consulta: {e}")

            except sqlite3.Error as e:
                st.error(f"Erro ao encontrar consulta: {e}")
            finally:
                if conexao:
                    conexao.close()
        else:
            st.info("Nenhuma consulta cadastrada.")
