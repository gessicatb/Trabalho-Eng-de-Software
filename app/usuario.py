from tkinter.ttk import *
from tkinter import *
from PIL import Image, ImageTk
from conexaobd import Banco
from produto import Produto
import customtkinter as ctk
import tkinter.messagebox as tkmb
import tkinter as tk
import psycopg2

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
        # Conectando banco de dados
        banco = Banco()
        bd = banco.conexao.cursor()
        try:
            # Execute the INSERT statement
            sql = """INSERT INTO public."Usuario"("Nome", "Email", "Senha", "CNPJ", "DadosBancario") VALUES(%s,%s,%s,%s,%s)"""
            bd.execute(sql, (self.nameEntry.get(), self.emailEntry.get(
            ), self.senhaEntry.get(), self.cnpjEntry.get(), self.bancoEntry.get()))
            # Commit the changes to the database
            banco.conexao.commit()
            # Close communication with the database
            bd.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if banco is not None:
                tkmb.showinfo(title="CadastradoSucesso",
                              message="Cadastro realizado com sucesso!")
                
    def cadastro(self):
        telaCadastro = ctk.CTkToplevel(self.app)
        telaCadastro.title("Tela Cadastro")
        telaCadastro.geometry("800x800")

        self.label = ctk.CTkLabel(
            telaCadastro, text="Cadastre seus dados:", font=self.title_font)
        self.label.pack(pady=20)
        # Frame
        self.frameCadastro = ctk.CTkFrame(master=telaCadastro)
        self.frameCadastro.pack(
            pady=20, padx=40, fill='both', anchor=tk.CENTER, expand=True)

        # Nome Label
        self.nameLabel = ctk.CTkLabel(
            master=self.frameCadastro, text="Nome", font=self.placeholder_botao)
        self.nameLabel.grid(row=0, column=0, padx=20, pady=20, sticky="ew")
        # Nome Entry Field
        self.nameEntry = ctk.CTkEntry(
            master=self.frameCadastro, placeholder_text="nome profissional", font=self.placeholder_botao, width=400)
        self.nameEntry.grid(row=0, column=1, columnspan=3,
                            padx=20, pady=20, sticky="ew")

        # Email Label
        self.emailLabel = ctk.CTkLabel(
            master=self.frameCadastro, text="Email", font=self.placeholder_botao)
        self.emailLabel.grid(row=1, column=0, padx=20, pady=20, sticky="ew")
        # Email Entry Field
        self.emailEntry = ctk.CTkEntry(
            master=self.frameCadastro, placeholder_text="email principal", font=self.placeholder_botao, width=400)
        self.emailEntry.grid(row=1, column=1, columnspan=3,
                             padx=20, pady=20, sticky="ew")

        # Senha Label
        self.senhaLabel = ctk.CTkLabel(
            master=self.frameCadastro, text="Senha", font=self.placeholder_botao)
        self.senhaLabel.grid(row=2, column=0, padx=20, pady=20, sticky="ew")
        # Senha Entry Field
        self.senhaEntry = ctk.CTkEntry(
            master=self.frameCadastro, placeholder_text="senha", font=self.placeholder_botao, width=400)
        self.senhaEntry.grid(row=2, column=1, columnspan=3,
                             padx=20, pady=20, sticky="ew")

        # CNPJ Label
        self.cnpjLabel = ctk.CTkLabel(
            master=self.frameCadastro, text="CNPJ", font=self.placeholder_botao)
        self.cnpjLabel.grid(row=3, column=0, padx=20, pady=20, sticky="ew")
        # CNPJ Entry Field
        self.cnpjEntry = ctk.CTkEntry(
            master=self.frameCadastro, placeholder_text="apenas números (12345678000100)", font=self.placeholder_botao, width=400)
        self.cnpjEntry.grid(row=3, column=1, columnspan=3,
                            padx=20, pady=20, sticky="ew")

        # Dados bancarios Label
        self.bancoLabel = ctk.CTkLabel(
            master=self.frameCadastro, text="Dados Bancarios", font=self.placeholder_botao)
        self.bancoLabel.grid(row=4, column=0, padx=20, pady=20, sticky="ew")
        # Dados bancarios Entry Field
        self.bancoEntry = ctk.CTkEntry(
            master=self.frameCadastro, placeholder_text="n° conta, n° banco, n° agencia", font=self.placeholder_botao, width=400)
        self.bancoEntry.grid(row=4, column=1, columnspan=3,
                             padx=20, pady=20, sticky="ew")

        # Botao
        self.botaoCadastro = ctk.CTkButton(
            master=self.frameCadastro, text='Cadastrar', width=250, font=self.placeholder_botao, command=self.cadastrar)
        self.botaoCadastro.grid(
            row=5, column=1, columnspan=3, padx=20, pady=20, sticky="ew")