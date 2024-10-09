from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.db import db

class Usuario(db.Model):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    senha = Column(String, nullable=False)
    cnpj = Column(String, unique=True, nullable=False)
    dados_bancarios = Column(String)

    jogos = relationship("Jogo", back_populates="usuario")  # Relacionamento com Jogo
    pessoas = relationship("Pessoa", back_populates="usuario")  # Relacionamento com Pessoa