import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from modulos.variables import variables as var
from modulos.secciones_modulares.estudiantes.sub_estudiantes.crear_estudiante import CrearEstudianteVentana
from modulos.secciones_modulares.estudiantes.sub_estudiantes.modificar_estudiante import ModificarEstudianteVentana
from modulos.secciones_modulares.estudiantes.sub_estudiantes.eliminar_estudiante import eliminar_estudiante

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

    
    def cargar_ventana_modificar_estudiante(self, cedula):
        self.contenido_ventana_modificar_estudiante = ModificarEstudianteVentana(self.master, cedula)
        self.contenido_ventana_modificar_estudiante.mostrar()
    
    
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
        self.boton_modificar_representante = self.crear_botones(texto="Modificar Representante",
                                                        color_boton=var.button_blue,
                                                        comando=None,
                                                        posicion_x=0.8,
                                                        posicion_y=0.8
                                                       )
        self.boton_modificar_estudiante = self.crear_botones(texto="Modificar Estudiante",
                                                        comando=lambda: self.cargar_ventana_modificar_estudiante(self.input_buscar_estudiantes.get()),
                                                        color_boton=var.button_blue,
                                                        posicion_x=0.8,
                                                        posicion_y=0.20
                                                       )
        self.boton_eliminar_estudiante = self.crear_botones(texto="Eliminar Estudiante",
                                                        comando=lambda: eliminar_estudiante(self.input_buscar_estudiantes.get()),
                                                        color_boton=var.button_blue,
                                                        posicion_x=0.8,
                                                        posicion_y=0.9
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
        # variables: nombres Apellidos Cedula Edad fecha 
        self.texto_Datos_del_estudiante = self.crear_texto(texto="Datos Del Estudiante",
                                                        posicion_x=0.19,
                                                        posicion_y=0.50,
                                                        fuente=var.Amaranth_medium
                                                       )
        self.texto_Numeral = self.crear_texto(texto="#",
                                                        posicion_x=0.085,
                                                        posicion_y=0.58,
                                                        fuente=var.Amaranth_small
                                                       )
        self.texto_nombres = self.crear_texto(texto="Nombres",
                                                        posicion_x=0.18,
                                                        posicion_y=0.58,
                                                        fuente=var.Amaranth_small             
                                                       )
        self.texto_apellidos = self.crear_texto(texto="Apellidos",
                                                        posicion_x=0.34,
                                                        posicion_y=0.58,
                                                        fuente=var.Amaranth_small             
                                                       )
        self.texto_cedula = self.crear_texto(texto="Cedula",
                                                        posicion_x=0.48,
                                                        posicion_y=0.58,
                                                        fuente=var.Amaranth_small             
                                                       )
        self.texto_edad = self.crear_texto(texto="Edad",
                                                        posicion_x=0.60,
                                                        posicion_y=0.58,
                                                        fuente=var.Amaranth_small             
                                                       )
        self.texto_fecha = self.crear_texto(texto="Fecha de nacimiento",
                                                        posicion_x=0.74,
                                                        posicion_y=0.58,
                                                        fuente=var.Amaranth_small             
                                                       )
        self.texto_acciones = self.crear_texto(texto="Acciones",
                                                        posicion_x=0.88,
                                                        posicion_y=0.58,
                                                        fuente=var.Amaranth_small             
                                                       )
    def variables_seleccion_estudiantes(self,identificador,nombres,apellidos,cedula,edad,fecha):
        # datos # nombre Apellido Cedula Edad 
        self.var_id = self.crear_texto(texto=f"{identificador}",
                                                        posicion_x=0.085,
                                                        posicion_y=0.58,
                                                        fuente=var.Amaranth_small
                                                       )
        self.var_nombres = self.crear_texto(texto=f"{nombres}",
                                                        posicion_x=0.18,
                                                        posicion_y=0.58,
                                                        fuente=var.Amaranth_small             
                                                       )
        self.var_apellidos = self.crear_texto(texto=f"{apellidos}",
                                                        posicion_x=0.34,
                                                        posicion_y=0.58,
                                                        fuente=var.Amaranth_small             
                                                       )
        self.var_cedula = self.crear_texto(texto=f"{cedula}",
                                                        posicion_x=0.48,
                                                        posicion_y=0.58,
                                                        fuente=var.Amaranth_small             
                                                       )
        self.var_edad = self.crear_texto(texto=f"{edad}",
                                                        posicion_x=0.60,
                                                        posicion_y=0.58,
                                                        fuente=var.Amaranth_small             
                                                       )
        self.var_fecha = self.crear_texto(texto=f"{fecha}",
                                                        posicion_x=0.74,
                                                        posicion_y=0.58,
                                                        fuente=var.Amaranth_small             
                                                       )
        self.var_acciones = self.crear_texto(texto="Acciones",
                                                        posicion_x=0.88,
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
                             width=130,
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