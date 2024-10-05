from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Rota para a tela inicial
@app.route('/')
def home():
    return render_template('index.html')

# Rota para a página de entrar
@app.route('/entrar', methods=['GET', 'POST'])
def entrar():
    if request.method == 'POST':
        usuario = request.form['usuario']
        senha = request.form['senha']
        # Aqui você pode adicionar lógica para autenticação
        return redirect(url_for('home'))  # Redireciona para a tela inicial após entrar
    return render_template('entrar.html')

# Rota para a página de cadastrar
@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    if request.method == 'POST':
        usuario = request.form['usuario']
        senha = request.form['senha']
        email = request.form['email']
        # Aqui você pode adicionar lógica para salvar o novo usuário
        return redirect(url_for('home'))  # Redireciona para a tela inicial após cadastro
    return render_template('cadastrar.html')

if __name__ == '__main__':
    app.run(debug=True)
