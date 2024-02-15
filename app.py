import streamlit as st
import sqlite3

# Função para autenticar o usuário com base no CPF e senha
def autenticar_usuario(cpf, senha):
    conn = sqlite3.connect('D:/Decoreba/data/decoreba.db')
    c = conn.cursor()
    c.execute("SELECT * FROM usuarios WHERE CPF = ? AND senha = ?", (cpf, senha))
    usuario = c.fetchone()
    conn.close()
    return usuario

# Função para criar um novo usuário
def cadastrar_usuario(nome, cpf, periodo_medicina, senha):
    conn = sqlite3.connect('D:/Decoreba/data/decoreba.db')
    c = conn.cursor()
    c.execute("INSERT INTO usuarios (nome, CPF, periodo_medicina, senha) VALUES (?, ?, ?, ?)", (nome, cpf, periodo_medicina, senha))
    conn.commit()
    conn.close()

# Função principal para a interface de usuário
def main():
    st.title("Acesso ao Decoreba")

    # Página de login
    if "pagina" not in st.session_state:
        st.session_state.pagina = "login"

    if st.session_state.pagina == "login":
        st.header("Login")

        cpf = st.text_input("CPF")
        senha = st.text_input("Senha", type="password")

        if st.button("Entrar"):
            usuario = autenticar_usuario(cpf, senha)
            if usuario:
                st.success(f"Bem-vindo, {usuario[1]}!")
                # Adicione aqui a lógica para redirecionar para a página principal após o login
            else:
                st.error("CPF ou senha incorretos. Por favor, tente novamente.")

        st.markdown("Não possui uma conta? [Cadastre-se aqui](#cadastrar)")

    # Página de cadastro
    elif st.session_state.pagina == "cadastrar":
        st.header("Cadastro")

        nome = st.text_input("Nome")
        cpf = st.text_input("CPF")
        periodo_medicina = st.selectbox("Período de Medicina", ["1º período", "2º período", "3º período", "4º período", "5º período", "6º período", "7º período", "8º período", "9º período", "10º período"])
        senha = st.text_input("Senha", type="password")

        if st.button("Cadastrar"):
            cadastrar_usuario(nome, cpf, periodo_medicina, senha)
            st.success("Usuário cadastrado com sucesso!")
            st.session_state.pagina = "login"

    st.write("")

if __name__ == "__main__":
    main()
