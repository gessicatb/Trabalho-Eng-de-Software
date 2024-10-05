from tkinter.ttk import *
from tkinter import *
from PIL import Image, ImageTk
import customtkinter as ctk

class Usuario():
    def __init__(self, app, placeholder_botao, title_font):
        self.app = app
        self.placeholder_botao = placeholder_botao
        self.title_font = title_font
        self.telaLogin()

    def login(self):
        pass

    def telaLogin(self):
        self.app.geometry("800x800")
        self.app.title("Login distribuidora musical")
        self.label = ctk.CTkLabel(
            self.app, text="Seja bem vindo a sua distribuidora de música digital!", font=self.title_font)
        self.label.pack(pady=20)

        self.frame = ctk.CTkFrame(master=self.app)
        self.frame.pack(pady=20, padx=40, fill='both', expand=True)

        self.my_image = Image.open("interface/image/logo.png")
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