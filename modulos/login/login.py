import sqlite3
import tkinter as tk
import customtkinter as ctk
from modulos.variables import variables as var
from modulos.controlador import controlador
from PIL import ImageTk, Image
from modulos.dashboard.dashboard import Dashboard
from modulos.dashboard.dashboard_docente import DashboardDocente
from CTkMessagebox import CTkMessagebox


class LoginApp:
    def __init__(self,master):
        self.master = master
        self.controlador = controlador
    
    def mostrar(self):
        # Eliminar widgets anteriores en el área de contenido
        for widget in self.master.winfo_children():
            widget.destroy()
        
        # imagenes e iconos
        self.importar_img_ico()
        
        # cuadro principal
        self.principal()
        self.izquierda()
        self.derecha()


    
    # importando imagenes e iconos
    def importar_img_ico(self):
        # importardo imagen
        self.icono_user_original = Image.open("imagenes/login-usuario-blanco.png")
        self.logo_inicio_original = Image.open("imagenes/login-logo-inicio.png")
        self.icono_password_original = Image.open("imagenes/login-candado-blanco.png")
        
        # ajustando al tamaño deseado. imagen.resize((nuevo_ancho, nuevo_alto), suavizar y mejorar la calidad)
        self.icono_user_ajustada = self.icono_user_original.resize((35, 35), Image.LANCZOS)
        self.logo_inicio_ajustada = self.logo_inicio_original.resize((300, 300), Image.LANCZOS)
        self.icono_password_ajustada = self.icono_password_original.resize((35, 35), Image.LANCZOS)
        
        # asignando a la variable que va a ser usada
        self.img_icono_user = ImageTk.PhotoImage(self.icono_user_ajustada)
        self.img_logo_inicio = ImageTk.PhotoImage(self.logo_inicio_ajustada)
        self.img_icono_password = ImageTk.PhotoImage(self.icono_password_ajustada)
    
    
    def principal(self):
        # contenedor principal (blanco)
        self.contenedor_blanco = ctk.CTkFrame(master=self.master,
                                            width=550,
                                            height=550,
                                            corner_radius=0,
                                            fg_color=var.bg_white,
                                            border_color=var.border_black,
                                            border_width=.5
                                            )
        
        # contenedor principal (azul)
        self.contenedor_azul = ctk.CTkFrame(master=self.master,
                                            width=550,
                                            height=550,
                                            corner_radius=0,
                                            fg_color=var.bg_blue,
                                            border_color=var.border_black,
                                            border_width=0.5
                                            )
        
        # - Posicionamiento -
        self.contenedor_blanco.place(relx=0.5, rely=0.5, anchor="e")
        self.contenedor_azul.place(relx=0.5, rely=0.5, anchor="w")
    
    
    def izquierda(self):
        #texto nombre de la escuela
        self.texto_nombre_escuela_1era_linea = ctk.CTkLabel(master=self.contenedor_blanco,
                                                text="Escuela Nacional",
                                                text_color=var.text_black,
                                                font=var.Amaranth_large
                                                )
        
        self.texto_nombre_escuela_2da_linea = ctk.CTkLabel(master=self.contenedor_blanco,
                                                text="Rufino Duque Contreras",
                                                text_color=var.text_black,
                                                font=var.Amaranth_medium
                                                )
        
        # logo de inicio
        self.logo = ctk.CTkLabel(master=self.contenedor_blanco,
                                image=self.img_logo_inicio,
                                text="",
                                )
        
        # - Posicionamiento -
        self.texto_nombre_escuela_1era_linea.place(relx=0.5, rely=0.2, anchor="center")
        self.texto_nombre_escuela_2da_linea.place(relx=0.5, rely=0.3, anchor="center")
        self.logo.place(relx=0.5, rely=0.65, anchor="center")
    
    
    def derecha(self):
        #texto bienvenido
        self.texto_bienvenido = ctk.CTkLabel(master=self.contenedor_azul,
                                            text="Bienvenido!",
                                            text_color=var.text_white,
                                            font=var.Amaranth_large
                                            )
        
        # texto inicia sesion
        self.texto_inicio_continuar = ctk.CTkLabel(master=self.contenedor_azul,
                                            text="Inicia sesión para continuar",
                                            text_color=var.text_white,
                                            font=var.Andika_medium
                                            )
        
        # texto usuario
        self.texto_usuario = ctk.CTkLabel(master=self.contenedor_azul,
                                            text="Usuario:",
                                            text_color=var.text_white,
                                            font=var.Amaranth_small
                                            )
        
        # icono de usuario
        self.icono_usuario = ctk.CTkLabel(master=self.contenedor_azul,
                                    image=self.img_icono_user,
                                    text="",
                                    )
        
        # input donde se introduce el usuario
        self.input_usuario = ctk.CTkEntry(master=self.contenedor_azul,
                                    width=300,
                                    height=40,
                                    corner_radius=100,
                                    font=var.Andika_small,
                                    placeholder_text="Ingrese un usuario"
                                    )
        
        #texto contraseña
        self.texto_contraseña = ctk.CTkLabel(master=self.contenedor_azul,
                                            text="Contraseña:",
                                            text_color=var.text_white,
                                            font=var.Amaranth_small
                                            )
        
        # icono de contraseña
        self.icono_contraseña = ctk.CTkLabel(master=self.contenedor_azul,
                                    image=self.img_icono_password,
                                    text="",
                                    )
        
        # input donde se introduce la contraseña
        self.input_contraseña = ctk.CTkEntry(master=self.contenedor_azul,
                                    width=300,
                                    height=40,
                                    corner_radius=100,
                                    show="*",
                                    font=var.Andika_small,
                                    placeholder_text="Ingrese una contraseña"
                                    )
        
        # boton de login
        self.boton_login = ctk.CTkButton(master=self.contenedor_azul,
                                        width=300,
                                        height=40,
                                        text="Continuar",
                                        corner_radius=100,
                                        fg_color=var.buttons_color,
                                        text_color=var.text_black,
                                        font=var.Amaranth_small,
                                        command=self.validacion
                                        )
        
        # - Posicionamiento -
        self.texto_bienvenido.place(relx=0.22, rely=0.20, anchor="w")
        self.texto_inicio_continuar.place(relx=0.23, rely=0.30, anchor="w")
        self.texto_usuario.place(relx=0.25, rely=0.40, anchor="w")
        self.icono_usuario.place(relx=0.18, rely=0.47, anchor="center")
        self.input_usuario.place(relx=0.5, rely=0.47, anchor="center")
        self.texto_contraseña.place(relx=0.25, rely=0.57, anchor="w")
        self.icono_contraseña.place(relx=0.18, rely=0.64, anchor="center")
        self.input_contraseña.place(relx=0.5, rely=0.64, anchor="center")
        self.boton_login.place(relx=0.5, rely=0.77, anchor="center")
    
    def validacion(self):
        username = self.input_usuario.get()
        password = self.input_contraseña.get()

        conn = sqlite3.connect('./bd_rufino/bd_escuela.db')
        cursor = conn.cursor()

        # Consulta SQL para verificar las credenciales
        cursor.execute('SELECT * FROM Ingreso WHERE usuario=? AND contrasena=?', (username, password))
        result = cursor.fetchone()
        
        conn.close()

        if result:
            # Credenciales válidas: carga la ventana principal
            tipo_usuario = self.pasar_cargo(self.input_usuario.get())
            if tipo_usuario[1] == "Director" or tipo_usuario[1] == "Admin":
                self.cargar_ventana_dashboard_director()
            else:
                self.cargar_ventana_dashboard_docente()
            
        else:
            # Credenciales incorrectas: muestra un mensaje de error
            texto_emergente = "Usuario o Contraseña incorrectos"
            CTkMessagebox(title="Alerta", message=texto_emergente,font=("calibri",16),icon="cancel")
            
    def pasar_cargo(self, usuario):
        usuario = usuario
        if usuario == "admin":
          result = ["Administrador", "Admin", usuario]
        elif usuario == "simoncito":
          result = ["Docente", "Simoncito", usuario]
        elif usuario == "inicial_a":
          result = ["Docente", "Inicial A", usuario]
        elif usuario == "inicial_b":
          result = ["Docente", "Inicial B", usuario]
        elif usuario == "inicial_c":
          result = ["Docente", "Inicial C", usuario]
        elif usuario == "grado_1":
          result = ["Docente", "1er Grado", usuario]
        elif usuario == "grado_2":
          result = ["Docente", "2do Grado", usuario]
        elif usuario == "grado_3":
          result = ["Docente", "3er Grado", usuario]
        elif usuario == "grado_4":
          result = ["Docente", "4to Grado", usuario]
        elif usuario == "grado_5":
          result = ["Docente", "5to Grado", usuario]
        elif usuario == "grado_6":
          result = ["Docente", "6to Grado", usuario]
        elif usuario == "director":
          result = ["Director", "Director", usuario]
        return result

    def cargar_ventana_dashboard_director(self):
        self.contenido_dashboard = Dashboard(self.master, self.pasar_cargo(self.input_usuario.get()))
        self.contenido_dashboard.mostrar()
    
    
    def cargar_ventana_dashboard_docente(self):
        self.contenido_dashboard = DashboardDocente(self.master, self.pasar_cargo(self.input_usuario.get()))
        self.contenido_dashboard.mostrar()