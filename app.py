from flask import Flask, render_template, request, redirect, url_for, flash, session
from models.usuario import Usuario
from models.pessoa import Pessoa
from models.jogo import Jogo
from models.db import db
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
        
        if not usuario:
            flash('CNPJ não encontrado.', 'error')
            return render_template('entrar.html')

        if check_password_hash(usuario.senha, senha):
            session['usuario_id'] = usuario.id  # Armazena o ID do usuário na sessão
            flash('Login bem-sucedido!', 'success')
            return redirect(url_for('resumo'))
        
        flash('Senha incorreta', 'error')
    return render_template('entrar.html')


@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        senha = generate_password_hash(request.form.get('senha'))
        cnpj = request.form.get('cnpj')
        dados_bancarios = request.form.get('dados_bancarios')

        # Verificar se o e-mail ou CNPJ já estão cadastrados
        if Usuario.query.filter((Usuario.email == email) | (Usuario.cnpj == cnpj)).first():
            flash('E-mail ou CNPJ já cadastrados.', 'error')
            return render_template('cadastrar.html')

        novo_usuario = Usuario(nome=nome, email=email, senha=senha, cnpj=cnpj, dados_bancarios=dados_bancarios)

        try:
            db.session.add(novo_usuario)
            db.session.commit()
            flash('Usuário cadastrado com sucesso!', 'success')

            # Logar automaticamente o usuário
            session['usuario_id'] = novo_usuario.id  # Armazena o ID do novo usuário na sessão
            
            return redirect(url_for('resumo'))  # Redireciona para a página de resumo
        except Exception as e:
            db.session.rollback()
            flash(f"Erro ao cadastrar usuário: {e}", 'error')
            return render_template('cadastrar.html')

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


@app.route('/suporte')
def suporte():
    # Acessível por qualquer usuário logado
    return render_template('suporte.html')


@app.route('/cadastrar_jogo', methods=['GET', 'POST'])
def cadastrar_jogo():
    if 'usuario_id' not in session:
        flash('Você precisa estar logado para cadastrar um jogo.', 'error')
        return redirect(url_for('entrar'))

    if request.method == 'POST':
        nome_jogo = request.form['nome_jogo']
        genero = request.form['genero']
        descricao = request.form['descricao']
        usuario_id = session['usuario_id']  # Obtém o ID do usuário logado

        novo_jogo = Jogo(nome_jogo=nome_jogo, genero=genero, descricao=descricao, usuario_id=usuario_id)

        try:
            db.session.add(novo_jogo)
            db.session.commit()
            flash('Jogo cadastrado com sucesso!', 'success')
            return redirect(url_for('meus+jogos'))
        except Exception as e:
            db.session.rollback()
            print(f"Erro ao cadastrar jogo: {e}")  # Adicionando um print para visualizar o erro no terminal
            flash(f'Erro ao cadastrar jogo: {str(e)}', 'error')  # Mensagem de erro com detalhes

    return render_template('cadastrar_jogo.html')

@app.route('/cadastrar_pessoa', methods=['GET', 'POST'])
def cadastrar_pessoa():
    if 'usuario_id' not in session:
        flash('Você precisa estar logado para cadastrar uma pessoa.', 'error')
        return redirect(url_for('entrar'))

    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        cpf = request.form['cpf']
        rede_social = request.form['rede_social']
        telefone = request.form['telefone']
        usuario_id = session['usuario_id']

        print(f"Cadastrando pessoa: {nome}, {email}, {cpf}, {rede_social}, {telefone}, {usuario_id}")

        nova_pessoa = Pessoa(nome=nome, email=email, cpf=cpf, rede_social=rede_social, telefone=telefone, usuario_id=usuario_id)

        try:
            db.session.add(nova_pessoa)
            db.session.commit()
            flash('Pessoa cadastrada com sucesso!', 'success')
            return redirect(url_for('minhas_pessoas'))
        except Exception as e:
            db.session.rollback()
            print(f"Erro ao cadastrar pessoa: {e}")
            flash(f'Erro ao cadastrar pessoa: {str(e)}', 'error')

    return render_template('cadastrar_pessoa.html')

@app.route('/meus_jogos')
def meus_jogos():
    if 'usuario_id' not in session:
        flash('Você precisa estar logado para acessar seus jogos.', 'error')
        return redirect(url_for('entrar'))

    usuario_id = session['usuario_id']
    jogos = Jogo.query.filter_by(usuario_id=usuario_id).all()

    return render_template('meus_jogos.html', jogos=jogos)

@app.route('/minhas_pessoas')
def minhas_pessoas():
    if 'usuario_id' not in session:
        flash('Você precisa estar logado para acessar suas pessoas.', 'error')
        return redirect(url_for('entrar'))

    usuario_id = session['usuario_id']
    pessoas = Pessoa.query.filter_by(usuario_id=usuario_id).all()

    return render_template('minhas_pessoas.html', pessoas=pessoas)


if __name__ == '__main__':
    with app.app_context():  # Certifique-se de usar o contexto da aplicação
        db.create_all()  # Criar as tabelas, se elas ainda não existirem
    app.run(debug=True)
    


