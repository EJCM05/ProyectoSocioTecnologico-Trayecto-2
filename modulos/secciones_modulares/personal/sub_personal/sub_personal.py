import customtkinter as ctk
from modulos.variables import variables as var
from modulos.secciones_modulares.personal.sub_personal.crear_personal import CrearPersonalVentana
from modulos.secciones_modulares.personal.sub_personal.ver_lista_personal import VerListaPersonalVentana

class SubPersonalVentana:
    def __init__(self, master, nombre_personal):
        self.master = master
        self.nombre_personal = nombre_personal
        self.decidir_personal()
    
    
    def mostrar(self):
        # Eliminar widgets anteriores en el área de contenido
        for widget in self.master.winfo_children():
            widget.destroy()
        
        self.texto_titulo()
        self.botones_personal()
    
    
    def decidir_personal(self):
        if self.nombre_personal == "Obrero":
            self.tipo_personal = 1
        elif self.nombre_personal == "Docente":
            self.tipo_personal = 2
        elif self.nombre_personal == "Especialista":
            self.tipo_personal = 3
    
    
    def cargar_ventana_crar_personal(self, nombre_personal):
        self.contenido_crear_personal = CrearPersonalVentana(master=self.master,
                                                     nombre_personal = nombre_personal,
                                                     tipo_personal=self.tipo_personal
                                                    )
        self.contenido_crear_personal.mostrar()
    
    
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
    
    
    def botones_personal(self):
        self.boton_crear_personal = self.crear_botones_personal(texto="Registrar Personal",
                                                        comando=lambda: self.cargar_ventana_crar_personal(nombre_personal=self.nombre_personal),
                                                        color_boton=var.button_blue,
                                                        posicion_x=0.15,
                                                        posicion_y=0.15
                                                       )
        self.boton_ver_lista_personal = self.crear_botones_personal(texto="Ver lista Personal",
                                                        comando=lambda: self.cargar_ventana_ver_lista_personal(nombre_personal=self.nombre_personal),
                                                        color_boton=var.button_blue,
                                                        posicion_x=0.5,
                                                        posicion_y=0.8
                                                       )
    
    
    def crear_botones_personal(self, texto, comando, color_boton, posicion_x, posicion_y):
        boton = ctk.CTkButton(master=self.master,
                             text=texto,
                             width=130,
                             height=40,
                             font=var.Amaranth_small,
                             fg_color=color_boton,
                             hover_color=var.hover_buttons_color,
                             corner_radius=10,
                             command=comando
                             )
        
        boton.place(relx=posicion_x, rely=posicion_y, anchor="center")