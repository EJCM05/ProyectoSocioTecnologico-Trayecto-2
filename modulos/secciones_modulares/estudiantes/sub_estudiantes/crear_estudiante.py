import customtkinter as ctk
from modulos.variables import variables as var

class CrearEstudianteVentana:
    def __init__(self, master):
        self.master = master
    
    
    def mostrar(self):
        # Eliminar widgets anteriores en el área de contenido
        for widget in self.master.winfo_children():
            widget.destroy()
        
        self.texto_titulo()
        self.area_input()
    
    
    def texto_titulo(self):
        self.texto_seleccion = ctk.CTkLabel(master=self.master,
                                           text="Registrar Estudiante",
                                           text_color=var.text_black,
                                           font=var.Andika_large
                                           )
        
        self.texto_seleccion.place(relx=0.5, rely=0.06, anchor="center")
    
    
    def area_input(self):
        self.contenedor_input = ctk.CTkFrame(master=self.master,
                                 width=400,
                                 height=500,
                                 corner_radius=20,
                                 fg_color=var.bg_blue
                                 )
        
        self.contenedor_input.place(relx=0.5, rely=0.1, anchor="n")
