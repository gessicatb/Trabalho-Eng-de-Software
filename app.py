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


if __name__ == '__main__':
    app.run(debug=True)