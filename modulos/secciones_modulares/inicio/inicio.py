import customtkinter as ctk
import tkinter as tk
import sqlite3
from modulos.variables import variables as var

class InicioVentana:
    def __init__(self, master):
        self.master = master

    def mostrar(self):
        # Eliminar widgets anteriores en el área de contenido
        for widget in self.master.winfo_children():
            widget.destroy()
        self.texto_titulo()
        self.texto_datos_generales()
        self.obtener_lista_grados()
        self.frame_graficos()

    def frame_graficos(self):
        self.frame_graficos = ctk.CTkFrame(master=self.master,
                                           width=600,
                                           height=400)
        self.frame_graficos.place(relx=0.5, rely=0.65, anchor="center")
        self.graficos()
        

    def graficos(self):
        # aca van los graficos
        self.frame_grafico = ctk.CTkFrame(master=self.master, width=600, height=400)
        self.frame_grafico.place(relx=0.5, rely=0.65, anchor="center")

        # Datos de ejemplo (puedes reemplazarlos con tus propios datos)
        x = [1, 2, 3, 4, 5]
        y = [10, 15, 7, 12, 20]
        
    def texto_titulo(self):
        self.texto_estadisticas = ctk.CTkLabel(master=self.master,
                                           text="Estadisticas Generales",
                                           text_color=var.text_black,
                                           font=var.Andika_large
                                           )
        
        self.texto_estadisticas.place(relx=0.5, rely=0.06, anchor="center")
    
    
    def texto_datos_generales(self):
        self.texto_estudiantes = self.crear_rectangulo_texto(nombre_texto="Estudiante",
                                                            dato_texto=self.sumar_estudiante_lista(),
                                                            color_frame=var.est_color_blue,
                                                            posicion_x=0.1,
                                                            posicion_y=0.2
                                                            )
        
        self.texto_docentes = self.crear_rectangulo_texto(nombre_texto="Docentes",
                                                         dato_texto="10",
                                                         color_frame=var.est_color_gray,
                                                         posicion_x=0.3,
                                                         posicion_y=0.2
                                                         )
        
        self.texto_obreros = self.crear_rectangulo_texto(nombre_texto="Obreros",
                                                        dato_texto="10",
                                                        color_frame=var.est_color_pink,
                                                        posicion_x=0.5,
                                                        posicion_y=0.2
                                                        )
        
        self.texto_aulas = self.crear_rectangulo_texto(nombre_texto="Aulas",
                                                      dato_texto="10",
                                                      color_frame=var.est_color_orange,
                                                      posicion_x=0.7,
                                                      posicion_y=0.2
                                                      )
        
        self.texto_especialistas = self.crear_rectangulo_texto(nombre_texto="Especialistas",
                                                              dato_texto="10",
                                                              color_frame=var.est_color_grayBlack,
                                                              posicion_x=0.9,
                                                              posicion_y=0.2
                                                              )
    
    
    def crear_rectangulo_texto(self, nombre_texto, dato_texto, color_frame, posicion_x, posicion_y):
        contenedor = ctk.CTkFrame(master=self.master,
                                 width=160,
                                 height=100,
                                 corner_radius=20,
                                 fg_color=color_frame,
                                 )
        
        texto_nombre = ctk.CTkLabel(master=contenedor,
                                   text=nombre_texto,
                                   text_color=var.text_white,
                                   font=var.Amaranth_medium,
                                   )
        
        texto_dato = ctk.CTkLabel(master=contenedor,
                                 text=dato_texto,
                                 text_color=var.text_white,
                                 font=var.Amaranth_medium
                                 )
        
        contenedor.place(relx=posicion_x, rely=posicion_y, anchor="center")
        texto_nombre.place(relx=0.5, rely=0.32, anchor="center")
        texto_dato.place(relx=0.5, rely=0.68, anchor="center")

    def obtener_lista_grados(self):
        # Conectarse a la base de datos
        conn = sqlite3.connect('./bd_rufino/bd_escuela.db')
        c = conn.cursor()

        # Insertar valores en la tabla
        c.execute(f"SELECT id_grado, COUNT(*) AS cantidad_estudiantes FROM Estudiante GROUP BY id_grado;")
        result = c.fetchall()
        
        lista = []
        
        for element in result:
          lista.append(element[1])

        # Confirmar los cambios y cerrar la conexión
        conn.commit()
        conn.close()
        return lista
        
    def sumar_estudiante_lista(self):
      lista = self.obtener_lista_grados()
      
      # Usamos la función sum para sumar todos los elementos de la lista
      suma_total = sum(lista)

      return suma_total
 