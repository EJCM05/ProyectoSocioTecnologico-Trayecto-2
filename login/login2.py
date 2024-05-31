import tkinter as tk
import customtkinter as CustomTK
import variables as var
from PIL import ImageTk, Image

class LoginApp:
    def __init__(self):
        # definicion de aparciencia
        CustomTK.set_appearance_mode("light")
        CustomTK.set_default_color_theme("dark-blue")
        # creando ventana
        self.app = CustomTK.CTk()
        self.app.geometry("1024x720")
        self.app.title("Login")
        
        # importando y añadiendo imagenes de background y iconos
        img_bg = ImageTk.PhotoImage(Image.open("imagen/background_light.png"))    
        img_login_left = CustomTK.CTkImage(Image.open("imagen/interface_control.png"), size=(240,240))
        img_bg_frame = ImageTk.PhotoImage(Image.open("imagen/background_gradient_blue.png"))
        
        # frame principal
        self.div_login = CustomTK.CTkLabel(master=self.app, image=img_bg)
        self.div_login.pack()

        # añadiendo frame left
        self.frame = CustomTK.CTkFrame(master=self.div_login,
                                        width=663,
                                        height=546)
        
        self.frame.place(relx=0.58, rely=0.5, anchor=tk.E) #posicion del frame
        
        img_bg = CustomTK.CTkLabel(master=self.frame,
                                    image=img_bg_frame,
                                    text=" ",
                                    bg_color="#B8CEE4")
        img_bg.place(x=0,y=0)

        
        # añadiendo frame right
        self.frame2 = CustomTK.CTkFrame(master=self.div_login,
                                        width=457,
                                        height=546,
                                        fg_color="#FFFFFF")
        
        self.frame2.place(relx=0.58,rely=0.5,anchor=tk.W) #posicion del frame
    
        # # imagen de login user
        # img_log = CustomTK.CTkImage(Image.open("imagen/user.png"), size=(100,100))
        # image_label = CustomTK.CTkLabel(master=self.frame2,image=img_log, text=" ")
        # image_label.place(x=115, y=25)

        # añadiendo texto
        div_login_two = CustomTK.CTkLabel(master=self.frame2,
                                        text="HOLA!",
                                        font=var.font_text_2)
        div_login_two.place(x=50, y=170)

        div_login_three = CustomTK.CTkLabel(master=self.frame2,
                                            text="Bienvenido de nuevo",
                                            font=var.font_text)
        div_login_three.place(x=50,y=190)

        # entradas de texto
        self.input_one = CustomTK.CTkEntry(master=self.frame2, width=220,
                                        placeholder_text="Usuario",
                                        font=("Verdana",16),
                                        corner_radius=100)
        
        self.input_one.place(x=50, y=240)

        self.input_two = CustomTK.CTkEntry(master=self.frame2,
                                        width=220, 
                                        placeholder_text="Contraseña",
                                        show="*",
                                        font=("Verdana",16),
                                        corner_radius=100)
        
        self.input_two.place(x=50, y=280)

        # boton
        button1 = CustomTK.CTkButton(master=self.frame2,
                                    width=100,
                                    height=40,
                                    text="Login",
                                    corner_radius=100,
                                    fg_color=var.blue_button,
                                    font=var.font_text_button)
        
        button1.place(x=100, y=350,anchor=tk.W)


            
    # funcion de bucle
    def run(self):
        self.app.mainloop()

# Crear y ejecutar la aplicación
app = LoginApp()
app.run()
