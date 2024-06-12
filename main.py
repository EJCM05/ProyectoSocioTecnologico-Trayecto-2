import tkinter as tk
import customtkinter as ctk
from modulos.login import LoginApp

class VentanaPrincipal():
    def __init__(self):
        # definicion de apariencia
        self.configurar_apariencia()
        
        # creacion de ventana
        self.crear_ventana_principal()
        
        self.cargar_ventana_login()
    
    
    # configurar apariencia
    def configurar_apariencia(self):
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("dark-blue")
    
    
    # metodo para crear la ventana principal
    def crear_ventana_principal(self):
        self.app = ctk.CTk()
        self.app.geometry("1280x720")
        self.app.title("Login")
        self.app.resizable(0,0)
    
    
    def cargar_ventana_login(self):
        contenido_inicio = LoginApp(self.app)
        contenido_inicio.mostrar()
    
    
    #iniciar la ventana
    def run(self):
        self.app.mainloop()

app = VentanaPrincipal()
app.run()