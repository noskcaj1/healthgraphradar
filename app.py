import streamlit as st
from healthgraph_app_multi import render_paginas
from healthgraph_input_secure import login

st.set_page_config(page_title="HealthGraph Radar", layout="wide", initial_sidebar_state="expanded")

# ✅ Inicializa a sessão
if "logado" not in st.session_state:
    st.session_state["logado"] = False

# ✅ Exibe tela de login se necessário
if not st.session_state["logado"]:
    st.session_state["logado"] = login()

# ✅ Renderiza app se logado
if st.session_state["logado"]:
    render_paginas()
