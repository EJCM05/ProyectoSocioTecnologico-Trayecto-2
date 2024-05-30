from customtkinter import *
from PIL import Image

app = CTk()
app.geometry("900x720")

# sistema
# set_appearance_mode("light")
set_appearance_mode("dark")




# interfaz aca van la mayoria de propiedades para personalizar 


# nuevas ventanas

frame = CTkFrame(master=app,
                #  fg_color="red",
                #  border_color="green",
                 border_width=2)
frame.place(relx=0.5,rely=0.2,anchor="center")
btn2=CTkButton(master=frame,text="hola")
btn2.place(relx=0.5,rely=0.5,anchor="center")


# widgets entry
entry = CTkEntry(master=app,
                 placeholder_text="Ingrese su Usuario...",
                 font=("Arial", 18),
                 width=280,
                #  text_color="#FFFFFF",
                 bg_color="#FFFFFF")
entry.place(relx=0.5,rely=0.6,anchor="center")

entry_two = CTkEntry(master=app,
                 placeholder_text="Ingrese su Contraseña...",
                 font=("Arial", 18),
                 width=280,
                #  text_color="#FFFFFF",
                 bg_color="#FFFFFF")
entry_two.place(relx=0.5,rely=0.5,anchor="center")



img = Image.open("imagen/locked.png") #esto es la variable con la imagen que vamos a usar
# boton
btn = CTkButton(master=app,
                text="Ingresar",
                width=200,
                font=("Arial",18),
                corner_radius=32,
                fg_color="#004AAC",
                hover_color="#00357C",
                border_color="black",
                border_width=0.5,
                image=CTkImage(dark_image=img,light_image=img) #esto se coloca por la imagen dark light
                )
btn.place(relx=0.5,rely=0.7,anchor="center")

app.mainloop()