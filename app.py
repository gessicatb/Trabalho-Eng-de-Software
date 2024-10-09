from flask import Flask, render_template, request, redirect, url_for
from models.usuario import Usuario
from models.pessoa import Pessoa
from models.jogo import Jogo
from models.db import db
from flask_sqlalchemy import SQLAlchemy
from flask import flash
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
        
        try:
            usuario = Usuario.query.filter_by(cnpj=cnpj).first()
            if usuario and check_password_hash(usuario.senha, senha):
                return redirect(url_for('resumo'))
            flash('CNPJ ou senha incorretos', 'error')
        except Exception as e:
            print(f"Erro ao tentar logar: {e}")
            flash('Erro interno ao tentar logar.', 'error')
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
            return redirect(url_for('resumo'))
        except Exception as e:
            db.session.rollback()
            print(f"Erro ao cadastrar usuário: {e}")  # Captura o erro e exibe o detalhe no terminal
            flash('Erro ao cadastrar usuário.', 'error')

    return render_template('cadastrar.html')


@app.route('/resumo')
def resumo():
    try:
        return render_template('resumo.html')
    except Exception as e:
        print(f"Erro ao renderizar página de resumo: {e}")
        flash('Erro ao carregar o resumo.', 'error')
        return redirect(url_for('home'))


@app.route('/usuario')
def usuario():
    try:
        return render_template('usuario.html')
    except Exception as e:
        print(f"Erro ao renderizar página de usuário: {e}")
        flash('Erro ao carregar a página do usuário.', 'error')
        return redirect(url_for('home'))


@app.route('/cadastrar_jogo', methods=['GET', 'POST'])
def cadastrar_jogo():
    if request.method == 'POST':
        nome_jogo = request.form['nome_jogo']
        genero = request.form['genero']
        descricao = request.form['descricao']
        novo_jogo = Jogo(nome_jogo=nome_jogo, genero=genero, descricao=descricao)

        try:
            db.session.add(novo_jogo)
            db.session.commit()
            print("Jogo cadastrado com sucesso!")
            return redirect(url_for('resumo'))
        except Exception as e:
            db.session.rollback()
            print(f"Erro ao cadastrar jogo: {e}")
            flash('Erro ao cadastrar jogo.', 'error')

    return render_template('cadastrar_jogo.html')


@app.route('/suporte')
def suporte():
    try:
        return render_template('suporte.html')
    except Exception as e:
        print(f"Erro ao renderizar página de suporte: {e}")
        flash('Erro ao carregar a página de suporte.', 'error')
        return redirect(url_for('home'))


@app.route('/cadastrar_pessoa', methods=['GET', 'POST'])
def cadastrar_pessoa():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        cpf = request.form['cpf']
        rede_social = request.form['rede_social']
        telefone = request.form['telefone']

        nova_pessoa = Pessoa(nome=nome, email=email, cpf=cpf, rede_social=rede_social, telefone=telefone)

        try:
            db.session.add(nova_pessoa)
            db.session.commit()
            print("Pessoa cadastrada com sucesso!")
            return redirect(url_for('resumo'))
        except Exception as e:
            db.session.rollback()
            print(f"Erro ao cadastrar pessoa: {e}")
            flash('Erro ao cadastrar pessoa.', 'error')

    return render_template('cadastrar_pessoa.html')


if __name__ == '__main__':
    with app.app_context():  # Certifique-se de usar o contexto da aplicação
        db.create_all()  # Criar as tabelas, se elas ainda não existirem
    app.run(debug=True)