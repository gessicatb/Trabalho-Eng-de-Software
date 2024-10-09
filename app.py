
import configparser
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_babel import Babel, format_date  # Certifique-se de importar Babel e format_date
from models.usuario import Usuario
from models.pessoa import Pessoa
from models.jogo import Jogo
from models.ganho import Ganho
from models.db import db
from datetime import datetime
from sqlalchemy import extract
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

app.config['BABEL_DEFAULT_LOCALE'] = 'pt_BR'  # Alterado para pt_BR
babel = Babel(app)  # Inicializa o Babel

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



from sqlalchemy import func
from babel.dates import format_date


from babel.dates import format_date
from sqlalchemy import func

from sqlalchemy import extract
from babel.dates import format_date

@app.route('/resumo')
def resumo():
    # Verifica se o usuário está logado
    if 'usuario_id' not in session:
        flash('Você precisa estar logado para acessar o resumo.', 'error')
        return redirect(url_for('entrar'))

    usuario_id = session['usuario_id']

    # Obtém o mês atual em português
    mes_atual_pt = format_date(datetime.now(), format='MMMM', locale='pt_BR')

    # Obter os ganhos do mês atual usando o campo 'data'
    ganhos_mes = db.session.query(Ganho).filter(
        Ganho.usuario_id == usuario_id,
        extract('month', Ganho.data) == datetime.now().month,
        extract('year', Ganho.data) == datetime.now().year
    ).all()

    # Obter todos os ganhos do usuário
    ganhos_totais = db.session.query(Ganho).filter(
        Ganho.usuario_id == usuario_id
    ).all()

    # Calcular as somas
    total_ganhos_mes = sum(ganho.valor for ganho in ganhos_mes) or 0
    total_ganhos = sum(ganho.valor for ganho in ganhos_totais) or 0

    return render_template(
        'resumo.html',
        mes=mes_atual_pt,
        total_ganhos_mes=total_ganhos_mes,
        total_ganhos=total_ganhos
    )



@app.route('/usuario')
def usuario():
    if 'usuario_id' not in session:
        flash('Você precisa estar logado para acessar seu perfil.', 'error')
        return redirect(url_for('entrar'))  # Redireciona para a página de login se não estiver logado

    usuario_id = session['usuario_id']  # Obtém o ID do usuário logado
    usuario = Usuario.query.get(usuario_id)  # Obtém o usuário logado
    ganhos = Ganho.query.filter_by(usuario_id=usuario_id).all()  # Obtém os ganhos do usuário logado
    
    try:
        return render_template('usuario.html', usuario=usuario, ganhos=ganhos) 
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

@app.route('/adicionar_ganho', methods=['GET', 'POST'])
def adicionar_ganho():
    # Verifica se o usuário está logado
    if 'usuario_id' not in session:
        flash('Você precisa estar logado para adicionar um ganho.', 'error')
        return redirect(url_for('entrar'))

    if request.method == 'POST':
        valor = request.form.get('valor')
        descricao = request.form.get('descricao')
        usuario_id = session['usuario_id']

        # Obtém a data atual
        data_atual = datetime.now()

        # Obtém o mês atual em português
        mes_atual = format_date(data_atual, format='MMMM', locale='pt_BR').lower()

        # Criar um novo ganho
        novo_ganho = Ganho(
            valor=valor,
            descricao=descricao,
            data=data_atual,
            mes=mes_atual,
            usuario_id=usuario_id
        )

        try:
            db.session.add(novo_ganho)
            db.session.commit()
            flash('Ganho adicionado com sucesso!', 'success')
            return redirect(url_for('resumo'))
        except Exception as e:
            db.session.rollback()
            flash(f'Erro ao adicionar ganho: {e}', 'error')
            return render_template('adicionar_ganho.html')

    return render_template('adicionar_ganho.html')

if __name__ == '__main__':
    with app.app_context():  # Certifique-se de usar o contexto da aplicação
        db.create_all()  # Criar as tabelas, se elas ainda não existirem
    app.run(debug=True)
    


