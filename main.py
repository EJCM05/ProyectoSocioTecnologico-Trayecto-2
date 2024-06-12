import tkinter as tk
import customtkinter as ctk
from modulos.login import LoginApp
from modulos.dashboard import Dashboard

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
        #self.app.update_idletasks()
    
    
    def cargar_ventana_login(self):
        contenido_login = LoginApp(self.app)
        contenido_login.mostrar()
    
    
    def cargar_ventana_dashboard(self):
        contenido_dashboard = Dashboard(self.app)
        contenido_dashboard.mostrar()
    
    #iniciar la ventana
    def run(self):
        self.app.mainloop()

app = VentanaPrincipal()
app.run()