import customtkinter as ctk
from modulos.variables import variables as var
from modulos.secciones_modulares.estudiantes.sub_estudiantes.crear_estudiante import CrearEstudianteVentana

class EstudiantesVentana:
    def __init__(self, master):
        self.master = master
    
    
    def mostrar(self):
        # Eliminar widgets anteriores en el área de contenido
        for widget in self.master.winfo_children():
            widget.destroy()
        
        self.texto_titulo()
        self.botones_seleccion_estudiantes()
    
    
    def cargar_ventana_crear_estudiante(self):
        self.contenido_ventana_crear_estudiante = CrearEstudianteVentana(master=self.master)
        self.contenido_ventana_crear_estudiante.mostrar()
    
    
    def texto_titulo(self):
        self.texto_seleccion = ctk.CTkLabel(master=self.master,
                                           text="Estudiantes",
                                           text_color=var.text_black,
                                           font=var.Andika_large
                                           )
        
        self.texto_seleccion.place(relx=0.5, rely=0.06, anchor="center")
    
    
    def botones_seleccion_estudiantes(self):
        self.boton_crear_estudiante = self.crear_botones_estudiantes(texto="Crear estudiante",
                                                        comando=lambda: self.cargar_ventana_crear_estudiante(),
                                                        color_boton=var.btn_gray,
                                                        posicion_x=0.15,
                                                        posicion_y=0.45
                                                       )
    
    #Metodo para crear botones
    def crear_botones_estudiantes(self, texto, comando, color_boton, posicion_x, posicion_y):
        boton = ctk.CTkButton(master=self.master,
                             text=texto,
                             width=180,
                             height=50,
                             font=var.Amaranth_small,
                             fg_color=color_boton,
                             hover_color=var.hover_buttons_color,
                             corner_radius=10,
                             command=comando
                             )
        
        boton.place(relx=posicion_x, rely=posicion_y, anchor="center")