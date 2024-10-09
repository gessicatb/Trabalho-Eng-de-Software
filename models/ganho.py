from models.db import db

class Ganho(db.Model):
    __tablename__ = 'ganhos'  # Nome da tabela no banco de dados

    id = db.Column(db.Integer, primary_key=True)
    valor = db.Column(db.Float, nullable=False)  # Valor do ganho
    descricao = db.Column(db.String(200), nullable=True)  # Descrição do ganho
    mes = db.Column(db.String(20), nullable=False)  # Adiciona o mês
    data = db.Column(db.DateTime, default=db.func.current_timestamp())  # Data do ganho
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)  # Chave estrangeira para o usuário

    def __repr__(self):
        return f'<Ganho {self.id}, Valor: {self.valor}>'