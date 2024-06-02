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
        self.panel_central = CustomTK.CTkFrame(master=self.app,fg_color=var.bg_gray_light)
        self.panel_derecho = CustomTK.CTkFrame(master=self.panel_central,width=1000,height=800, fg_color=var.bg_white, corner_radius=100)    
        self.panel_izquierdo = CustomTK.CTkFrame(master=self.panel_central, width=240, height=800, fg_color=var.bg_gray_light, corner_radius=20)  

        #------------- posicionamiento--------------------------#
        self.panel_central.pack()
        self.panel_derecho.grid(column=4, row=0, padx=10,pady=25,columnspan=8)
        self.panel_izquierdo.grid(column=0, row=0, padx=20,pady=25)


    
    def CrearLabel(self):
        # labels
        self.bg_izq = CustomTK.CTkLabel(master=self.panel_izquierdo, text=" ", height=800,width=240,image=self.img_bg)
        self.label1 = CustomTK.CTkLabel(master=self.panel_derecho, text="Total de Estudiantes", 
                                        font=var.font_text_amaranth_medium, fg_color="#84b6f4", height=100, width=200)             
        self.label4 = CustomTK.CTkLabel(master=self.panel_derecho, text="Grafico de todas\nlas Estadisticas",
                                        font=var.font_text_amaranth_medium, fg_color="#84b6f4", height=250, width=800)  
        self.titulo = CustomTK.CTkLabel(master=self.panel_derecho, text="Panel Principal", font=("consola", 30, "bold" ))        
        self.sub_titulo = CustomTK.CTkLabel(master=self.panel_derecho, text="Bienvenido (Usuario)", font=var.font_text_bold_small) 
        
        # -------------posicionamiento general ----------------#
        
        self.label1.place(x=100, y=150)
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
        self.app.geometry("1240x720")
        self.app.title("Dashboard")        
        for i in range(10):
            self.app.grid_rowconfigure(i, weight=1)
            self.app.grid_columnconfigure(i, weight=1)


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