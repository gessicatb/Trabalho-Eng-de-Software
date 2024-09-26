from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Inicializando o banco de dados
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Configuração do banco de dados
    app.config.from_object('config.Config')

    # Inicializa o banco de dados
    db.init_app(app)

    # Registrar as rotas
    from .routes import init_routes
    init_routes(app)

    return app

