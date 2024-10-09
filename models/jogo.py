from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.db import db

class Jogo(db.Model):
    __tablename__ = 'jogos'

    id = Column(Integer, primary_key=True)
    nome_jogo = Column(String, nullable=False)
    genero = Column(String, nullable=False)
    descricao = Column(String)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'))  # Relacionamento com o modelo Usuario

    usuario = relationship("Usuario", back_populates="jogos")  # Para permitir o acesso inverso