# HealthGraph Radar

Sistema de monitoramento em tempo real da qualidade de dados clínicos.

## Funcionalidades

- Cadastro e atualização de prontuários
- Painel interativo com gráficos
- Atualizações em tempo real a cada 3 segundos
- Auditoria de alterações
- Autenticação de usuários

## Executar Localmente

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy na Nuvem

1. Suba este projeto no GitHub
2. Acesse [https://share.streamlit.io](https://share.streamlit.io)
3. Conecte ao repositório e configure `app.py` como arquivo inicial
4. Configure as variáveis no painel `.streamlit/secrets.toml`

## Banco de Dados

Usa Supabase (PostgreSQL) como backend.

## Variáveis de Ambiente

`.streamlit/secrets.toml`:

```toml
DB_URL = "postgresql://usuario:senha@host:5432/postgres"
```