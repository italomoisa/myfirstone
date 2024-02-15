import sys
sys.path.append("D:/Decoreba/api")
import cadastro

# Função principal
def main():
    st.title('Decoreba')
    st.caption('O seu aplicativo de revisão espaçada!')

    # Verifica se o botão "Cadastre-se" foi clicado
    cadastre_se_clicked = st.button('Cadastre-se')

    # Renderiza a página de cadastro se o botão "Cadastre-se" foi clicado
    if cadastre_se_clicked:
        # Renderiza a página de cadastro
        cadastro.render_cadastro()

    # Renderiza o botão "Cadastre-se" apenas se ainda não foi clicado
    if not cadastre_se_clicked:
        render_login()

# Função para renderizar a página de login
def render_login():
    st.write('Entre com seu CPF e senha para acessar sua conta.')
    cpf = st.text_input('CPF', key='cpf_input')  # Definindo chave única
    senha = st.text_input('Senha', type='password', key='senha_input')  # Definindo chave única
    if st.button('Entrar'):
        if autenticar_usuario(cpf, senha):
            st.success('Login bem-sucedido!')
            # Aqui você pode redirecionar para a próxima página após o login
        else:
            st.error('CPF ou senha incorretos.')

# Função para autenticar um usuário
def autenticar_usuario(CPF, senha):
    # Coloque sua lógica de autenticação aqui
    return True  # Apenas para simular uma autenticação bem-sucedida

if __name__ == '__main__':
    main()
