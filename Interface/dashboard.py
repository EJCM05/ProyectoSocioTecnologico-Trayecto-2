import tkinter as tk
import customtkinter as CustomTK
import variables as var
from PIL import ImageTk, Image

class Dashboard():
    def __init__(self):
        # Las nuevas funciones constructoras se ejecutan aqui
        self.ConfigurarcionDeApariencia()
        self.CreacionDeVentana()
        self.ImportacionDeImagenes()
        self.agregar_widgets()
        
        
    def ImportacionDeImagenes(self):
        # importacion de imagenes background e iconos 
        self.img_bg = ImageTk.PhotoImage(Image.open("imagen/background_dashboard.png"))
        
    def CrearFrames(self):
        self.panel_principal = CustomTK.CTkFrame(master=self.app, width=1100, height=800, fg_color="#ffffff", corner_radius=100)        
        self.panel_izquierdo = CustomTK.CTkFrame(master=self.app, width=240, height=800, fg_color="#EBEBEB", corner_radius=20)  
        # posicionamiento   
        self.panel_izquierdo.grid(column=0, row=0, padx=30,pady=25)
        self.panel_principal.grid(column=1, row=0, padx=10,pady=25 )
    
    def CrearLabel(self):
        # labels
        self.bg_izq = CustomTK.CTkLabel(master=self.panel_izquierdo, text=" ", height=800,width=240,image=self.img_bg)
        self.label1 = CustomTK.CTkLabel(master=self.panel_principal, text="Total de Estudiantes", 
                                        font=("FontAwesome",30, "bold"), fg_color="#84b6f4", height=100, width=200)        
        self.label2 = CustomTK.CTkLabel(master=self.panel_principal, text="Total de Secciones", 
                                        font=("FontAwesome",30, "bold"), fg_color="#84b6f4", height=100, width=200)        
        self.label3 = CustomTK.CTkLabel(master=self.panel_principal, text="Total de Profesores", 
                                        font=("FontAwesome",30, "bold"), fg_color="#84b6f4", height=100, width=200)        
        self.label4 = CustomTK.CTkLabel(master=self.panel_principal, text="Grafico de todas\nlas Estadisticas",
                                        font=("FontAwesome",30, "bold"), fg_color="#84b6f4", height=250, width=800)  
        self.titulo = CustomTK.CTkLabel(master=self.panel_principal, text="Panel Principal", font=("consola", 30, "bold" ))        
        self.sub_titulo = CustomTK.CTkLabel(master=self.panel_principal, text="Bienvenido (Ususario)", font=("consola",10, "bold")) 
        
        # -------------posicionamiento general ----------------#
        
        self.label1.place(x=100, y=150)
        self.label2.place(x=450, y=150)
        self.label3.place(x=800, y=150)
        self.label4.place(x=150, y=350)
        self.titulo.place(x=150, y=30)
        self.sub_titulo.place(x=150, y=70)
        self.bg_izq.place(x=0,y=0)
        
    def crear_botones(self):
        # Botones panel izquierdo
        self.home = CustomTK.CTkButton(master=self.panel_izquierdo,
                                    width=100,
                                    text="Home",
                                    corner_radius=100,
                                    hover_color="#006BD7",
                                    bg_color="#0463D1",
                                    fg_color=var.blue_button,
                                    font=var.font_text_button)
        
        # --------posicionamiento general---------------#
        self.home.place(x=60,y=120)
        
        
    def ConfigurarcionDeApariencia(self):
        # definicion de apariencia
        CustomTK.set_appearance_mode("light")
        CustomTK.set_default_color_theme("blue")
        
    def CreacionDeVentana(self):
        # creacion de ventana
        self.app = CustomTK.CTk()
        self.app.geometry("1024x720")
        self.app.title("Dashboard")        

    def agregar_widgets(self):
        # Agregar Funciones costructoras de nuevos wighets
        self.CrearFrames()
        self.CrearLabel()
        self.crear_botones()
    
    def run(self):
        # Funcion auto-ejecutable
        self.app.mainloop() #esto tiene que ir de ultimo

# Crear y ejecutar aplicación
app = Dashboard()
app.run()