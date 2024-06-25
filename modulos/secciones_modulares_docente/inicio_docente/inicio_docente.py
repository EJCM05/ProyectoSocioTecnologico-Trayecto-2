import customtkinter as ctk
import sqlite3
from modulos.variables import variables as var
from modulos.secciones_modulares_docente.inicio_docente.crear_estadistica_general_docente import crear_estadistica_general
from PIL import ImageTk, Image

class InicioDocenteVentana:
    def __init__(self, master, nombre_grado, id):
        self.master = master
        self.nombre_grado = nombre_grado
        self.lista = None
        self.id = id

    def mostrar(self):
        # Eliminar widgets anteriores en el área de contenido
        for widget in self.master.winfo_children():
            widget.destroy()
        self.lista = self.obtener_lista_grados()
        crear_estadistica_general(self.lista)
        self.texto_titulo()
        self.texto_datos_generales()
        self.frame_graficos()
        self.graficos()

    def frame_graficos(self):
        self.frame_graficos = ctk.CTkFrame(master=self.master,
                                           width=700,
                                           height=500)
        self.frame_graficos.place(relx=0.5, rely=0.95, anchor="s")
    
    
    def graficos(self):
        img_estadistica_original = Image.open("matricula_pdf_img/img_estadistica_general/estadistica_general.png")
        img_estadistica_ajustada = img_estadistica_original.resize((560, 420), Image.LANCZOS)
        self.img_estadistica = ImageTk.PhotoImage(img_estadistica_ajustada)
        # aca van los graficos
        self.grafica = ctk.CTkLabel(master=self.frame_graficos,
                                    image=self.img_estadistica,
                                    text="")
        self.grafica.pack()
    
    
    def texto_titulo(self):
        self.texto_estadisticas = ctk.CTkLabel(master=self.master,
                                           text="Estadisticas Generales",
                                           text_color=var.text_black,
                                           font=var.Andika_large
                                           )
        
        self.texto_estadisticas.place(relx=0.5, rely=0.06, anchor="center")
    
    
    def texto_datos_generales(self):
        self.texto_estudiantes = self.crear_rectangulo_texto(nombre_texto="Estudiante",
                                                            dato_texto=self.sumar_estudiante_total(),
                                                            color_frame=var.est_color_blue,
                                                            posicion_x=0.4,
                                                            posicion_y=0.2,
                                                            tipo_posicion="normal"
                                                            )
        
        self.texto_aulas = self.crear_rectangulo_texto(nombre_texto="",
                                                      dato_texto=self.nombre_grado,
                                                      color_frame=var.est_color_orange,
                                                      posicion_x=0.6,
                                                      posicion_y=0.2,
                                                      tipo_posicion="central"
                                                      )
    
    
    def crear_rectangulo_texto(self, nombre_texto, dato_texto, color_frame, posicion_x, posicion_y, tipo_posicion):
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
        if tipo_posicion == "normal":
            texto_dato.place(relx=0.5, rely=0.68, anchor="center")
        elif tipo_posicion == "central":
            texto_dato.place(relx=0.5, rely=0.5, anchor="center")


    def obtener_lista_grados(self):
        # Conectarse a la base de datos
        conn = sqlite3.connect('./bd_rufino/bd_escuela.db')
        c = conn.cursor()

        # Insertar valores en la tabla
        c.execute(f"""SELECT G.grado_nombre, COUNT(E.id_estudiante) AS cantidad_alumnos FROM Grado G LEFT JOIN Estudiante E ON G.id_grado = E.id_grado GROUP BY G.id_grado, G.grado_nombre ORDER BY G.id_grado LIMIT 10;""")
        result = c.fetchall()

        lista = []
                
        for element in result:
            lista.append(element[1])

        # Confirmar los cambios y cerrar la conexión
        conn.commit()
        conn.close()
        return lista
        
    def obtener_lista_estudiante(self):    
      # Conectarse a la base de datos
        conn = sqlite3.connect('./bd_rufino/bd_escuela.db')
        c = conn.cursor()

        # Insertar valores en la tabla
        c.execute(f"""SELECT id_estudiante, COUNT(*) AS count FROM Estudiante WHERE id_grado = {self.id};""")
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

    def sumar_estudiante_total(self):
          lista = self.obtener_lista_estudiante()
          
          # Usamos la función sum para sumar todos los elementos de la lista
          suma_total = sum(lista)

          return suma_total
          