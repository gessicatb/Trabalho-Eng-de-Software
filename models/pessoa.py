from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.db import db

class Pessoa(db.Model):
    __tablename__ = 'pessoas'

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    email = Column(String, nullable=False)
    cpf = Column(String, nullable=False)
    rede_social = Column(String)
    telefone = Column(String)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'))  # Relacionamento com o modelo Usuario

    usuario = relationship("Usuario", back_populates="pessoas")  # Para permitir o acesso inverso