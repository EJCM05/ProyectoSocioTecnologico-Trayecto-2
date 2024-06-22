import customtkinter as ctk
from modulos.variables import variables as var
from modulos.secciones_modulares.grados.sub_grados.sub_grados import SubGradosVentana
from modulos.crear_descargar_pdf.crear_pdf import CrearPDF
import sqlite3
from datetime import datetime, date

def calcular_edad(fecha_nacimiento):
    año, mes, dia = fecha_nacimiento.split("/")
    año = int(año)
    mes = int(mes)
    dia = int(dia)
    
    fecha_nacimiento = date(año, mes, dia)
    
    # Obtener la fecha actual
    hoy = date.today()
    
    # Calcular la edad en años
    edad = hoy.year - fecha_nacimiento.year - ((hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
    
    return edad

def lista_grado_simoncito():
  # Conectarse a la base de datos
  conn = sqlite3.connect('./bd_rufino/bd_escuela.db')
  c = conn.cursor()

  # Insertar valores en la tabla
  c.execute("SELECT cedula, primer_nombre, segundo_nombre, primer_apellido, segundo_apellido, fecha_nacimiento FROM Estudiante WHERE id_grado = 1")
  result = c.fetchall()

  lista_prueba_1 = []

  for element in result:
    cedula = str(element[0])
    nombre = f"{element[1]} {element[2]} {element[3]} {element[4]}"
    edad = str(calcular_edad(element[5]))
    fecha_nacimiento = str(element[5])
    lista = (cedula, nombre, edad, fecha_nacimiento, "")
    lista_prueba_1.append(lista)

  # Confirmar los cambios y cerrar la conexión
  conn.commit()
  conn.close()
  
  return lista_prueba_1

def lista_grado_inicial_a():
  # Conectarse a la base de datos
  conn = sqlite3.connect('./bd_rufino/bd_escuela.db')
  c = conn.cursor()

  # Insertar valores en la tabla
  c.execute("SELECT cedula, primer_nombre, segundo_nombre, primer_apellido, segundo_apellido, fecha_nacimiento FROM Estudiante WHERE id_grado = 2")
  result = c.fetchall()

  lista_prueba_2 = [
      ("1", "Oswaldo Antonio Urdaneta Moncada", "7", "2000/02/10",""),]

  for element in result:
    cedula = str(element[0])
    nombre = f"{element[1]} {element[2]} {element[3]} {element[4]}"
    edad = str(calcular_edad(element[5]))
    fecha_nacimiento = str(element[5])
    lista = (cedula, nombre, edad, fecha_nacimiento, "")
    lista_prueba_2.append(lista)

  # Confirmar los cambios y cerrar la conexión
  conn.commit()
  conn.close()
  
  return lista_prueba_2

lista_prueba_3 = [
    ("3", "Oswaldo Antonio Urdaneta Moncada", "7", "10/Febrero/2000",""),]
lista_prueba_4 = [
    ("4", "Oswaldo Antonio Urdaneta Moncada", "7", "10/Febrero/2000",""),]
lista_prueba_5 = [
    ("5", "Oswaldo Antonio Urdaneta Moncada", "7", "10/Febrero/2000",""),]
lista_prueba_6 = [
    ("6", "Oswaldo Antonio Urdaneta Moncada", "7", "10/Febrero/2000",""),]
lista_prueba_7 = [
    ("7", "Oswaldo Antonio Urdaneta Moncada", "7", "10/Febrero/2000",""),]
lista_prueba_8 = [
    ("8", "Oswaldo Antonio Urdaneta Moncada", "7", "10/Febrero/2000",""),]
lista_prueba_9 = [
    ("9", "Oswaldo Antonio Urdaneta Moncada", "7", "10/Febrero/2000",""),]
lista_prueba_10 = [
    ("10", "Oswaldo Antonio Urdaneta Moncada", "7", "10/Febrero/2000",""),
    ("10", "Oswaldo Antonio Urdaneta Moncada", "7", "10/Febrero/2000",""),
    ("10", "Oswaldo Antonio Urdaneta Moncada", "7", "10/Febrero/2000","")]


class GradosVentana:
    def __init__(self, master):
        self.master = master
        #cuando se cargue la ventana de grados se crean todos los pdf necesarios
        self.creacion_pdf(nombre="simoncito", lista=lista_grado_simoncito())
        self.creacion_pdf(nombre="inicial_a", lista=lista_grado_inicial_a())
        self.creacion_pdf(nombre="inicial_b", lista=lista_prueba_3)
        self.creacion_pdf(nombre="inicial_c", lista=lista_prueba_4)
        self.creacion_pdf(nombre="1er_grado", lista=lista_prueba_5)
        self.creacion_pdf(nombre="2do_grado", lista=lista_prueba_6)
        self.creacion_pdf(nombre="3er_grado", lista=lista_prueba_7)
        self.creacion_pdf(nombre="4to_grado", lista=lista_prueba_8)
        self.creacion_pdf(nombre="5to_grado", lista=lista_prueba_9)
        self.creacion_pdf(nombre="6to_grado", lista=lista_prueba_10)
    
    
    def creacion_pdf(self, nombre, lista):
        self.pdf_matricula = CrearPDF()
        self.pdf_matricula.creacion(nombre_pdf=nombre, lista=lista)
    
    
    def mostrar(self):
        # Eliminar widgets anteriores en el área de contenido
        for widget in self.master.winfo_children():
            widget.destroy()
        
        self.texto_titulo()
        self.botones_seleccion_grado()
    
    
    def cargar_ventana_sub_grados(self, nombre_grado, nombre_archivo):
        self.contenido_sub_grados = SubGradosVentana(master=self.master,
                                                     nombre_grado= nombre_grado,
                                                    )
        self.contenido_sub_grados.pdf_a_img(nombre_archivo=nombre_archivo)
        self.contenido_sub_grados.mostrar()
    
    
    def texto_titulo(self):
        self.texto_seleccion = ctk.CTkLabel(master=self.master,
                                           text="Selecciona un Grado",
                                           text_color=var.text_black,
                                           font=var.Andika_large
                                           )
        
        self.texto_seleccion.place(relx=0.5, rely=0.06, anchor="center")
    
    
    def botones_seleccion_grado(self):
        self.boton_simoncito = self.crear_botones_grado(texto="Simoncito",
                                                        comando=lambda: self.cargar_ventana_sub_grados(nombre_grado="Simoncito",nombre_archivo="simoncito"),
                                                        color_boton=var.btn_gray,
                                                        posicion_x=0.15,
                                                        posicion_y=0.45
                                                       )
        
        self.boton_inicial_a = self.crear_botones_grado(texto="Inicial A",
                                                        comando=lambda: self.cargar_ventana_sub_grados(nombre_grado="Inicial A", nombre_archivo="inicial_a"),
                                                        color_boton=var.btn_pink,
                                                        posicion_x=0.35,
                                                        posicion_y=0.45
                                                       )
        
        self.boton_inicial_b = self.crear_botones_grado(texto="Inicial B",
                                                        comando=lambda: self.cargar_ventana_sub_grados(nombre_grado="Inicial B", nombre_archivo="inicial_b"),
                                                        color_boton=var.btn_beige,
                                                        posicion_x=0.15,
                                                        posicion_y=0.65
                                                       )
        
        self.boton_inicial_c = self.crear_botones_grado(texto="Inicial C",
                                                        comando=lambda: self.cargar_ventana_sub_grados(nombre_grado="Inicial C", nombre_archivo="inicial_c"),
                                                        color_boton=var.btn_gold,
                                                        posicion_x=0.35,
                                                        posicion_y=0.65
                                                       )
        
        self.boton_1er_grado = self.crear_botones_grado(texto="1er Grado",
                                                        comando=lambda: self.cargar_ventana_sub_grados(nombre_grado="1er Grado", nombre_archivo="1er_grado"),
                                                        color_boton=var.btn_blue,
                                                        posicion_x=0.65,
                                                        posicion_y=0.35
                                                       )
        
        self.boton_2do_grado = self.crear_botones_grado(texto="2do Grado",
                                                        comando=lambda: self.cargar_ventana_sub_grados(nombre_grado="2do Grado", nombre_archivo="2do_grado"),
                                                        color_boton=var.btn_red_black,
                                                        posicion_x=0.65,
                                                        posicion_y=0.55
                                                       )
        
        self.boton_3er_grado = self.crear_botones_grado(texto="3er Grado",
                                                        comando=lambda: self.cargar_ventana_sub_grados(nombre_grado="3er Grado", nombre_archivo="3er_grado"),
                                                        color_boton=var.btn_purple,
                                                        posicion_x=0.65,
                                                        posicion_y=0.75
                                                       )
        
        self.boton_4to_grado = self.crear_botones_grado(texto="4to Grado",
                                                        comando=lambda: self.cargar_ventana_sub_grados(nombre_grado="4to Grado", nombre_archivo="4to_grado"),
                                                        color_boton=var.btn_green,
                                                        posicion_x=0.85,
                                                        posicion_y=0.35
                                                       )
        
        self.boton_5to_grado = self.crear_botones_grado(texto="5to Grado",
                                                        comando=lambda: self.cargar_ventana_sub_grados(nombre_grado="5to Grado", nombre_archivo="5to_grado"),
                                                        color_boton=var.btn_lila,
                                                        posicion_x=0.85,
                                                        posicion_y=0.55
                                                       )
        
        self.boton_6to_grado = self.crear_botones_grado(texto="6to Grado",
                                                        comando=lambda: self.cargar_ventana_sub_grados(nombre_grado="6to Grado", nombre_archivo="6to_grado"),
                                                        color_boton=var.btn_blueosc,
                                                        posicion_x=0.85,
                                                        posicion_y=0.75
                                                       )
    
    
    def crear_botones_grado(self, texto, comando, color_boton, posicion_x, posicion_y):
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