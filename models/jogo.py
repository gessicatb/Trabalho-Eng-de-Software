from .db import db

class Jogo(db.Model):
    __tablename__ = 'jogos'
    id = db.Column(db.Integer, primary_key=True)
    nome_jogo = db.Column(db.String(100), nullable=False)
    genero = db.Column(db.String(50), nullable=False)
    descricao = db.Column(db.Text)