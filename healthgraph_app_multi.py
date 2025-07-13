import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import os
import plotly.express as px

def carregar_dados():
    engine = create_engine(os.getenv("DB_URL"))
    df = pd.read_sql("SELECT * FROM prontuarios", con=engine)
    return df

def render_dashboard():
    st.subheader("📊 Painel de Análise de Dados Clínicos")
    df = carregar_dados()

    st.dataframe(df, use_container_width=True)

    if not df.empty:
        col1, col2 = st.columns(2)

        with col1:
            fig = px.histogram(df, x="idade", title="Distribuição de Idades")
            st.plotly_chart(fig, use_container_width=True)

        with col2:
            fig2 = px.pie(df, names="sexo", title="Distribuição por Sexo")
            st.plotly_chart(fig2, use_container_width=True)

def render_paginas():
    menu = ["📥 Cadastro", "📊 Análise"]
    escolha = st.sidebar.radio("Menu", menu)

    if escolha == "📥 Cadastro":
        import healthgraph_input_front
    elif escolha == "📊 Análise":
        render_dashboard()