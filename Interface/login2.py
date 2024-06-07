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
    
    
    # parte central (login e informacion)
    def parte_central(self):
        # parte izquierda
        self.frame = CustomTK.CTkFrame(master=self.div_login,
                                        width=463,
                                        height=546)
        
        #parte derecha
        self.frame2 = CustomTK.CTkFrame(master=self.div_login,
                                        width=357,
                                        height=546,
                                        fg_color=var.bg_white)
        # -- Posicionamiento --
        self.frame.place(relx=0.54, rely=0.5, anchor=tk.E) #posicion del frame
        self.frame2.place(relx=0.54,rely=0.5,anchor=tk.W) #posicion del frame
    
    
    def derecha(self):
        self.div_login_two = CustomTK.CTkLabel(master=self.frame2,
                                        text="Hola!",
                                        font=var.font_text_bold
                                        )
        
        self.div_login_three = CustomTK.CTkLabel(master=self.frame2,
                                            text="Bienvenido de nuevo",
                                            font=var.font_text_regular
                                            )      
        
        self.input_one = CustomTK.CTkEntry(master=self.frame2,
                                        width=220,
                                        height=40,
                                        placeholder_text="Usuario",
                                        font=var.font_text_entry,
                                        corner_radius=100)
        
        self.label_ico_user = CustomTK.CTkLabel(master=self.frame2,
                                            image=self.icono_user,
                                            text=" "
                                            )
        
        self.input_two = CustomTK.CTkEntry(master=self.frame2,
                                        width=220,
                                        height=40,
                                        placeholder_text="Contraseña",
                                        show="*",
                                        font=var.font_text_entry,
                                        corner_radius=100)
        
        self.label_ico_password = CustomTK.CTkLabel(master=self.frame2,
                                            image=self.icono_password,
                                            text=" "
                                            )
        
        self.button1 = CustomTK.CTkButton(master=self.frame2,
                                    width=100,
                                    height=35,
                                    text="Login",
                                    corner_radius=100,
                                    fg_color=var.blue_button,
                                    font=var.font_text_button)
        # -- Posicionamiento --
        self.input_two.place(x=50, y=290)
        self.input_one.place(x=50, y=240)
        self.div_login_two.place(x=50, y=130)
        self.div_login_three.place(x=50,y=175)
        self.label_ico_user.place(x=20,y=245)
        self.label_ico_password.place(x=20,y=295)
        self.button1.place(x=100, y=355,anchor=tk.W)
    
    
    def izquierda(self):
        img_bg = CustomTK.CTkLabel(master=self.frame,
                                    image=self.img_bg_frame,
                                    text=" ",
                                    bg_color=var.bg_light_blue)
        
        button2 = CustomTK.CTkButton(master=self.frame,
                                    width=100,
                                    height=35,
                                    text="Leer mas!",
                                    corner_radius=0,
                                    fg_color=var.blue_button,
                                    bg_color="#02369A",
                                    font=var.font_text_button)
        # -- Posicionamiento --
        img_bg.place(x=0,y=0)
        button2.place(x=70, y=325,anchor=tk.W)
    
    
    # imagen de fondo
    def fondo(self):
        self.div_login = CustomTK.CTkLabel(master=self.app, image=self.img_bg)
        # -- Posicionamiento --
        self.div_login.pack()
    
    
    # importando y añadiendo imagenes de background e iconos
    def importar_img_ico(self):
        self.img_bg = ImageTk.PhotoImage(Image.open("imagen/background_light.png"))    
        self.img_bg_frame = ImageTk.PhotoImage(Image.open("imagen/background_gradient_blue.png"))
        self.icono_user = ImageTk.PhotoImage(file="imagen/ico_user.png")
        self.icono_password = ImageTk.PhotoImage(file="imagen/ico_password.png")
        self.icono_user_dashboard = ImageTk.PhotoImage(file="imagen/ico_user_dashboard.png")
        
    
    
    # configurar apariencia
    def configurar_apariencia(self):
        CustomTK.set_appearance_mode("light")
        CustomTK.set_default_color_theme("dark-blue")
    
    
    # metodo para crear la ventana principal
    def crear_ventana_principal(self):
        self.app = CustomTK.CTk()
        self.app.geometry("920x600")
        self.app.title("Login")
        # self.app.resizable(0,0)
    
    
    # funcion de bucle
    def run(self):
        self.app.mainloop()


# Crear y ejecutar aplicación
app = LoginApp()
app.run()
