import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from modulos.variables import variables as var
from modulos.secciones_modulares.inicio.inicio import InicioVentana
import sqlite3

class GradoRegistrarVentana():
    def __init__(self, master):
        self.master = master
    
    
    def mostrar(self):
        # Eliminar widgets anteriores en el área de contenido
        for widget in self.master.winfo_children():
            widget.destroy()
        
        self.texto_titulo()
        self.area_input()
    
    
    def texto_titulo(self):
        self.texto_seleccion = ctk.CTkLabel(master=self.master,
                                           text="Grado a Registrar",
                                           text_color=var.text_black,
                                           font=var.Andika_large
                                           )
        
        self.texto_seleccion.place(relx=0.5, rely=0.06, anchor="center")
    
    
    def area_input(self):
        #contenedor principal de los inputs
        self.contenedor_input = ctk.CTkFrame(master=self.master,
                                 width=380,
                                 height=300,
                                 corner_radius=40,
                                 fg_color=var.btn_gray
                                 )
        self.contenedor_input.place(relx=0.5, rely=0.1, anchor="n")
        
        #LISTA para opciones del input desplegable
        lista_grados = ["Simoncito", "Inicial A", "Inicial B", "Inicial C", "1er Grado", "2do Grado", "3er Grado", "4to Grado", "5to Grado", "6to Grado"]
        
        self.input_grado_estudiante = ctk.CTkComboBox(self.contenedor_input,
                                state="readonly",
                                values=lista_grados,
                                width=280,
                                height=40
                               )
        self.input_grado_estudiante.set(lista_grados[0])
        self.input_grado_estudiante.place(relx=0.5, rely=0.35, anchor="center")
        
        #------boton continuar------
        self.boton_continuar = self.crear_botones_estudiantes(texto="Continuar",
                                                        comando=lambda: self.continuar(),
                                                        color_boton=var.buttons_color,
                                                        posicion_x=0.5,
                                                        posicion_y=0.5
                                                       )
        
        #------texto------
        self.texto_grados = self.crear_texto(posicion_x=0.18,
                                              posicion_y=0.2,
                                              texto="Lista de Grados:"
                                             )
    
    
    def continuar(self):
        ventana_estudiantes = InicioVentana(self.master)
        grado = self.input_grado_estudiante.get()
        
        if grado == "Simoncito":
          opcion = 1
        elif grado == "Inicial A":
          opcion = 2
        elif grado == "Inicial B":
          opcion = 3
        elif grado == "Inicial C":
          opcion = 4
        elif grado == "1er Grado":
          opcion = 5
        elif grado == "2do Grado":
          opcion = 6
        elif grado == "3er Grado":
          opcion = 7
        elif grado == "4to Grado":
          opcion = 8
        elif grado == "5to Grado":
          opcion = 9
        elif grado == "6to Grado":
          opcion = 10
          
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
          
        c.execute("UPDATE Estudiante SET id_grado = ? WHERE id_estudiante = ?", (opcion, ultimo_elemento[0]))
          
        # Confirmar los cambios y cerrar la conexión
        conn.commit()
        conn.close()

        texto_emergente = "Estudiante registrado correctamente"
        CTkMessagebox(title="Información", message=texto_emergente)
        ventana_estudiantes.mostrar()
    
    
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