import customtkinter as ctk
from datetime import date
import datetime
import sqlite3
from modulos.variables import variables as var
from PIL import ImageTk, Image
from modulos.crear_descargar_pdf.crear_pdf import CrearPDF
from modulos.secciones_modulares_docente.estudiantes_docente.estudiantes_docente import EstudiantesDocenteVentana
from modulos.secciones_modulares_docente.inicio_docente.inicio_docente import InicioDocenteVentana
from modulos.secciones_modulares_docente.perfil_docente.perfil_docente import PerfilDocenteVentana

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


class DashboardDocente:
    def __init__(self, master, cargo):
        self.master = master
        self.cargo = cargo
        self.nombre_archivo = self.cargo[2]
        id = self.decidir_id(self.nombre_archivo)
        self.creacion_pdf(nombre=self.nombre_archivo, lista=obtener_lista_estudiantes(id_grado=id))
    
    def mostrar(self):
        # Eliminar widgets anteriores en el área de contenido
        for widget in self.master.winfo_children():
            widget.destroy()
        
        # imagenes e iconos
        self.importar_img_ico()
        #datetime
        self.datetime()
        # cuadro principal
        self.area_principal_funcion()
        self.panel_izquierdo()
        self.elementos_panel_izquierdo()
        self.panel_superior()
        self.elementos_panel_superior()
    
    
    # importando imagenes e iconos
    def importar_img_ico(self):
        # importardo imagen
        self.icono_menu_png = Image.open("imagenes/icono_menu.png")
        self.icono_usuario_png = Image.open("imagenes/login-usuario-blanco.png")  
        # ajustando al tamaño deseado. imagen.resize((nuevo_ancho, nuevo_alto), suavizar y mejorar la calidad)
        self.icono_menu_ajustada = self.icono_menu_png.resize((79, 68), Image.LANCZOS)
        self.icono_usuario_ajustada = self.icono_usuario_png.resize((40, 40), Image.LANCZOS)
        # asignando a la variable que va a ser usada
        self.img_menu = ImageTk.PhotoImage(self.icono_menu_ajustada)
        self.img_usuario = ImageTk.PhotoImage(self.icono_usuario_ajustada)
    
    
    # incorporacion de frames y widgets
    def panel_izquierdo(self):
        self.panel_izquierdo = ctk.CTkFrame(master=self.master,
                                    width=196,
                                    height=720,
                                    fg_color=var.bg_gray,
                                    corner_radius=0)

        #------------------posicionamiento----------------------------------#
        self.panel_izquierdo.grid(row=0,column=0)
    
    
    def elementos_panel_izquierdo(self):
        # icono de menu
        self.icono_menu = ctk.CTkLabel(master=self.panel_izquierdo,
                                image=self.img_menu,
                                text="",
                                )
        
        # texto de menu
        self.texto_menu = ctk.CTkLabel(master=self.panel_izquierdo,
                                    text="Menu",
                                    font=var.Amaranth_medium_large,
                                    text_color=var.text_white
                                    )
        
        # botones del menu
        self.boton_inicio = ctk.CTkButton(master=self.panel_izquierdo,
                                        text="Inicio",
                                        width=185,
                                        font=var.Andika_small,
                                        hover_color=var.bg_blue,
                                        fg_color=var.bg_gray,
                                        anchor="sw",
                                        command=self.cargar_ventana_inicio
                                        )
        
        self.boton_estudiantes = ctk.CTkButton(master=self.panel_izquierdo,
                                        text="Estudiantes",
                                        width=185,
                                        font=var.Andika_small,
                                        hover_color=var.bg_blue,
                                        fg_color=var.bg_gray,
                                        anchor="sw",
                                        command=self.cargar_ventana_estudiantes
                                        )
        
        self.boton_perfil = ctk.CTkButton(master=self.panel_izquierdo,
                                        text="Perfil",
                                        width=185,
                                        font=var.Andika_small,
                                        hover_color=var.bg_blue,
                                        fg_color=var.bg_gray,
                                        anchor="sw",
                                        command=self.cargar_ventana_perfil
                                        )
        
        self.boton_salir = ctk.CTkButton(master=self.panel_izquierdo,
                                        text="Salir",
                                        width=160,
                                        font=var.Amaranth_small,
                                        fg_color=var.buttons_color,
                                        hover_color=var.hover_buttons_color,
                                        corner_radius=30,
                                        command=self.kill
                                        )
        
        #------------------posicionamiento------------------------------------
        self.icono_menu.place(relx=0.25, rely=0.01, anchor="n")
        self.texto_menu.place(relx=0.7,rely=0.030,anchor="n",)
        self.boton_inicio.place(relx=0.5,rely=0.4,anchor="center")
        self.boton_estudiantes.place(relx=0.5,rely=0.5,anchor="center")
        self.boton_perfil.place(relx=0.5,rely=0.6,anchor="center")
        self.boton_salir.place(relx=0.5,rely=0.91,anchor="s")
    
    
    #-------------------------funciones de botones-----------------------
    def panel_superior(self):
        self.panel_superior = ctk.CTkFrame(master=self.master,
                                    width=1084,
                                    height=80,
                                    fg_color=var.bg_blue,
                                    corner_radius=0)
        #------------------posicionamiento----------------------------------#
        self.panel_superior.grid(row=0,column=1,sticky="N")
    
    
    def elementos_panel_superior(self):
        self.icono_usuario = ctk.CTkLabel(master=self.panel_superior,
                                image=self.img_usuario,
                                text="",
                                )
        self.texto_usuario = ctk.CTkLabel(master=self.panel_superior,
                                text=f"Bienvenido {self.cargo[0]} - {self.cargo[1]}",
                                text_color=var.text_white,
                                font=var.Amaranth_small
                                )
        self.Hora_fecha = ctk.CTkLabel(master=self.panel_superior,
                                    text=f"Fecha actual: {self.fecha_actual} - Ingreso: {self.hora_actual}",
                                    text_color=var.text_white,
                                    font=var.Amaranth_small
                                    )
        #           posicionamiento
        self.icono_usuario.place(relx=0.02, rely=0.5, anchor="w")
        self.texto_usuario.place(relx=0.06, rely=0.55, anchor="w")
        self.Hora_fecha.place(relx=0.98,rely=0.5, anchor="e")
    
    
    def area_principal_funcion(self):
        self.area_contenido = ctk.CTkFrame(master=self.master,
                                    width=1084,
                                    height=640,
                                    corner_radius=0)
        self.cargar_ventana_inicio()
        #------------------posicionamiento----------------------------------#
        self.area_contenido.grid(column=1,row=0, sticky="s")
    
    
    #funcionalidad de los botones
    def cargar_ventana_estudiantes(self):
        contenido_estudiantes = EstudiantesDocenteVentana(master=self.area_contenido,
                                                          nombre_grado=self.cargo[1]
                                                         )
        contenido_estudiantes.pdf_a_img(nombre_archivo=self.nombre_archivo)
        contenido_estudiantes.mostrar()
    
    
    def cargar_ventana_inicio(self):
        contenido_inicio = InicioDocenteVentana(self.area_contenido, self.cargo[1])
        contenido_inicio.mostrar()
    
    
    def cargar_ventana_perfil(self):
        contenido_perfil = PerfilDocenteVentana(self.area_contenido, self.cargo[2])
        contenido_perfil.mostrar()
    
    
    def datetime(self):
        self.ahora = datetime.datetime.now()
        self.fecha_actual = self.ahora.strftime("%d/%m/%y")
        self.hora_actual = self.ahora.strftime("%I:%M%p")
    
    
    def kill(self):
        self.master.destroy()
    
    
    def creacion_pdf(self, nombre, lista):
        self.pdf_matricula = CrearPDF()
        self.pdf_matricula.creacion(nombre_pdf=nombre, lista=lista)
    
    
    def decidir_id(self, usuario):
        usuario = usuario
        if usuario == "simoncito":
          result = 1
        elif usuario == "inicial_a":
          result = 2
        elif usuario == "inicial_b":
          result = 3
        elif usuario == "inicial_c":
          result = 4
        elif usuario == "grado_1":
          result = 5
        elif usuario == "grado_2":
          result = 6
        elif usuario == "grado_3":
          result = 7
        elif usuario == "grado_4":
          result = 8
        elif usuario == "grado_5":
          result = 9
        elif usuario == "grado_6":
          result = 10
        return result