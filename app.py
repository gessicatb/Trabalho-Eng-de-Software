from flask import Flask, render_template, request, redirect, url_for
from models.usuario import Usuario
from models.db import db
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import configparser 


app = Flask(__name__)

config = configparser.ConfigParser()
config.read('database.ini')

app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{config['postgresql']['user']}:{config['postgresql']['password']}@{config['postgresql']['host']}:{config['postgresql']['port']}/{config['postgresql']['dbname']}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'sua_chave_secreta' 
db.init_app(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/entrar', methods=['GET', 'POST'])
def entrar():
    if request.method == 'POST':
        cnpj = request.form['cnpj']
        senha = request.form['senha']
        usuario = Usuario.query.filter_by(cnpj=cnpj).first()
        if usuario and check_password_hash(usuario.senha, senha):
            return redirect(url_for('resumo'))  
        flash('CNPJ ou senha incorretos', 'error')
    return render_template('entrar.html')

@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        senha = generate_password_hash(request.form.get('senha'))
        cnpj = request.form.get('cnpj')
        dados_bancarios = request.form.get('dados_bancarios')

        novo_usuario = Usuario(nome=nome, email=email, senha=senha, cnpj=cnpj, dados_bancarios=dados_bancarios)

        try:
            db.session.add(novo_usuario)
            db.session.commit()
            print("Usuário cadastrado com sucesso!")  
            return redirect(url_for('resumo'))  # Redirecionar após sucesso
        except Exception as e:
            db.session.rollback() 
            print(f"Erro ao cadastrar usuário: {e}")  
            # Você pode considerar renderizar um template de erro ou mostrar uma mensagem ao usuário

    return render_template('cadastrar.html')  # Retornar o formulário em caso de GET

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
