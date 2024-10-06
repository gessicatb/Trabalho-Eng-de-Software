from tkinter.ttk import *
from tkinter import *
from usuario import Usuario
import customtkinter as ctk
import tkinter.messagebox as tkmb

# selecionando o tema - dark, light , system (for system default)
ctk.set_appearance_mode("dark")
# selecionando cor tema - blue, green, dark-blue
ctk.set_default_color_theme("dark-blue")
# cria tkinter geral
app = ctk.CTk()
# configura fontes
title_font = ctk.CTkFont(family="sans-serif", size=20, slant="italic", weight="bold")
placeholder_botao = ctk.CTkFont(family="arial", size=15) 

# Inicia aplicação tkinter
app.mainloop()

if __name__ == "__main__":
    Usuario(app, placeholder_botao, title_font)
    
app.mainloop()    
