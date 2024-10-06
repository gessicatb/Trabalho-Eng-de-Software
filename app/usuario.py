import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
from tkinter import *
import customtkinter as ctk
import tkinter.messagebox as tkmb
from PIL import Image, ImageTk
import psycopg2
from conexaobd import Banco
from datetime import date

class Usuario():
    def __init__(self, app, placeholder_botao, title_font):
        self.app = app
        self.placeholder_botao = placeholder_botao
        self.title_font = title_font
        self.telaLogin()

    def login(self):
        # conectando banco de dados
        banco = Banco()
        bd = banco.conexao.cursor()

        # realiza busca
        buscaCnpj = """ SELECT "CNPJ" FROM public."Usuario" where "CNPJ" = %s; """
        buscaSenha = """ SELECT "Senha" FROM public."Usuario" where "CNPJ" = %s; """
        bd.execute(buscaCnpj, (self.user_entry.get(),))
        self.username = bd.fetchone()

        bd.execute(buscaSenha, (self.user_entry.get(),))
        self.password = bd.fetchone()

        # fecha comunicação com banco
        bd.close()

        # testando credenciais
        if self.username and self.password and self.user_pass.get() == self.password[0]:
            # Oculta a janela de login
            self.app.withdraw()
            self.cnpj = self.username
            Produto(self.app, self.cnpj)

        elif self.username and self.user_pass.get() != self.password[0]:
            tkmb.showwarning(title='Senha incorreta', message='Senha incorreta')
        else:
            tkmb.showerror(title="Falha no login", message="usuário e senha incorretos")

    def telaLogin(self):
        self.app.geometry("800x800")
        self.app.title("Login distribuidora de jogos")
        self.label = ctk.CTkLabel(
            self.app, text="Seja bem vindo a sua distribuidora de jogos digitais!", font=self.title_font)
        self.label.pack(pady=20)

        self.frame = ctk.CTkFrame(master=self.app)
        self.frame.pack(pady=20, padx=40, fill='both', expand=True)

        self.my_image = Image.open("app/image/logo.png")
        self.my_image = ImageTk.PhotoImage(
            self.my_image.resize((200, 200)))  # Resize the image
        self.image_label = ctk.CTkLabel(
            master=self.frame, image=self.my_image, text="")
        self.image_label.pack(pady=0, padx=0)

        self.label = ctk.CTkLabel(master=self.frame, text='')
        self.label.pack(pady=12, padx=10)

        self.user_entry = ctk.CTkEntry(
            master=self.frame, placeholder_text="CNPJ", width=250, font=self.placeholder_botao)
        self.user_entry.pack(pady=12, padx=10)

        self.user_pass = ctk.CTkEntry(
            master=self.frame, placeholder_text="Senha", show="*", width=250, font=self.placeholder_botao)
        self.user_pass.pack(pady=12, padx=10)

        self.button = ctk.CTkButton(
            master=self.frame, text='Entrar', width=250, font=self.placeholder_botao, command=self.login)
        self.button.pack(pady=12, padx=10)

        self.button = ctk.CTkButton(master=self.frame, text='Novo cadastro',
                                    width=250, font=self.placeholder_botao, command=self.cadastro)
        self.button.pack(pady=12, padx=10)

        self.checkbox = ctk.CTkCheckBox(
            master=self.frame, text='Esqueci minha senha')
        self.checkbox.pack(pady=12, padx=10)

    def cadastrar(self):
        pass

    def cadastro(self):
        pass