from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/entrar', methods=['GET', 'POST'])
def entrar():
    if request.method == 'POST':
        cnpj = request.form['cnpj']
        senha = request.form['senha']
        # Adicione lógica para autenticação
        return redirect(url_for('resumo'))  # Redireciona para a tela de resumo após entrar
    return render_template('entrar.html')

@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        cnpj = request.form['cnpj']
        dados_bancarios = request.form['dados_bancarios']
        # Adicione lógica para salvar o novo usuário
        return redirect(url_for('resumo'))  # Redireciona para a tela de resumo após cadastro
    return render_template('cadastrar.html')

@app.route('/resumo')
def resumo():
    return render_template('resumo.html')  # Crie este arquivo para a tela de resumo

@app.route('/usuario')
def usuario():
    return render_template('usuario.html')  # Certifique-se de que o nome do arquivo está correto

<<<<<<< HEAD

if __name__ == '__main__':
    app.run(debug=True)
=======
@app.route('/cadastrar_jogo', methods=['GET', 'POST'])  # Nova rota para cadastrar jogos
def cadastrar_jogo():
    if request.method == 'POST':
        nome_jogo = request.form['nome_jogo']
        genero = request.form['genero']
        descricao = request.form['descricao']
        # Adicione lógica para salvar o novo jogo
        return redirect(url_for('resumo'))  # Redireciona para a tela de resumo após cadastro
    return render_template('cadastrar_jogo.html')  # Rendeiriza o formulário para cadastrar jogo

@app.route('/suporte')
def suporte():
    return render_template('suporte.html')  # Renderiza o arquivo suporte.html

@app.route('/cadastrar_pessoa', methods=['GET', 'POST'])  # Nova rota para cadastrar pessoa
def cadastrar_pessoa():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        cpf = request.form['cpf']
        rede_social = request.form['rede_social']
        telefone = request.form['telefone']
        
        # Adicione a lógica para salvar os dados da pessoa no banco de dados
        
        return redirect(url_for('resumo'))  # Redireciona para a tela de resumo após o cadastro
    return render_template('cadastrar_pessoa.html')  # Renderiza o formulário para cadastrar pessoa


if __name__ == '__main__':
    app.run(debug=True)
>>>>>>> 53582c6 (Atualiza arquivos e configurações do projeto)
