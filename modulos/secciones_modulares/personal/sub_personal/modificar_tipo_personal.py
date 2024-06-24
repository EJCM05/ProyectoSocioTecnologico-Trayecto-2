import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from modulos.variables import variables as var
from modulos.secciones_modulares.inicio.inicio import InicioVentana
import sqlite3

class ModificarTipoPersonalVentana():
    def __init__(self, master, cedula):
        self.master = master
        self.cedula = cedula
    
    
    def mostrar(self):
        # Eliminar widgets anteriores en el área de contenido
        for widget in self.master.winfo_children():
            widget.destroy()
        
        self.texto_titulo()
        self.area_input()
    
    
    def texto_titulo(self):
        self.texto_seleccion = ctk.CTkLabel(master=self.master,
                                           text="Tipo Personal a Registrar",
                                           text_color=var.text_black,
                                           font=var.Andika_large
                                           )
        
        self.texto_seleccion.place(relx=0.5, rely=0.06, anchor="center")
    
    
    def area_input(self):
        #LISTA para opciones del input desplegable
        lista_tipo_empleado = ["Obrero", "Docente", "Especialista"]
        
        # Conectarse a la base de datos
        conn = sqlite3.connect('./bd_rufino/bd_escuela.db')
        c = conn.cursor()

        # Insertar valores en la tabla
        c.execute(f"SELECT id_grado FROM Estudiante WHERE cedula = {self.cedula};")

        info = c.fetchall()

        for element in info:
          tipo = info[0][0]
        
        # Confirmar los cambios y cerrar la conexión
        conn.commit()
        conn.close()
        
        if tipo == 1:
            opcion = "Obrero"
        elif tipo == 2:
            opcion = "Docente"
        elif tipo == 3:
            opcion = "Especialista"
        
        tipo_viejo = opcion
        
        #contenedor principal de los inputs
        self.contenedor_input = ctk.CTkFrame(master=self.master,
                                 width=380,
                                 height=300,
                                 corner_radius=40,
                                 fg_color=var.btn_gray
                                 )
        self.contenedor_input.place(relx=0.5, rely=0.1, anchor="n")
        
        self.input_tipo_empleado = ctk.CTkComboBox(self.contenedor_input,
                                state="readonly",
                                values=lista_tipo_empleado,
                                width=280,
                                height=40
                               )
        self.input_tipo_empleado.set(tipo_viejo)
        self.input_tipo_empleado.place(relx=0.5, rely=0.35, anchor="center")
        
        #------boton continuar------
        self.boton_continuar = self.crear_botones_personal(texto="Continuar",
                                                        comando=lambda: self.continuar(),
                                                        color_boton=var.buttons_color,
                                                        posicion_x=0.5,
                                                        posicion_y=0.5
                                                       )
        
        #------texto------
        self.texto_grados = self.crear_texto(posicion_x=0.18,
                                              posicion_y=0.2,
                                              texto="Lista de Personal:"
                                             )
    
    
    def continuar(self):
        ventana = InicioVentana(self.master)
        tipo = self.input_tipo_empleado.get()
        
        if tipo == "Obrero":
          opcion = 1
        elif tipo == "Docente":
          opcion = 2
        elif tipo == "Especialista":
          opcion = 3
          
        # ACTUALIZAR EL ID DEL REPRESENTANTE EN LA TABLA DEL ESTUDIANTE
        conn = sqlite3.connect('./bd_rufino/bd_escuela.db')
        c = conn.cursor()
          
        c.execute("UPDATE Estudiante SET id_grado = ? WHERE cedula = ?", (opcion, self.cedula))
          
        # Confirmar los cambios y cerrar la conexión
        conn.commit()
        conn.close()

        texto_emergente = "Personal Modificado correctamente"
        CTkMessagebox(title="Información", message=texto_emergente)
        ventana.mostrar()
    
    
    #Metodo para crear texto
    def crear_texto(self, posicion_x, posicion_y, texto):
        palabras = ctk.CTkLabel(master=self.contenedor_input,
                                            text=texto,
                                            text_color=var.text_white,
                                            font=var.Amaranth_small
                                            )
        palabras.place(relx=posicion_x, rely=posicion_y, anchor="w")
    
    
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
                             command=comando,
                             bg_color=var.btn_gray
                             )
        
        boton.place(relx=posicion_x, rely=posicion_y, anchor="center")