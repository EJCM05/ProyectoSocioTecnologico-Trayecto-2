import tkinter as tk
import customtkinter as ctk
import variables as var
from PIL import ImageTk, Image

class Dashboard:
    def __init__(self):
        # definicion de apariencia
        self.configurar_apariencia()
        
        # creacion de ventana
        self.crear_ventana_principal()
        
        # imagenes e iconos
        self.importar_img_ico()
        
        # cuadro principal
        self.panel_izquierdo()
        self.elementos_panel_izquierdo()
        self.panel_superior()
        self.secciones()
    
    
    # configurar apariencia
    def configurar_apariencia(self):
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("dark-blue")
    
    
    # metodo para crear la ventana principal
    def crear_ventana_principal(self):
        self.app = ctk.CTk()
        self.app.geometry("1280x720")
        self.app.title("Login")
        self.app.resizable(0,0)
    
    
    # importando imagenes e iconos
    def importar_img_ico(self):
        # importardo imagen
        self.icono_menu_png = Image.open("imagenes/icono_menu.png")       
        # ajustando al tamaño deseado. imagen.resize((nuevo_ancho, nuevo_alto), suavizar y mejorar la calidad)
        self.icono_menu_ajustada = self.icono_menu_png.resize((80, 80), Image.LANCZOS)
        # asignando a la variable que va a ser usada
        self.img_menu = ImageTk.PhotoImage(self.icono_menu_ajustada)
        
    
    
    def panel_izquierdo(self):
        self.panel_izquierdo = ctk.CTkFrame(master=self.app,
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
                                    text_color=var.text_white)
        
        # botones del menu
        self.boton_inicio = ctk.CTkButton(master=self.panel_izquierdo,
                                        text="Inicio",
                                        width=185,
                                        font=var.Andika_small,
                                        hover_color=var.bg_blue,
                                        fg_color=var.bg_gray,
                                        anchor="sw"
                                        )
        self.boton_grados = ctk.CTkButton(master=self.panel_izquierdo,
                                        text="Grados",
                                        width=185,
                                        font=var.Andika_small,
                                        hover_color=var.bg_blue,
                                        fg_color=var.bg_gray,
                                        anchor="sw"
                                        )
        self.boton_personal = ctk.CTkButton(master=self.panel_izquierdo,
                                        text="Personal",
                                        width=185,
                                        font=var.Andika_small,
                                        hover_color=var.bg_blue,
                                        fg_color=var.bg_gray,
                                        anchor="sw"
                                        )
        self.boton_estudiantes = ctk.CTkButton(master=self.panel_izquierdo,
                                        text="Estudiantes",
                                        width=185,
                                        font=var.Andika_small,
                                        hover_color=var.bg_blue,
                                        fg_color=var.bg_gray,
                                        anchor="sw"
                                        )
        self.boton_perfil = ctk.CTkButton(master=self.panel_izquierdo,
                                        text="Perfil",
                                        width=185,
                                        font=var.Andika_small,
                                        hover_color=var.bg_blue,
                                        fg_color=var.bg_gray,
                                        anchor="sw"
                                        )
        self.boton_salir = ctk.CTkButton(master=self.panel_izquierdo,
                                        text="Salir",
                                        width=80,
                                        font=var.Amaranth_small,
                                        fg_color=var.buttons_color,
                                        hover_color=var.hover_buttons_color,
                                        corner_radius=30
                                        )
        
        #           posicionamiento
        self.icono_menu.place(relx=0.25, rely=0.01, anchor="n")
        self.texto_menu.place(relx=0.7,rely=0.030,anchor="n",)
        self.boton_inicio.place(relx=0.5,rely=0.3,anchor="center")
        self.boton_grados.place(relx=0.5,rely=0.35,anchor="center")
        self.boton_personal.place(relx=0.5,rely=0.4,anchor="center")
        self.boton_estudiantes.place(relx=0.5,rely=0.45,anchor="center")
        self.boton_perfil.place(relx=0.5,rely=0.5,anchor="center")
        self.boton_salir.place(relx=0.5,rely=0.9,anchor="s")
        
        
        
    
    
    
    def panel_superior(self):
        self.panel_superior = ctk.CTkFrame(master=self.app,
                                    width=1084,
                                    height=80,
                                    fg_color=var.bg_blue,
                                    corner_radius=0)
        #------------------posicionamiento----------------------------------#
        self.panel_superior.grid(row=0,column=1,sticky="N")
        
    def secciones(self):
        pass
    
    #iniciar la ventana
    def run(self):
        self.app.mainloop()


# Crear y ejecutar aplicación
app = Dashboard()
app.run()
