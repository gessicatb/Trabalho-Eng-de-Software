from flask import Flask, render_template, request, redirect, url_for
from models import db,Usuario,Pessoa,Jogo
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import configparser 

app = Flask(__name__)

config = configparser.ConfigParser()
config.read('database.ini')

app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{config['postgresql']['user']}:{config['postgresql']['password']}@{config['postgresql']['host']}:{config['postgresql']['port']}/{config['postgresql']['dbname']}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'sua_chave_secreta' 

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
        senha = generate_password_hash(request.form['senha'])
        cnpj = request.form['cnpj']
        dados_bancarios = request.form['dados_bancarios']
        novo_usuario = Usuario(nome=nome, email=email, senha=senha, cnpj=cnpj, dados_bancarios=dados_bancarios)
        db.session.add(novo_usuario)
        db.session.commit()
        return redirect(url_for('resumo'))  # Redireciona para a tela de resumo após cadastro
    return render_template('cadastrar.html')

@app.route('/resumo')
def resumo():
    return render_template('resumo.html')  # Crie este arquivo para a tela de resumo

@app.route('/usuario')
def usuario():
    return render_template('usuario.html')  # Certifique-se de que o nome do arquivo está correto

@app.route('/cadastrar_jogo', methods=['GET', 'POST'])  # Nova rota para cadastrar jogos
def cadastrar_jogo():
    if request.method == 'POST':
        nome_jogo = request.form['nome_jogo']
        genero = request.form['genero']
        descricao = request.form['descricao']
        # Adicione lógica para salvar o novo jogo
        return redirect(url_for('resumo'))  # Redireciona para a tela de resumo após cadastro
    return render_template('cadastrar_jogo.html')  # Renderiza o formulário para cadastrar jogo

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
