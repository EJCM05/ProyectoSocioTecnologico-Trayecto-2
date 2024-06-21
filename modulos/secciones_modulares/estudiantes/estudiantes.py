import tkinter as tk
from tkinter import ttk
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
        self.input_seleccion_estudiantes()
        self.texto_seleccion_estudiantes()
        self.consulta()
    
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
        
    # botones de estudiantes
    def botones_seleccion_estudiantes(self):
        self.boton_crear_estudiante = self.crear_botones(texto="Registrar Estudiante",
                                                        comando=lambda: self.cargar_ventana_crear_estudiante(),
                                                        color_boton=var.button_blue,
                                                        posicion_x=0.15,
                                                        posicion_y=0.20
                                                       )
        self.boton_ver_resultados = self.crear_botones(texto="Buscar Estudiante",
                                                        comando=self.consulta,
                                                        color_boton=var.button_blue,
                                                        posicion_x=0.35,
                                                        posicion_y=0.30
                                                       )

    # input de estudiantes
    def input_seleccion_estudiantes(self):
        self.input_buscar_estudiantes = ctk.CTkEntry(master=self.master,
                                            width=200,
                                            height=40,
                                            text_color=var.text_black,
                                            font=var.Andika_small_ultra,
                                            placeholder_text="Buscar por Cedula"
                                            )
        self.input_buscar_estudiantes.place(relx=0.078, rely=0.30,anchor="w")

    
    
    # texto estudiantes
    def texto_seleccion_estudiantes(self):
        self.texto_datos_de_alumnos = self.crear_texto(texto="Datos del Estudiante",
                                                        posicion_x=0.19,
                                                        posicion_y=0.5,
                                                        fuente=var.Amaranth_medium
                                                       )
        # datos # nombre Apellido Cedula Edad 
        self.texto_Numeral = self.crear_texto(texto="#",
                                                        posicion_x=0.085,
                                                        posicion_y=0.58,
                                                        fuente=var.Amaranth_small
                                                       )
        self.texto_Numeral = self.crear_texto(texto="Nombres",
                                                        posicion_x=0.18,
                                                        posicion_y=0.58,
                                                        fuente=var.Amaranth_small             
                                                       )
        self.texto_Numeral = self.crear_texto(texto="Apellidos",
                                                        posicion_x=0.34,
                                                        posicion_y=0.58,
                                                        fuente=var.Amaranth_small             
                                                       )
        self.texto_Numeral = self.crear_texto(texto="Cedula",
                                                        posicion_x=0.48,
                                                        posicion_y=0.58,
                                                        fuente=var.Amaranth_small             
                                                       )
        self.texto_Numeral = self.crear_texto(texto="Edad",
                                                        posicion_x=0.60,
                                                        posicion_y=0.58,
                                                        fuente=var.Amaranth_small             
                                                       )
        self.texto_Numeral = self.crear_texto(texto="Fecha de nacimiento",
                                                        posicion_x=0.74,
                                                        posicion_y=0.58,
                                                        fuente=var.Amaranth_small             
                                                       )
        self.texto_Numeral = self.crear_texto(texto="Acciones",
                                                        posicion_x=0.74,
                                                        posicion_y=0.58,
                                                        fuente=var.Amaranth_small             
                                                       )
    # Metodos  de creacion generales
    #Metodo para crear texto
    def crear_texto(self, posicion_x, posicion_y, texto,fuente):
        palabras = ctk.CTkLabel(master=self.master,
                                            text=texto,
                                            text_color=var.text_black,
                                            font=fuente
                                            )
        palabras.place(relx=posicion_x, rely=posicion_y,anchor="center")

        
    #Metodo para crear botones
    def crear_botones(self, texto, comando, color_boton, posicion_x, posicion_y):
        boton = ctk.CTkButton(master=self.master,
                             text=texto,
                             width=100,
                             height=40,
                             font=var.Andika_small_ultra,
                             fg_color=color_boton,
                             hover_color=var.hover_button_blue,
                             corner_radius=5,
                             command=comando
                             )
        
        boton.place(relx=posicion_x, rely=posicion_y,anchor="center")
        
        
    # logica de consulta 
    
    def consulta(self):
        cedula = self.input_buscar_estudiantes.get()
        print(cedula)