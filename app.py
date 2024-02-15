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

        # Executando a página de cadastro
        exec(open("cadastro.py").read())

    st.write("")

if __name__ == "__main__":
    main()
