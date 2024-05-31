import tkinter as tk
import customtkinter as CustomTK
import variables as var
from PIL import ImageTk, Image

class LoginApp:
    def __init__(self):
        # definicion de aparciencia
        CustomTK.set_appearance_mode("light")
        CustomTK.set_default_color_theme("dark-blue")
        
        # creacion de ventana
        self.app = CustomTK.CTk()
        self.app.geometry("1024x720")
        self.app.title("Login")
        
        # importando y añadiendo imagenes de background y iconos
        img_bg = ImageTk.PhotoImage(Image.open("imagen/background_light.png"))    
        img_bg_frame = ImageTk.PhotoImage(Image.open("imagen/background_gradient_blue.png"))
        icono_user = ImageTk.PhotoImage(file="imagen/ico_user.png")
        icono_password = ImageTk.PhotoImage(file="imagen/ico_password.png")
        
        # ------------------------------Frames--------------------------- 
        self.div_login = CustomTK.CTkLabel(master=self.app, image=img_bg,fg_color="transparent")
        
        self.frame = CustomTK.CTkFrame(master=self.div_login,
                                        width=663,
                                        height=546)
        
        img_bg = CustomTK.CTkLabel(master=self.frame,
                                    image=img_bg_frame,
                                    text=" ",
                                    bg_color=var.bg_light_blue)
        
        self.frame2 = CustomTK.CTkFrame(master=self.div_login,
                                        width=457,
                                        height=546,
                                        fg_color=var.bg_white)
        
        div_login_two = CustomTK.CTkLabel(master=self.frame2,
                                        text="Hola!",
                                        font=var.font_text_bold
                                        )
        
        div_login_three = CustomTK.CTkLabel(master=self.frame2,
                                            text="Bienvenido de nuevo",
                                            font=var.font_text_regular
                                            )      
        
        self.input_one = CustomTK.CTkEntry(master=self.frame2,
                                        width=220,
                                        height=40,
                                        placeholder_text="Usuario",
                                        font=var.font_text_entry,
                                        corner_radius=100)
        
        label_ico_user = CustomTK.CTkLabel(master=self.frame2,
                                            image=icono_user,
                                            text=" "
                                            )
        
        self.input_two = CustomTK.CTkEntry(master=self.frame2,
                                        width=220,
                                        height=40,
                                        placeholder_text="Contraseña",
                                        show="*",
                                        font=var.font_text_entry,
                                        corner_radius=100)
        
        label_ico_password = CustomTK.CTkLabel(master=self.frame2,
                                            image=icono_password,
                                            text=" "
                                            )
        
        button1 = CustomTK.CTkButton(master=self.frame2,
                                    width=100,
                                    height=35,
                                    text="Login",
                                    corner_radius=100,
                                    fg_color=var.blue_button,
                                    font=var.font_text_button)
        
        div_login_four = CustomTK.CTkLabel(master=self.frame,
                                            text="Somos Educacion",
                                            font=var.font_text_regular,
                                            text_color=var.text_white,
                                            fg_color="transparent",
                                            bg_color="transparent"
                                            )      
        
        
        #---------------- posicionamiento-----------------------
            
        self.div_login.pack()
        self.frame.place(relx=0.58, rely=0.5, anchor=tk.E) #posicion del frame
        self.frame2.place(relx=0.58,rely=0.5,anchor=tk.W) #posicion del frame
        self.input_two.place(x=50, y=290)
        self.input_one.place(x=50, y=240)
        
        div_login_two.place(x=50, y=130)
        
        div_login_three.place(x=50,y=175)
        
        label_ico_user.place(x=20,y=245)
        
        label_ico_password.place(x=20,y=295)
        
        img_bg.place(x=0,y=0)
        
        
        
        button1.place(x=100, y=355,anchor=tk.W)
        
        div_login_four.place(x=50,y=200,anchor=tk.W)
        
        
        
        
        
    # funcion de bucle
    def run(self):
        self.app.mainloop()

# Crear y ejecutar la aplicación
app = LoginApp()
app.run()
