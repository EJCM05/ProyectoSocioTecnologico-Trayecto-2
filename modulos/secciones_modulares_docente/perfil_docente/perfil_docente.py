import customtkinter as ctk
from modulos.variables import variables as var

class PerfilVentana:
    def __init__(self, master):
        self.master = master

    def mostrar(self):
        # Eliminar widgets anteriores en el área de contenido
        for widget in self.master.winfo_children():
            widget.destroy()

        self.texto_titulo()
    
    def texto_titulo(self):
        self.texto_seleccion = ctk.CTkLabel(master=self.master,
                                           text="Perfil",
                                           text_color=var.text_black,
                                           font=var.Andika_large
                                           )
        
        self.texto_seleccion.place(relx=0.5, rely=0.06, anchor="center")
    
    
    # Metodos  de creacion generales
    #Metodo para crear texto
    def crear_texto(self, posicion_x, posicion_y, texto,fuente):
        palabras = ctk.CTkLabel(master=self.master,
                                            text=texto,
                                            text_color=var.text_black,
                                            font=fuente,
                                            fg_color="white",
                                            compound="center",
                                            justify="center"
                                            )
        palabras.place(relx=posicion_x, rely=posicion_y,anchor="center")
    
    
    #Metodo para crear botones
    def crear_botones(self, texto, comando, color_boton, posicion_x, posicion_y):
        boton = ctk.CTkButton(master=self.master,
                             text=texto,
                             width=130,
                             height=40,
                             font=var.Andika_small_ultra,
                             fg_color=color_boton,
                             hover_color=var.hover_button_blue,
                             corner_radius=5,
                             command=comando
                             )
        
        boton.place(relx=posicion_x, rely=posicion_y,anchor="center")
