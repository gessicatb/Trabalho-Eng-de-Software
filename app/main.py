from tkinter.ttk import *
from tkinter import *
from usuario import Usuario
import customtkinter as ctk

def main() -> None:
    # Cria tkinter geral
    app = ctk.CTk()

    # Selecionando o tema - dark, light , system (for system default)
    app.set_appearance_mode("dark")
    
    # Selecionando cor tema - blue, green, dark-blue
    app.set_default_color_theme("dark-blue")
    
    # Configura fontes
    title_font = ctk.CTkFont(family="sans-serif", size=20, slant="italic", weight="bold")
    placeholder_botao = ctk.CTkFont(family="arial", size=15)

    _ = Usuario(app, title_font, placeholder_botao)

    # Inicia aplicação tkinter
    app.mainloop()

if __name__ == "__main__":
    main()
