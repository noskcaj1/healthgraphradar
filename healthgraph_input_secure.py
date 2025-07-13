import streamlit as st

def login():
    st.sidebar.title("🔐 Autenticação")
    usuario = st.sidebar.text_input("Usuário")
    senha = st.sidebar.text_input("Senha", type="password")
    if st.sidebar.button("Entrar"):
        if usuario == "admin" and senha == "hgr@123":
            return True
        else:
            st.sidebar.error("Usuário ou senha inválidos.")
            return False
    return False