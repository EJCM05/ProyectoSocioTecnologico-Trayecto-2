import customtkinter as ctk
from modulos.variables import variables as var
from modulos.secciones_modulares.personal.sub_personal.sub_personal import SubPersonalVentana
from modulos.crear_descargar_pdf.crear_pdf_personal import CrearPDFPersonal
import sqlite3
from datetime import datetime, date
from PIL import ImageTk, Image

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

def obtener_lista_personal(id_personal):
    # Conectarse a la base de datos
    conn = sqlite3.connect('./bd_rufino/bd_escuela.db')
    c = conn.cursor()

    # Insertar valores en la tabla
    c.execute(f"SELECT id_personal, primer_nombre, segundo_nombre, primer_apellido, segundo_apellido, fecha_nacimiento, cedula, genero FROM Personal WHERE id_personal = {id_personal}")
    result = c.fetchall()

    lista_prueba = []
    
    for element in result:
        personal_id = str(element[0])
        nombre = f"{element[1]} {element[2]} {element[3]} {element[4]}"
        edad = str(calcular_edad(element[5]))
        fecha_nacimiento = str(element[5])
        cedula = str(element[6])
        genero = element[7]
        lista = (cedula, nombre, edad, fecha_nacimiento, genero)
        lista_prueba.append(lista)

    # Confirmar los cambios y cerrar la conexión
    conn.commit()
    conn.close()
    
    return lista_prueba


class PersonalVentana:
    def __init__(self, master):
        self.master = master
        #cuando se cargue la ventana de grados se crean todos los pdf necesarios
        self.creacion_pdf(nombre="obrero", lista=obtener_lista_personal(id_personal='1'))
        self.creacion_pdf(nombre="docente", lista=obtener_lista_personal(id_personal='2'))
        self.creacion_pdf(nombre="especialista", lista=obtener_lista_personal(id_personal="3"))
    
    
    def creacion_pdf(self, nombre, lista):
        self.pdf_matricula = CrearPDFPersonal()
        self.pdf_matricula.creacion(nombre_pdf=nombre, lista=lista)
    
    
    def mostrar(self):
        # Eliminar widgets anteriores en el área de contenido
        for widget in self.master.winfo_children():
            widget.destroy()
        
        self.texto_titulo()
        self.botones_seleccion_personal()
        self.importar_img_ico()
        self.imagen_de_personal()
    
    
    def cargar_ventana_sub_personal(self, nombre_personal):
        self.contenido_sub_personal = SubPersonalVentana(master=self.master,
                                                     nombre_personal = nombre_personal
                                                    )
        self.contenido_sub_personal.mostrar()
    
    
    def texto_titulo(self):
        self.texto_seleccion = ctk.CTkLabel(master=self.master,
                                           text="Personal",
                                           text_color=var.text_black,
                                           font=var.Amaranth_medium_large
                                           )
        
        self.texto_seleccion.place(relx=0.5, rely=0.06, anchor="center")
    
    
    def botones_seleccion_personal(self):
        self.boton_obrero = self.crear_botones_personal(texto="Obrero",
                                                        comando=lambda: self.cargar_ventana_sub_personal(nombre_personal="Obrero"),
                                                        color_boton=var.btn_gold,
                                                        posicion_x=0.74,
                                                        posicion_y=0.3
                                                       )
        self.boton_docente = self.crear_botones_personal(texto="Docente",
                                                        comando=lambda: self.cargar_ventana_sub_personal(nombre_personal="Docente"),
                                                        color_boton=var.btn_green,
                                                        posicion_x=0.74,
                                                        posicion_y=0.5
                                                       )
        self.boton_especialista = self.crear_botones_personal(texto="Especialista",
                                                        comando=lambda: self.cargar_ventana_sub_personal(nombre_personal="Especialista"),
                                                        color_boton=var.btn_blueosc,
                                                        posicion_x=0.74,
                                                        posicion_y=0.7
                                                       )
    
    
    def crear_botones_personal(self, texto, comando, color_boton, posicion_x, posicion_y):
        boton = ctk.CTkButton(master=self.master,
                             text=texto,
                             width=220,
                             height=70,
                             font=var.Amaranth_medium,
                             fg_color=color_boton,
                             hover_color=var.hover_buttons_color,
                             corner_radius=10,
                             command=comando
                             )
        
        boton.place(relx=posicion_x, rely=posicion_y, anchor="center")
    
    
    def importar_img_ico(self):
        self.icono_user_original = Image.open("imagenes/imagen_teamwork.png")
        self.icono_user_ajustada = self.icono_user_original.resize((500, 380), Image.LANCZOS)
        self.img_icono_user = ImageTk.PhotoImage(self.icono_user_ajustada)

    def imagen_de_personal(self):
        self.carga_imagen_personal = ctk.CTkLabel(master=self.master,
                                                    image=self.img_icono_user,
                                                    text="")
        self.carga_imagen_personal.place(relx=0.3,rely=0.5,anchor="center")