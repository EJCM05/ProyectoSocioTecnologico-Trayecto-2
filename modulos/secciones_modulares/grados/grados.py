import customtkinter as ctk
from modulos.variables import variables as var


class GradosVentana:
    def __init__(self, master):
        self.master = master

    def mostrar(self):
        # Eliminar widgets anteriores en el área de contenido
        for widget in self.master.winfo_children():
            widget.destroy()
        
        self.texto_titulo()
        self.botones_seleccion_grado()
    
    
    def texto_titulo(self):
        self.texto_seleccion = ctk.CTkLabel(master=self.master,
                                           text="Selecciona un Grado",
                                           text_color=var.text_black,
                                           font=var.Amaranth_medium
                                           )
        
        self.texto_seleccion.place(relx=0.5, rely=0.1, anchor="center")
    
    
    def botones_seleccion_grado(self):
        self.boton_simoncito = self.crear_botones_grado(texto="Simoncito",
                                                        comando="",
                                                        color_boton=var.buttons_color,
                                                        posicion_x=0.15,
                                                        posicion_y=0.45
                                                       )
        
        self.boton_inicial_a = self.crear_botones_grado(texto="Inicial A",
                                                        comando="",
                                                        color_boton=var.buttons_color,
                                                        posicion_x=0.35,
                                                        posicion_y=0.45
                                                       )
        
        self.boton_inicial_b = self.crear_botones_grado(texto="Inicial B",
                                                        comando="",
                                                        color_boton=var.buttons_color,
                                                        posicion_x=0.15,
                                                        posicion_y=0.65
                                                       )
        
        self.boton_inicial_c = self.crear_botones_grado(texto="Inicial C",
                                                        comando="",
                                                        color_boton=var.buttons_color,
                                                        posicion_x=0.35,
                                                        posicion_y=0.65
                                                       )
        
        self.boton_1er_grado = self.crear_botones_grado(texto="1er Grado",
                                                        comando="",
                                                        color_boton=var.buttons_color,
                                                        posicion_x=0.65,
                                                        posicion_y=0.35
                                                       )
        
        self.boton_2do_grado = self.crear_botones_grado(texto="2do Grado",
                                                        comando="",
                                                        color_boton=var.buttons_color,
                                                        posicion_x=0.65,
                                                        posicion_y=0.55
                                                       )
        
        self.boton_3er_grado = self.crear_botones_grado(texto="3er Grado",
                                                        comando="",
                                                        color_boton=var.buttons_color,
                                                        posicion_x=0.65,
                                                        posicion_y=0.75
                                                       )
        
        self.boton_4to_grado = self.crear_botones_grado(texto="4to Grado",
                                                        comando="",
                                                        color_boton=var.buttons_color,
                                                        posicion_x=0.85,
                                                        posicion_y=0.35
                                                       )
        
        self.boton_5to_grado = self.crear_botones_grado(texto="5to Grado",
                                                        comando="",
                                                        color_boton=var.buttons_color,
                                                        posicion_x=0.85,
                                                        posicion_y=0.55
                                                       )
        
        self.boton_6to_grado = self.crear_botones_grado(texto="6to Grado",
                                                        comando="",
                                                        color_boton=var.buttons_color,
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