import customtkinter as ctk
import sqlite3
from modulos.variables import variables as var
from modulos.secciones_modulares.estudiantes.sub_estudiantes.sub_crear_estudiantes.grado_registrar import GradoRegistrarVentana
from CTkMessagebox import CTkMessagebox

class DatosRepresentanteVentana():
    def __init__(self, master):
        self.master = master
    
    
    def mostrar(self):
        # Eliminar widgets anteriores en el área de contenido
        for widget in self.master.winfo_children():
            widget.destroy()
        
        self.texto_titulo()
        self.area_input_principal()
        self.area_input_izquierda()
        self.area_input_derecha()
    
    
    def texto_titulo(self):
        self.texto_seleccion = ctk.CTkLabel(master=self.master,
                                           text="Datos del Representante",
                                           text_color=var.text_black,
                                           font=var.Andika_large
                                           )
        
        self.texto_seleccion.place(relx=0.5, rely=0.06, anchor="center")
    
    
    def area_input_principal(self):
        #contenedor principal de los inputs
        self.contenedor_input_izquierda = ctk.CTkFrame(master=self.master,
                                 width=370,
                                 height=450,
                                 corner_radius=40,
                                 fg_color=var.btn_gray
                                 )
        self.contenedor_input_derecha = ctk.CTkFrame(master=self.master,
                                 width=370,
                                 height=450,
                                 corner_radius=40,
                                 fg_color=var.btn_gray
                                 )
        #------boton continuar------
        self.boton_continuar = self.crear_botones_estudiantes(texto="Continuar",
                                                        comando=self.verificar_espacios,
                                                        color_boton=var.buttons_color,
                                                        posicion_x=0.5,
                                                        posicion_y=0.9
                                                       )
        self.contenedor_input_izquierda.place(relx=0.3, rely=0.12, anchor="n")
        self.contenedor_input_derecha.place(relx=0.7, rely=0.12, anchor="n")
    
    
    def area_input_izquierda(self):
        validacion_numeros = self.master.register(self.solo_numeros)
        validacion_letras = self.master.register(self.solo_letras)
        
        self.input_nombres_representante = ctk.CTkEntry(master=self.contenedor_input_izquierda,
                                    width=250,
                                    height=40,
                                    corner_radius=100,
                                    font=var.Andika_small,
                                    validate="key",
                                    validatecommand=(validacion_letras, '%S')
                                    )
        self.input_nombres_representante.place(relx=0.5, rely=0.18, anchor="center")
        
        self.input_apellidos_representante = ctk.CTkEntry(master=self.contenedor_input_izquierda,
                                    width=250,
                                    height=40,
                                    corner_radius=100,
                                    font=var.Andika_small,
                                    validate="key",
                                    validatecommand=(validacion_letras, '%S')
                                    )
        self.input_apellidos_representante.place(relx=0.5, rely=0.48, anchor="center")

        self.input_cedula_representante = ctk.CTkEntry(master=self.contenedor_input_izquierda,
                                    width=250,
                                    height=40,
                                    corner_radius=100,
                                    font=var.Andika_small,
                                    validate="key",
                                    validatecommand=(validacion_numeros, '%S')
                                    )
        self.input_cedula_representante.place(relx=0.5, rely=0.78, anchor="center")
        
        #------texto------
        self.texto_nombres = self.crear_texto(posicion_x=0.18,
                                              posicion_y=0.1,
                                              texto="Nombres:",
                                              contenedor=self.contenedor_input_izquierda
                                             )

        self.texto_apellidos = self.crear_texto(posicion_x=0.18,
                                              posicion_y=0.4,
                                              texto="Apellidos:",
                                              contenedor=self.contenedor_input_izquierda
                                             )
        
        self.texto_cedula = self.crear_texto(posicion_x=0.18,
                                              posicion_y=0.7,
                                              texto="Cedula:",
                                              contenedor=self.contenedor_input_izquierda
                                             )
    
    
    def area_input_derecha(self):
        validacion_numeros = self.master.register(self.solo_numeros)
        
        self.input_correo_representante = ctk.CTkEntry(master=self.contenedor_input_derecha,
                                    width=250,
                                    height=40,
                                    corner_radius=100,
                                    font=var.Andika_small
                                    )
        self.input_correo_representante.place(relx=0.5, rely=0.18, anchor="center")
        
        self.input_telefono_representante = ctk.CTkEntry(master=self.contenedor_input_derecha,
                                    width=250,
                                    height=40,
                                    corner_radius=100,
                                    font=var.Andika_small,
                                    validate="key",
                                    validatecommand=(validacion_numeros, '%S')
                                    )
        self.input_telefono_representante.place(relx=0.5, rely=0.48, anchor="center")

        self.input_direcion_representante = ctk.CTkEntry(master=self.contenedor_input_derecha,
                                    width=250,
                                    height=40,
                                    corner_radius=100,
                                    font=var.Andika_small,
                                    )
        self.input_direcion_representante.place(relx=0.5, rely=0.78, anchor="center")
        
        #------texto------
        self.texto_correo= self.crear_texto(posicion_x=0.18,
                                              posicion_y=0.1,
                                              texto="Correo Electrónico:",
                                              contenedor=self.contenedor_input_derecha
                                             )

        self.texto_telefono  = self.crear_texto(posicion_x=0.18,
                                              posicion_y=0.4,
                                              texto="Numero de teléfono:",
                                              contenedor=self.contenedor_input_derecha
                                             )
        
        self.texto_direccion = self.crear_texto(posicion_x=0.18,
                                              posicion_y=0.7,
                                              texto="Dirección de Habitación:",
                                              contenedor=self.contenedor_input_derecha
                                             )
    
    
    def verificar_espacios(self):
        nombres = self.input_nombres_representante.get()
        apellidos = self.input_apellidos_representante.get()
        cedula = self.input_cedula_representante.get()
        correo = self.input_correo_representante.get()
        telefono = self.input_telefono_representante.get()
        direccion = self.input_direcion_representante.get()

        # Verificar si hay espacios vacíos
        if not nombres.strip() or not apellidos.strip() or not cedula.strip() or not correo.strip() or not telefono.strip() or not direccion.strip():
            print("Hay campos vacíos. Por favor, ingrese todos los datos.")

        # Verificar si todos los campos comienzan con una letra y cedula con numero
        elif nombres[0].isalpha() and apellidos[0].isalpha() and cedula[0].isdigit() and telefono[0].isdigit():
            self.continuar()  # Ejecutar self.continuar() si todo está correcto

        else:
            print("Los campos deben comenzar con una letra/numero")
    
    
    def continuar(self):
        #-------------------------aqui
        self.cedula = self.input_cedula_representante.get()
        if self.cedula == "1234":
            texto_emergente = "Representante Ya Registrado"
            CTkMessagebox(title="Información", message=texto_emergente)
            ventana_grados_registar = GradoRegistrarVentana(self.master)
            ventana_grados_registar.mostrar()
        else:
            self.continuar_registro()
    
    
    def continuar_registro(self):
        nombres = self.input_nombres_representante.get()
        nombre_1, nombre_2 = nombres.split()
        apellidos = self.input_apellidos_representante.get()
        apellido_1, apellido_2 = apellidos.split()
        correo = self.input_correo_representante.get()
        telefono = self.input_telefono_representante.get()
        direccion = self.input_direcion_representante.get()
        
        # INSERTAR DATOS DEL REPRESENTANTE
        conn = sqlite3.connect('./bd_rufino/bd_escuela.db')
        c = conn.cursor()

        # Insertar valores en la tabla
        c.execute("INSERT INTO Representante (primer_nombre, segundo_nombre, primer_apellido, segundo_apellido, cedula, correo, telefono, direccion) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (nombre_1, nombre_2, apellido_1, apellido_2, self.cedula, correo, telefono, direccion))

        representante_id = c.lastrowid
          
        # Confirmar los cambios y cerrar la conexión
        conn.commit()
        conn.close()
          
        # OBTENER ID DEL ULTIMO ESTUDIANTE
        conn = sqlite3.connect('./bd_rufino/bd_escuela.db')
        c = conn.cursor()
          
        c.execute("SELECT id_estudiante FROM Estudiante ORDER BY id_estudiante DESC LIMIT 1")
        ultimo_elemento = c.fetchone()
          
        # Confirmar los cambios y cerrar la conexión
        conn.commit()
        conn.close()
          
        # ACTUALIZAR EL ID DEL REPRESENTANTE EN LA TABLA DEL ESTUDIANTE
        conn = sqlite3.connect('./bd_rufino/bd_escuela.db')
        c = conn.cursor()
          
        c.execute("UPDATE Estudiante SET id_representante = ? WHERE id_estudiante = ?", (representante_id, ultimo_elemento[0]))
          
        # Confirmar los cambios y cerrar la conexión
        conn.commit()
        conn.close()
        ventana_grados_registar = GradoRegistrarVentana(self.master)
        ventana_grados_registar.mostrar()
    
    
    def solo_numeros(self, char):
        return char.isdigit() # solo numeros
    
    
    def solo_letras(self, char):
        return char.isalpha() or char.isspace()  # Permitir letras y espacios en blanco
    
    
    #Metodo para crear texto
    def crear_texto(self, posicion_x, posicion_y, texto, contenedor):
        palabras = ctk.CTkLabel(master=contenedor,
                                            text=texto,
                                            text_color=var.text_white,
                                            font=var.Amaranth_small
                                            )
        palabras.place(relx=posicion_x, rely=posicion_y, anchor="w")
    
    
    def lista_str(self, lista):
        opciones_str = [str(opcion) for opcion in lista]
        return opciones_str
    
    
    #Metodo para crear botones
    def crear_botones_estudiantes(self, texto, comando, color_boton, posicion_x, posicion_y):
        boton = ctk.CTkButton(master=self.master,
                             text=texto,
                             width=330,
                             height=40,
                             font=var.Amaranth_small,
                             fg_color=color_boton,
                             hover_color=var.btn_gold,
                             corner_radius=30,
                             command=comando
                             )
        
        boton.place(relx=posicion_x, rely=posicion_y, anchor="center")