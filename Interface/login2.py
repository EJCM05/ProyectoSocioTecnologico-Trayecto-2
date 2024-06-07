import tkinter as tk
import customtkinter as CustomTK
import variables as var
from PIL import ImageTk, Image

class LoginApp:
    def __init__(self):
        
        # definicion de apariencia
        self.configurar_apariencia()
        
        # creacion de ventana
        self.crear_ventana_principal()
        
        # importando imagenes de background e iconos
        self.importar_img_ico()
        
        # fondo
        self.fondo()
        
        # cuadro principal
        self.parte_central()
        self.derecha()
        self.izquierda()
    

    # configurar apariencia
    def configurar_apariencia(self):
        CustomTK.set_appearance_mode("light")
        CustomTK.set_default_color_theme("dark-blue")
    
    
    # metodo para crear la ventana principal
    def crear_ventana_principal(self):
        self.app = CustomTK.CTk()
        self.app.geometry("1240x720")
        self.app.title("Login")
    

    # importando y añadiendo imagenes de background e iconos
    def importar_img_ico(self):
        self.img_bg = ImageTk.PhotoImage(Image.open("imagen/background_light.png"))    
        self.img_bg_frame = ImageTk.PhotoImage(Image.open("imagen/background_gradient_blue.png"))
        self.icono_user = ImageTk.PhotoImage(file="imagen/ico_user.png")
        self.icono_password = ImageTk.PhotoImage(file="imagen/ico_password.png")
    
    
    # imagen de fondo
    def fondo(self):
        self.div_login = CustomTK.CTkLabel(master=self.app, image=self.img_bg)
        # -- Posicionamiento --
        self.div_login.pack()
    
    
    # parte central (login e informacion)
    def parte_central(self):
        # parte izquierda
        self.frame_izquierda = CustomTK.CTkFrame(master=self.div_login,
                                        width=663,
                                        height=546)
        
        #parte derecha
        self.frame_derecha = CustomTK.CTkFrame(master=self.div_login,
                                        width=457,
                                        height=546,
                                        fg_color=var.bg_white)
        # -- Posicionamiento --
        self.frame_izquierda.place(relx=0.58, rely=0.5, anchor=tk.E) #posicion del frame
        self.frame_derecha.place(relx=0.58,rely=0.5,anchor=tk.W) #posicion del frame
    
    
    def derecha(self):
        self.texto_hola = CustomTK.CTkLabel(master=self.frame_derecha,
                                        text="Hola!",
                                        font=var.font_text_bold
                                        )
        
        self.texto_bienvenido = CustomTK.CTkLabel(master=self.frame_derecha,
                                            text="Bienvenido de nuevo",
                                            font=var.font_text_regular
                                            )      
        
        self.input_user = CustomTK.CTkEntry(master=self.frame_derecha,
                                        width=220,
                                        height=40,
                                        placeholder_text="Usuario",
                                        font=var.font_text_entry,
                                        corner_radius=100)
        
        self.label_ico_user = CustomTK.CTkLabel(master=self.frame_derecha,
                                            image=self.icono_user,
                                            text=" "
                                            )
        
        self.input_password = CustomTK.CTkEntry(master=self.frame_derecha,
                                        width=220,
                                        height=40,
                                        placeholder_text="Contraseña",
                                        show="*",
                                        font=var.font_text_entry,
                                        corner_radius=100)
        
        self.label_ico_password = CustomTK.CTkLabel(master=self.frame_derecha,
                                            image=self.icono_password,
                                            text=" "
                                            )
        
        self.button_login = CustomTK.CTkButton(master=self.frame_derecha,
                                    width=100,
                                    height=35,
                                    text="Login",
                                    corner_radius=100,
                                    fg_color=var.blue_button,
                                    font=var.font_text_button)
        # -- Posicionamiento --
        self.texto_hola.place(x=50, y=130)
        self.texto_bienvenido.place(x=50,y=175)
        self.input_user.place(x=50, y=240)
        self.input_password.place(x=50, y=290)
        self.label_ico_user.place(x=20,y=245)
        self.label_ico_password.place(x=20,y=295)
        self.button_login.place(x=100, y=355,anchor=tk.W)
    
    
    def izquierda(self):
        self.img_bg = CustomTK.CTkLabel(master=self.frame_izquierda,
                                    image=self.img_bg_frame,
                                    text=" ",
                                    bg_color=var.bg_light_blue)
        
        self.button_leer = CustomTK.CTkButton(master=self.frame_izquierda,
                                    width=100,
                                    height=35,
                                    text="Leer mas!",
                                    corner_radius=0,
                                    fg_color=var.blue_button,
                                    bg_color="#02369A",
                                    font=var.font_text_button)
        # -- Posicionamiento --
        self.img_bg.place(x=0,y=0)
        self.button_leer.place(x=70, y=325,anchor=tk.W)
    
    
    # funcion de bucle
    def run(self):
        self.app.mainloop()


# Crear y ejecutar aplicación
app = LoginApp()
app.run()
