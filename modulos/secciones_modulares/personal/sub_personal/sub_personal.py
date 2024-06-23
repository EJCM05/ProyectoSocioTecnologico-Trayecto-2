import customtkinter as ctk
from modulos.variables import variables as var

class SubPersonalVentana:
    def __init__(self, master, nombre_personal):
        self.master = master
        self.nombre_personal = nombre_personal
    
    
    def mostrar(self):
        # Eliminar widgets anteriores en el área de contenido
        for widget in self.master.winfo_children():
            widget.destroy()
        
        self.texto_titulo()
    
    
    def texto_titulo(self):
        self.texto_seleccion = ctk.CTkLabel(master=self.master,
                                           text=f"Personal {self.nombre_personal}",
                                           text_color=var.text_black,
                                           font=var.Andika_large
                                           )
        
        self.texto_seleccion.place(relx=0.5, rely=0.06, anchor="center")