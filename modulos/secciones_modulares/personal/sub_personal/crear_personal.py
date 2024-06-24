import customtkinter as ctk
from modulos.variables import variables as var
import sqlite3
from CTkMessagebox import CTkMessagebox
from modulos.secciones_modulares.inicio.inicio import InicioVentana

class CrearPersonalVentana:
    def __init__(self, master, nombre_personal, tipo_personal):
        self.master = master
        self.nombre_personal = nombre_personal
        self.tipo_personal = tipo_personal
    
    
    def mostrar(self):
        # Eliminar widgets anteriores en el área de contenido
        for widget in self.master.winfo_children():
            widget.destroy()
        
        self.texto_titulo()
        self.area_input()
    
    
    def texto_titulo(self):
        self.texto_seleccion = ctk.CTkLabel(master=self.master,
                                           text=f"Registrar Personal {self.nombre_personal}",
                                           text_color=var.text_black,
                                           font=var.Andika_large
                                           )
        
        self.texto_seleccion.place(relx=0.5, rely=0.06, anchor="center")
    
    
    def area_input(self):
        #contenedor principal de los inputs
        self.contenedor_input = ctk.CTkFrame(master=self.master,
                                 width=450,
                                 height=550,
                                 corner_radius=40,
                                 fg_color=var.btn_gray
                                 )
        self.contenedor_input.place(relx=0.5, rely=0.1, anchor="n")
        
        
        validacion_numeros = self.master.register(self.solo_numeros)
        validacion_letras = self.master.register(self.solo_letras)
        
        self.input_nombres_personal = ctk.CTkEntry(master=self.contenedor_input,
                                    width=330,
                                    height=40,
                                    corner_radius=100,
                                    font=var.Andika_small,
                                    validate="key",
                                    validatecommand=(validacion_letras, '%S')
                                    )
        self.input_nombres_personal.place(relx=0.5, rely=0.14, anchor="center")
        
        self.input_apellidos_personal = ctk.CTkEntry(master=self.contenedor_input,
                                    width=330,
                                    height=40,
                                    corner_radius=100,
                                    font=var.Andika_small,
                                    validate="key",
                                    validatecommand=(validacion_letras, '%S')
                                    )
        self.input_apellidos_personal.place(relx=0.5, rely=0.30, anchor="center")

        self.input_cedula_personal = ctk.CTkEntry(master=self.contenedor_input,
                                    width=330,
                                    height=40,
                                    corner_radius=100,
                                    font=var.Andika_small,
                                    validate="key",
                                    validatecommand=(validacion_numeros, '%S')
                                    )
        self.input_cedula_personal.place(relx=0.5, rely=0.46, anchor="center")
        
        #LISTA para opciones del input desplegable
        # Se llama al metodo lista_str para pasar los valores numeros a str
        lista_dias = list(range(1, 32))
        lista_dias = self.lista_str(lista_dias)
        lista_meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
        lista_años = list(range(2000, 2025))
        lista_años = self.lista_str(lista_años)
        lista_genero = ["Masculino", "Femenino"]
        
        self.input_dia_nacimiento_personal = ctk.CTkComboBox(self.contenedor_input,
                                state="readonly",
                                values=lista_dias,
                                width=80,
                                height=40
                               )
        self.input_dia_nacimiento_personal.set(lista_dias[0])
        self.input_dia_nacimiento_personal.place(relx=0.26, rely=0.62, anchor="center")
        
        self.input_mes_nacimiento_personal = ctk.CTkComboBox(self.contenedor_input,
                                state="readonly",
                                values=lista_meses,
                                width=125,
                                height=40
                               )
        self.input_mes_nacimiento_personal.set(lista_meses[0])
        self.input_mes_nacimiento_personal.place(relx=0.5, rely=0.62, anchor="center")
        
        self.input_año_nacimiento_personal = ctk.CTkComboBox(self.contenedor_input,
                                state="readonly",
                                values=lista_años,
                                width=80,
                                height=40
                               )
        self.input_año_nacimiento_personal.set(lista_años[-1])
        self.input_año_nacimiento_personal.place(relx=0.74, rely=0.62, anchor="center")
        
        self.input_genero_personal = ctk.CTkComboBox(self.contenedor_input,
                                state="readonly",
                                values=lista_genero,
                                width=280,
                                height=40
                               )
        self.input_genero_personal.set(lista_genero[0])
        self.input_genero_personal.place(relx=0.5, rely=0.78, anchor="center")
        
        
        #------boton continuar------
        self.boton_continuar = self.crear_botones_personal(texto="Continuar",
                                                        comando=self.verificar_espacios,
                                                        color_boton=var.buttons_color,
                                                        posicion_x=0.5,
                                                        posicion_y=0.87
                                                       )
        
        #------texto------
        self.texto_nombres = self.crear_texto(posicion_x=0.18,
                                              posicion_y=0.07,
                                              texto="Nombres:"
                                             )

        self.texto_apellidos = self.crear_texto(posicion_x=0.18,
                                              posicion_y=0.23,
                                              texto="Apellidos:"
                                             )
        
        self.texto_cedula = self.crear_texto(posicion_x=0.18,
                                              posicion_y=0.39,
                                              texto="Cedula:"
                                             )
        
        self.texto_fecha = self.crear_texto(posicion_x=0.18,
                                              posicion_y=0.55,
                                              texto="Fecha de Nacimeinto:"
                                             )
        
        self.texto_genero = self.crear_texto(posicion_x=0.18,
                                              posicion_y=0.71,
                                              texto="Genero:"
                                             )
    
    
    def continuar(self):
      # Conectarse a la base de datos
      conn = sqlite3.connect('./bd_rufino/bd_escuela.db')
      c = conn.cursor()

      # Insertar valores en la tabla
      c.execute(f"SELECT cedula FROM Personal")
      info = c.fetchall()
      
      lista = []
      for tupla in info:
        lista.append(str(tupla[0]))
      
      # Confirmar los cambios y cerrar la conexión
      conn.commit()
      conn.close()
      
      self.cedula = self.input_cedula_personal.get()
      if self.cedula in lista:
          texto_emergente = "Personal Ya Registrado"
          CTkMessagebox(title="Información", message=texto_emergente)
      else:
          self.continuar_registro()
    
    
    def continuar_registro(self):
      nombres = self.input_nombres_personal.get()
      nombre_1, *nombres_2 = nombres.split()
      # print(nombres_2)

      # Unir todos los elementos de la lista en un solo string, sin separador
      nombre_2 = " ".join(nombres_2)

      # Mostrar el resultado
      # print(nombre_2)
      
      apellidos = self.input_apellidos_personal.get()
      apellido_1, *apellidos_2 = apellidos.split()
      
      apellido_2 = " ".join(apellidos_2)
        
      if len(apellidos_2) >= 3 or len(nombres_2) >= 3:
        print("Cantidad excesiva de nombres, ni que fueras simon bolivar")
      
      dia_nacimiento = self.input_dia_nacimiento_personal.get()
      mes_nacimiento = self.input_mes_nacimiento_personal.get()
      
      if mes_nacimiento == "Enero":
        opcion = 1
      elif mes_nacimiento == "Febrero":
        opcion = 2
      elif mes_nacimiento == "Marzo":
        opcion = 3
      elif mes_nacimiento == "Abril":
        opcion = 4
      elif mes_nacimiento == "Mayo":
        opcion = 5
      elif mes_nacimiento == "Junio":
        opcion = 6
      elif mes_nacimiento == "Julio":
        opcion = 7
      elif mes_nacimiento == "Agosto":
        opcion = 8
      elif mes_nacimiento == "Septiembre":
        opcion = 9
      elif mes_nacimiento == "Octubre":
        opcion = 10
      elif mes_nacimiento == "Noviembre":
        opcion = 11
      elif mes_nacimiento == "Diciembre":
        opcion = 12
      
      año_nacimiento = self.input_año_nacimiento_personal.get()
      
      fecha_nacimiento = f"{año_nacimiento}/{opcion}/{dia_nacimiento}"
      
      genero = self.input_genero_personal.get()
      
      # Conectarse a la base de datos
      conn = sqlite3.connect('./bd_rufino/bd_escuela.db')
      c = conn.cursor()

      # Insertar valores en la tabla
      c.execute("INSERT INTO Personal (id_personal, primer_nombre, segundo_nombre, primer_apellido, segundo_apellido, fecha_nacimiento, cedula, genero) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (self.tipo_personal, nombre_1, nombre_2, apellido_1, apellido_2, fecha_nacimiento,  self.cedula, genero))

      # Confirmar los cambios y cerrar la conexión
      conn.commit()
      conn.close()
      
      ventana_inicio = InicioVentana(self.master)
      texto_emergente = "Personal Registrado Correctamente"
      CTkMessagebox(title="Información", message=texto_emergente)
      ventana_inicio.mostrar()
    
    
    #Metodo para crear texto
    def crear_texto(self, posicion_x, posicion_y, texto):
        palabras = ctk.CTkLabel(master=self.contenedor_input,
                                            text=texto,
                                            text_color=var.text_white,
                                            font=var.Amaranth_small
                                            )
        palabras.place(relx=posicion_x, rely=posicion_y, anchor="w")
    
    
    #Metodo para crear botones
    def crear_botones_personal(self, texto, comando, color_boton, posicion_x, posicion_y):
        boton = ctk.CTkButton(master=self.master,
                             text=texto,
                             width=330,
                             height=40,
                             font=var.Amaranth_small,
                             fg_color=color_boton,
                             hover_color=var.btn_gold,
                             corner_radius=30,
                             command=comando,
                             bg_color=var.btn_gray
                             )
        
        boton.place(relx=posicion_x, rely=posicion_y, anchor="center")
    
    
    def lista_str(self, lista):
        opciones_str = [str(opcion) for opcion in lista]
        return opciones_str
    
    
    def solo_numeros(self, char):
        return char.isdigit() # solo numeros
    
    
    def solo_letras(self, char):
        return char.isalpha() or char.isspace()  # Permitir letras y espacios en blanco
    
    
    def verificar_espacios(self):
        nombres = self.input_nombres_personal.get()
        apellidos = self.input_apellidos_personal.get()
        cedula = self.input_cedula_personal.get()

        # Verificar si hay espacios vacíos
        if not nombres.strip() or not apellidos.strip() or not cedula.strip():
            print("Hay campos vacíos. Por favor, ingrese todos los datos.")

        # Verificar si todos los campos comienzan con una letra y cedula con numero
        elif nombres[0].isalpha() and apellidos[0].isalpha() and cedula[0].isdigit():
            self.continuar()  # Ejecutar self.continuar() si todo está correcto

        else:
            print("Los campos deben comenzar con una letra/numero")