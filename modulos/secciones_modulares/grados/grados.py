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

def obtener_lista_estudiantes(id_grado):
    # Conectarse a la base de datos
    conn = sqlite3.connect('./bd_rufino/bd_escuela.db')
    c = conn.cursor()

    # Insertar valores en la tabla
    c.execute(f"SELECT cedula, primer_nombre, segundo_nombre, primer_apellido, segundo_apellido, fecha_nacimiento, genero FROM Estudiante WHERE id_grado = {id_grado}")
    result = c.fetchall()

    lista_prueba = []
    
    for element in result:
        cedula = str(element[0])
        nombre = f"{element[1]} {element[2]} {element[3]} {element[4]}"
        edad = str(calcular_edad(element[5]))
        fecha_nacimiento = str(element[5])
        genero = element[6]
        lista = (cedula, nombre, edad, fecha_nacimiento, genero)
        lista_prueba.append(lista)

    # Confirmar los cambios y cerrar la conexión
    conn.commit()
    conn.close()
    
    return lista_prueba


class GradosVentana:
    def __init__(self, master):
        self.master = master
        #cuando se cargue la ventana de grados se crean todos los pdf necesarios
        self.creacion_pdf(nombre="simoncito", lista=obtener_lista_estudiantes(id_grado=1))
        self.creacion_pdf(nombre="inicial_a", lista=obtener_lista_estudiantes(id_grado=2))
        self.creacion_pdf(nombre="inicial_b", lista=obtener_lista_estudiantes(id_grado=3))
        self.creacion_pdf(nombre="inicial_c", lista=obtener_lista_estudiantes(id_grado=4))
        self.creacion_pdf(nombre="1er_grado", lista=obtener_lista_estudiantes(id_grado=5))
        self.creacion_pdf(nombre="2do_grado", lista=obtener_lista_estudiantes(id_grado=6))
        self.creacion_pdf(nombre="3er_grado", lista=obtener_lista_estudiantes(id_grado=7))
        self.creacion_pdf(nombre="4to_grado", lista=obtener_lista_estudiantes(id_grado=8))
        self.creacion_pdf(nombre="5to_grado", lista=obtener_lista_estudiantes(id_grado=9))
        self.creacion_pdf(nombre="6to_grado", lista=obtener_lista_estudiantes(id_grado=10))
    
    
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