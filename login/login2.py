import tkinter as tk
import customtkinter as CustomTK
from PIL import ImageTk, Image

class LoginApp:
    def __init__(self):
        # definicion de aparciencia
        CustomTK.set_appearance_mode("dark")
        CustomTK.set_default_color_theme("green")
        # creando ventana
        self.app = CustomTK.CTk()
        self.app.geometry("1024x720")
        self.app.title("Login")
        
        # importando y añadiendo imagen de fondo
        img_bg = ImageTk.PhotoImage(Image.open("imagen/background_login.jpg"))    
        self.div_login = CustomTK.CTkLabel(master=self.app, image=img_bg)
        self.div_login.pack()

        # añadiendo frame right
        self.frame = CustomTK.CTkFrame(master=self.div_login, width=320, height=380,corner_radius=50)
        self.frame.place(relx=0.5, rely=0.5, anchor=tk.E) #posicion del frame

        # añadiendo frame left
        self.frame2 = CustomTK.CTkFrame(master=self.div_login, width=320,height=380,fg_color="#151515")
        self.frame2.place(relx=0.5,rely=0.5,anchor=tk.W) #posicion del frame
        
        # imagen de frame2
        img_login_left = CustomTK.CTkImage(Image.open("imagen/logo.png"), size=(320,320))
        image_label=CustomTK.CTkLabel(master=self.frame2,image=img_login_left,text=" ")
        image_label.place(x=15, y=30)
        
        # imagen de login user
        img_log = CustomTK.CTkImage(Image.open("imagen/user_login.png"), size=(80,80))
        image_label = CustomTK.CTkLabel(master=self.frame,image=img_log, text=" ")
        image_label.place(x=125, y=25)

        # añadiendo texto
        div_login_two = CustomTK.CTkLabel(master=self.frame,text="Iniciar sesion",font=("Lucida Sans", 24))
        div_login_two.place(x=85, y=110)

        # entradas de texto
        self.input_one = CustomTK.CTkEntry(master=self.frame, width=220, placeholder_text="Usuario", font=("Verdana",16))
        self.input_one.place(x=50, y=160)

        self.input_two = CustomTK.CTkEntry(master=self.frame, width=220, placeholder_text="Contraseña", show="*", font=("Verdana",16))
        self.input_two.place(x=50, y=200)

        # boton
        button1 = CustomTK.CTkButton(master=self.frame, width=220, text="Login", corner_radius=6)
        button1.place(x=50, y=270)


            
    # funcion de bucle
    def run(self):
        self.app.mainloop()

# Crear y ejecutar la aplicación
app = LoginApp()
app.run()
