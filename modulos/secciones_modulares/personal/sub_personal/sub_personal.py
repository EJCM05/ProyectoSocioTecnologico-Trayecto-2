import customtkinter as ctk
from modulos.variables import variables as var
from modulos.secciones_modulares.personal.sub_personal.crear_personal import CrearPersonalVentana
from modulos.secciones_modulares.personal.sub_personal.ver_lista_personal import VerListaPersonalVentana
from modulos.secciones_modulares.personal.sub_personal.modificar_personal import ModificarPersonalVentana
import sqlite3
from modulos.secciones_modulares.personal.sub_personal.eliminar_personal import eliminar_personal
from CTkMessagebox import CTkMessagebox
from PIL import ImageTk, Image

class SubPersonalVentana:
    def __init__(self, master, nombre_personal):
        self.master = master
        self.nombre_personal = nombre_personal
        self.decidir_personal()
    
    
    def mostrar(self):
        # Eliminar widgets anteriores en el área de contenido
        for widget in self.master.winfo_children():
            widget.destroy()
        
        self.frame_texto_blanco()
        self.texto_titulo()
        self.botones_personal()
        self.importar_img_ico()
        self.input_seleccion_personal()
        self.imagen_de_usuario()
    
    
    def decidir_personal(self):
        if self.nombre_personal == "Obrero":
            self.tipo_personal = 1
            self.nombre_imagen = "obrero"
        elif self.nombre_personal == "Docente":
            self.tipo_personal = 2
            self.nombre_imagen = "docente"
        elif self.nombre_personal == "Especialista":
            self.tipo_personal = 3
            self.nombre_imagen = "especialista"
    
    
    def importar_img_ico(self):
        self.icono_user_original = Image.open(f"imagenes/imagen_{self.nombre_imagen}.png")
        self.icono_user_ajustada = self.icono_user_original.resize((250, 250), Image.LANCZOS)
        self.img_icono_user = ImageTk.PhotoImage(self.icono_user_ajustada)

    def imagen_de_usuario(self):
        self.carga_imagen_estudiante = ctk.CTkLabel(master=self.master,
                                                    image=self.img_icono_user,
                                                    text="",
                                                    fg_color="#FFFFFF")
        self.carga_imagen_estudiante.place(relx=0.5,rely=0.6,anchor="center")
    
    
    def cargar_ventana_crar_personal(self, nombre_personal):
        self.contenido_crear_personal = CrearPersonalVentana(master=self.master,
                                                     nombre_personal = nombre_personal,
                                                     tipo_personal=self.tipo_personal
                                                    )
        self.contenido_crear_personal.mostrar()
    
    
    def cargar_ventana_modificar_personal(self, cedula):
        self.contenido_ventana_modificar_personal = ModificarPersonalVentana(self.master, cedula)
        self.contenido_ventana_modificar_personal.mostrar()
    
    
    def cargar_ventana_ver_lista_personal(self, nombre_personal):
        self.contenido_ver_lista_personal = VerListaPersonalVentana(master=self.master,
                                                     nombre_personal = nombre_personal
                                                    )
        self.contenido_ver_lista_personal.pdf_a_img(nombre_archivo=self.nombre_personal)
        self.contenido_ver_lista_personal.mostrar()
    
    
    def texto_titulo(self):
        self.texto_seleccion = ctk.CTkLabel(master=self.master,
                                           text=f"Personal {self.nombre_personal}",
                                           text_color=var.text_black,
                                           font=var.Andika_large
                                           )
        
        self.texto_seleccion.place(relx=0.5, rely=0.06, anchor="center")
    
    
    def frame_texto_blanco(self):
        self.frame_fondo_blanco = ctk.CTkFrame(master=self.master,
                                               width=1000,
                                               height=300,
                                               fg_color="white",
                                               corner_radius=20
                                                )
        self.frame_fondo_blanco.place(relx=0.5,rely=0.6,anchor="center")
    
    
    def botones_personal(self):
        self.texto_ingrese_cedula = ctk.CTkLabel(master=self.master,
                                           text="Ingrese La Cedula",
                                           text_color=var.text_black,
                                           font=var.Andika_small
                                           )
        self.texto_ingrese_cedula.place(relx=0.15, rely=0.24, anchor="center")
        
        self.boton_crear_personal = self.crear_botones_personal(texto="Registrar Personal",
                                                        comando=lambda: self.cargar_ventana_crar_personal(nombre_personal=self.nombre_personal),
                                                        color_boton=var.button_blue,
                                                        posicion_x=0.15,
                                                        posicion_y=0.15,
                                                        tamaño="normal"
                                                       )
        self.boton_ver_lista_personal = self.crear_botones_personal(texto="Ver lista Personal",
                                                        comando=lambda: self.cargar_ventana_ver_lista_personal(nombre_personal=self.nombre_personal),
                                                        color_boton=var.button_blue,
                                                        posicion_x=0.5,
                                                        posicion_y=0.9,
                                                        tamaño="largo"
                                                       )
        self.boton_ver_resultados = self.crear_botones_personal(texto="Buscar Personal",
                                                        comando=self.consulta,
                                                        color_boton=var.button_blue,
                                                        posicion_x=0.35,
                                                        posicion_y=0.30,
                                                        tamaño="normal"
                                                       )
    
    
    def variables_seleccion_personal(self):
        cedula = self.input_buscar_personal.get()
        
        # Conectarse a la base de datos
        conn = sqlite3.connect('./bd_rufino/bd_escuela.db')
        c = conn.cursor()

        # Insertar valores en la tabla
        c.execute(f"SELECT cedula, primer_nombre, segundo_nombre, primer_apellido, segundo_apellido, genero, fecha_nacimiento FROM Personal WHERE cedula = {cedula} AND id_personal = {self.tipo_personal}")
        info = c.fetchall()
        
        for element in info:
          nombres = f"{element[1]} {element[2]}"
          apellidos = f"{element[3]} {element[4]}"
          cedula = element[0]
          genero = element[5]
          fecha_nacimiento = element[6]

        # Confirmar los cambios y cerrar la conexión
        conn.commit()
        conn.close()
      
        # datos # nombre Apellido Cedula Edad 
        lista_datos = (
            nombres,
            apellidos,
            cedula,
            genero,
            fecha_nacimiento
        )
        self.var_nombres = self.crear_texto_center(texto=lista_datos[0],
                                                        posicion_x=0.15,
                                                        posicion_y=0.64,
                                                        fuente=var.Amaranth_small             
                                                       )
        self.var_apellidos = self.crear_texto_center(texto=lista_datos[1],
                                                        posicion_x=0.28,
                                                        posicion_y=0.64,
                                                        fuente=var.Amaranth_small             
                                                       )
        self.var_cedula = self.crear_texto_center(texto=f"V{lista_datos[2]}",
                                                        posicion_x=0.41,
                                                        posicion_y=0.64,
                                                        fuente=var.Amaranth_small             
                                                       )
        self.var_edad = self.crear_texto_center(texto=lista_datos[3],
                                                        posicion_x=0.51,
                                                        posicion_y=0.64,
                                                        fuente=var.Amaranth_small             
                                                       )
        self.var_fecha = self.crear_texto_center(texto=lista_datos[4],
                                                        posicion_x=0.65,
                                                        posicion_y=0.64,
                                                        fuente=var.Amaranth_small             
                                                       )
    
    
    
    # input de personal
    def input_seleccion_personal(self):
        validacion_numeros = self.master.register(self.solo_numeros)
        self.input_buscar_personal = ctk.CTkEntry(master=self.master,
                                            width=200,
                                            height=40,
                                            text_color=var.text_black,
                                            font=var.Andika_small_ultra,
                                            validate="key",
                                            validatecommand=(validacion_numeros,'%S')
                                            )
        self.input_buscar_personal.place(relx=0.080, rely=0.30,anchor="w")
    
    
    # texto estudiantes
    def texto_seleccion_personal(self):
        # variables: nombres Apellidos Cedula Edad fecha 
        self.texto_Datos_del_estudiante = self.crear_texto(texto="Datos del Personal",
                                                        posicion_x=0.12,
                                                        posicion_y=0.50,
                                                        fuente=var.Amaranth_medium
                                                       )
        self.texto_nombres = self.crear_texto(texto="Nombres",
                                                        posicion_x=0.12,
                                                        posicion_y=0.58,
                                                        fuente=var.Amaranth_small             
                                                       )
        self.texto_apellidos = self.crear_texto(texto="Apellidos",
                                                        posicion_x=0.25,
                                                        posicion_y=0.58,
                                                        fuente=var.Amaranth_small             
                                                       )
        self.texto_cedula = self.crear_texto(texto="Cedula",
                                                        posicion_x=0.38,
                                                        posicion_y=0.58,
                                                        fuente=var.Amaranth_small             
                                                       )
        self.texto_edad = self.crear_texto(texto="Genero",
                                                        posicion_x=0.48,
                                                        posicion_y=0.58,
                                                        fuente=var.Amaranth_small             
                                                       )
        self.texto_fecha = self.crear_texto(texto="Fecha De Nacimiento",
                                                        posicion_x=0.57,
                                                        posicion_y=0.58,
                                                        fuente=var.Amaranth_small             
                                                       )
        self.texto_acciones = self.crear_texto(texto="Acciones",
                                                        posicion_x=0.79,
                                                        posicion_y=0.58,
                                                        fuente=var.Amaranth_small             
                                                       )
        self.boton_modificar_personal = self.crear_boton_simple(texto="Editar",
                                                        comando=lambda: self.cargar_ventana_modificar_personal(self.input_buscar_personal.get()),
                                                        color_boton=var.button_transparent,
                                                        color_text=var.text_blue,
                                                        posicion_x=0.80,
                                                        posicion_y=0.64
                                                       )
        self.boton_eliminar_personal = self.crear_boton_simple(texto="Borrar",
                                                        comando=lambda: eliminar_personal(self.input_buscar_personal.get()),
                                                        color_boton=var.button_transparent,
                                                        color_text=var.text_blue,
                                                        posicion_x=0.85,
                                                        posicion_y=0.64
                                                       )
    
    
    #Metodo para crear texto
    def crear_texto(self, posicion_x, posicion_y, texto,fuente):
        palabras = ctk.CTkLabel(master=self.master,
                                            text=texto,
                                            text_color=var.text_black,
                                            font=fuente,
                                            fg_color="white"
                                            )
        palabras.place(relx=posicion_x, rely=posicion_y,anchor="w")
    
    def crear_texto_center(self, posicion_x, posicion_y, texto,fuente):
        palabras = ctk.CTkLabel(master=self.master,
                                            text=texto,
                                            text_color=var.text_black,
                                            font=fuente,
                                            fg_color="white"
                                            )
        palabras.place(relx=posicion_x, rely=posicion_y,anchor="center")
    
    
    def crear_botones_personal(self, texto, comando, color_boton, posicion_x, posicion_y, tamaño):
        if tamaño == "normal":
            ancho = 130
            alto = 40
        elif tamaño == "largo":
            ancho = 250
            alto = 40
        
        boton = ctk.CTkButton(master=self.master,
                             text=texto,
                             width=ancho,
                             height=alto,
                             font=var.Amaranth_small,
                             fg_color=color_boton,
                             hover_color=var.hover_buttons_color,
                             corner_radius=10,
                             command=comando
                             )
        
        boton.place(relx=posicion_x, rely=posicion_y, anchor="center")
    
    
    def crear_boton_simple(self, texto,color_text, comando, color_boton, posicion_x, posicion_y):
        boton = ctk.CTkButton(master=self.master,
                             text=texto,
                             width=20,
                             height=20,
                             font=var.Andika_small_ultra,
                             fg_color=color_boton,
                             text_color=color_text,
                             hover_color=var.hover_button_transparent,
                             corner_radius=5,
                             command=comando
                             )
        
        boton.place(relx=posicion_x, rely=posicion_y,anchor="center")
    
    def consulta(self):
        self.frame_texto_blanco()
        cedula = self.input_buscar_personal.get()
        if cedula:
            try:
                cedula = int(cedula)
        # Resto de tu código aquí
            except ValueError:
                texto_emergente = "No se encuentra una cedula registrada"
                CTkMessagebox(title="Error", message=texto_emergente,font=("calibri",16),icon="cancel")
        
        # Conectarse a la base de datos
        conn = sqlite3.connect('./bd_rufino/bd_escuela.db')
        c = conn.cursor()

        # Insertar valores en la tabla
        c.execute(f"SELECT cedula FROM Personal WHERE id_personal = {self.tipo_personal}")
        info = c.fetchall()

        # Confirmar los cambios y cerrar la conexión
        conn.commit()
        conn.close()
        
        lista_cedulas = []
        
        for element in info:
          lista_cedulas.append(element[0])
        
        if cedula in lista_cedulas:
            self.texto_seleccion_personal()
            self.variables_seleccion_personal()
            self.variables_seleccion_personal()
        else:
            texto_emergente = "No se encuentra una cedula registrada"
            CTkMessagebox(title="Error", message=texto_emergente,font=("calibri",16),icon="cancel")
            self.imagen_de_usuario()
    
    
    def solo_numeros(self, char):
        return char.isdigit() # solo numeros