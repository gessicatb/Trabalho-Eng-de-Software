from flask import request, jsonify
from .models import User, Person, Game
from . import db
from sqlalchemy.exc import IntegrityError

def init_routes(app):

    @app.route('/register', methods=['POST'])
    def register_user():
        data = request.json
        try:
            new_user = User(
                name=data['name'],
                email=data['email'],
                cpf_cnpj=data['cpf_cnpj'],
                bank_details=data['bank_details']
            )
            new_user.set_password(data['password'])
            db.session.add(new_user)
            db.session.commit()
            return jsonify({"message": "Usuário registrado com sucesso!"}), 201
        except IntegrityError:
            db.session.rollback()
            return jsonify({"message": "Erro: Email ou CPF/CNPJ já está em uso."}), 400

    @app.route('/login', methods=['POST'])
    def login():
        data = request.json
        user = User.query.filter_by(email=data['email']).first()
        if user and user.check_password(data['password']):
            return jsonify({"message": "Login bem-sucedido!"}), 200
        return jsonify({"message": "Email ou senha incorretos."}), 401

    @app.route('/add_person', methods=['POST'])
    def add_person():
        data = request.json
        try:
            new_person = Person(
                name=data['name'],
                email=data['email'],
                cpf=data['cpf'],
                social_media=data['social_media'],
                phone=data['phone']
            )
            db.session.add(new_person)
            db.session.commit()
            return jsonify({"message": "Pessoa cadastrada com sucesso!"}), 201
        except IntegrityError:
            db.session.rollback()
            return jsonify({"message": "Erro: CPF já cadastrado."}), 400

    @app.route('/add_game', methods=['POST'])
    def add_game():
        data = request.json
        try:
            new_game = Game(
                title=data['title'],
                platform=data['platform'],
                genre=data['genre'],
                release_date=data['release_date'],
                sku=data['sku'],
                isrc=data['isrc'],
                developers=data['developers']
            )
            db.session.add(new_game)
            db.session.commit()
            return jsonify({"message": "Jogo cadastrado com sucesso!"}), 201
        except IntegrityError:
            db.session.rollback()
            return jsonify({"message": "Erro: SKU ou ISRC já está em uso."}), 400
