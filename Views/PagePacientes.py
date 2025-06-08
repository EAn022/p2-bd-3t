import sqlite3
import streamlit as st
import pandas as pd
import Controller.PacienteController as pacienteController
from Models.Pacientes import Paciente

def show_pacientes_page():
    st.title('Cadastro de Pacientes')

    # Menu de operações para Funcionário
    Page_Paciente = st.sidebar.selectbox("Operações", ["Incluir", "Consultar", "Excluir", "Alterar"])

    if Page_Paciente == "Incluir":   
        paciente = Paciente(id="",  id_pessoa="", nome="", CPF="", data_nasc="")

        # Usar setters
        paciente.set_nome(st.text_input("Digite seu nome: "))
        paciente.set_cpf(st.text_input("Digite seu cpf: "))
        paciente.set_data_nasc(st.text_input("Digite a data de nascimento (DD/MM/YYYY)"))

        # Botão para inserir
        if st.button("Inserir"):
            pacienteController.incluirPaciente(paciente)
            st.success("Paciente adicionado com sucesso!")


    elif Page_Paciente == "Consultar":
        if st.button("Consultar"):
            dados = pacienteController.consultarPaciente()
        
            if dados:           
                tb = pd.DataFrame(dados, columns=["id", "nome", "cpf", "data_nasc"]) 
                st.header("Lista de Pacientes")
                st.dataframe(tb, width=1000)

            else:
                st.info("Nenhum Funcionário cadastrado.")


    elif Page_Paciente == "Excluir":
        st.subheader("Excluir paciente")
        dados = pacienteController.consultarPaciente()

        if dados:
            df = pd.DataFrame(dados, columns=["id", "nome", "cpf", "data_nasc"])
            st.table(df)

            id = st.number_input("Digite o código do paciente que deseja excluir", min_value=1, step=1)
            id = str(id)
            if st.button("Excluir"):
                try:
                    pacienteController.excluirPaciente(id)
                    st.success(f"Paciente com código {id} excluído com sucesso!")
                    st.rerun()
                except Exception as e:
                    st.error(f"Erro ao excluir paciente: {e}")
        else:
            st.info("Nenhum paciente cadastrado.")


    elif Page_Paciente == "Alterar":
        st.subheader("Alterar Paciente")
        dados = pacienteController.consultarPaciente()

        if dados:
            df = pd.DataFrame(dados, columns=["id", "nome", "cpf", "data_nasc"])
            st.table(df)

            id_alterar = st.number_input("Digite o código do funcionário que deseja alterar", min_value=0, step=1)

            try:
                conexao = pacienteController.conectaBD()
                cursor = conexao.cursor()

                cursor.execute(
                ''' 
                    SELECT pa.id, p.nome, p.CPF, p.data_nasc 
                    FROM pacientes pa
                    JOIN pessoas p ON pa.id_pessoa = p.id
                    WHERE pa.id = ?;
                ''',   
                (str(id_alterar),))

                resultado = cursor.fetchone()

                if not resultado:
                    st.error("Paciente não encontrado.")
                else:
                    id, nome, cpf, data_nasc = resultado

                    with st.form(key="form_alterar_paciente"):
                        nome = st.text_input("Nome", value=nome)
                        cpf = st.text_input("CPF", value=cpf)
                        data_nasc = st.text_input("Data de nascimento (DD/MM/YYYY)", value=data_nasc)

                        if st.form_submit_button("Salvar Alterações"):
                            paciente_atualizado = Paciente(
                                id=id,
                                id_pessoa="",
                                nome=nome,
                                CPF=cpf,
                                data_nasc=data_nasc
                            )

                            try:
                                pacienteController.alterarPaciente(paciente_atualizado)
                                st.success("Paciente alterado com sucesso!")
                                st.rerun()
                            except Exception as e:
                                st.error(f"Erro ao alterar paciente: {e}")

            except sqlite3.Error as e:
                st.error(f"Erro ao encontrar paciente: {e}")
            finally:
                if conexao:
                    conexao.close()
        else:
            st.info("Nenhum paciente cadastrado.")
