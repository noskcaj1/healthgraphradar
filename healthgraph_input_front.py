import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import os
import datetime

def form_input():
    st.subheader("📥 Cadastro ou Atualização de Prontuário")

    with st.form("form_prontuario"):
        paciente_id = st.text_input("ID do Paciente")
        nome = st.text_input("Nome Completo")
        idade = st.number_input("Idade", min_value=0, max_value=120)
        data_nascimento = st.date_input("Data de Nascimento")
        sexo = st.selectbox("Sexo", ["Masculino", "Feminino", "Outro"])
        sintomas = st.text_area("Sintomas")
        exames = st.text_area("Exames Realizados")
        prescricao = st.text_area("Prescrição Médica")
        profissional = st.text_input("Profissional Responsável")

        submit = st.form_submit_button("Salvar ou Atualizar")

    if submit:
        DB_URL = os.getenv("DB_URL")
        engine = create_engine(DB_URL)

        with engine.begin() as conn:
            prontuario = {
                "paciente_id": paciente_id,
                "nome": nome,
                "idade": idade,
                "data_nascimento": data_nascimento.strftime('%Y-%m-%d'),
                "sexo": sexo,
                "sintomas": sintomas,
                "exames": exames,
                "prescricao": prescricao,
                "profissional": profissional,
                "data_atualizacao": datetime.datetime.now().isoformat()
            }

            conn.execute(
                """
                INSERT INTO prontuarios (paciente_id, nome, idade, data_nascimento, sexo, sintomas, exames, prescricao, profissional, data_atualizacao)
                VALUES (%(paciente_id)s, %(nome)s, %(idade)s, %(data_nascimento)s, %(sexo)s, %(sintomas)s, %(exames)s, %(prescricao)s, %(profissional)s, %(data_atualizacao)s)
                ON CONFLICT (paciente_id) DO UPDATE SET
                    nome = EXCLUDED.nome,
                    idade = EXCLUDED.idade,
                    data_nascimento = EXCLUDED.data_nascimento,
                    sexo = EXCLUDED.sexo,
                    sintomas = EXCLUDED.sintomas,
                    exames = EXCLUDED.exames,
                    prescricao = EXCLUDED.prescricao,
                    profissional = EXCLUDED.profissional,
                    data_atualizacao = EXCLUDED.data_atualizacao
                """,
                prontuario
            )

            conn.execute(
                """
                INSERT INTO auditoria_logs (paciente_id, profissional, acao, data_hora)
                VALUES (%s, %s, %s, %s)
                """,
                (paciente_id, profissional, "Atualização de prontuário", datetime.datetime.now().isoformat())
            )

        st.success("✅ Prontuário salvo ou atualizado com sucesso!")

form_input()