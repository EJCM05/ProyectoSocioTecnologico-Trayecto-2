import customtkinter as ctk
from modulos.variables import variables as var
from PIL import ImageTk, Image
import sqlite3

class PerfilVentana:
    def __init__(self, master):
        self.master = master

    def mostrar(self):
        # Eliminar widgets anteriores en el área de contenido
        for widget in self.master.winfo_children():
            widget.destroy()

        self.texto_titulo()
        self.importar_img_ico()
        self.frame_color_gray()
        self.imagen_password()
        self.inputs_password()
        self.texto_passwords()
        self.boton_aceptar()
               
    def importar_img_ico(self):
        self.icono_user_original = Image.open("imagenes/imagen_lock_password.png")
        self.icono_user_ajustada = self.icono_user_original.resize((250, 250), Image.LANCZOS)
        self.img_icono_password = ImageTk.PhotoImage(self.icono_user_ajustada)
    
    def imagen_password(self):
        self.carga_imagen_estudiante = ctk.CTkLabel(master=self.master,
                                                    image=self.img_icono_password,
                                                    text="",
                                                    fg_color=var.bg_gray)
        self.carga_imagen_estudiante.place(relx=0.24,rely=0.55,anchor="w")
    
    def frame_color_gray(self):
        self.background_gray = ctk.CTkFrame(master=self.master,
                                            width=746,
                                            height=387,
                                            fg_color=var.bg_gray
                                            )
        self.background_gray.place(relx=0.5,rely=0.55,anchor="center")

    def texto_titulo(self):
        self.texto_seleccion = ctk.CTkLabel(master=self.master,
                                           text="Cambiar contraseña",
                                           text_color=var.text_black,
                                           font=var.Amaranth_medium_large
                                           )
        
        self.texto_seleccion.place(relx=0.5, rely=0.15, anchor="center")
        
    def texto_passwords(self):
        self.texto_contraseña = self.crear_texto(texto="Contraseña Actual:",
                                                        posicion_x=0.75,
                                                        posicion_y=0.20,
                                                        fuente=var.Andika_small
                                                       )
        self.texto_contraseña_2 = self.crear_texto(texto="Nueva Contraseña:",
                                                        posicion_x=0.75,
                                                        posicion_y=0.42,
                                                        fuente=var.Andika_small
                                                       )
        self.texto_contraseña_3 = self.crear_texto(texto="Repita Nueva Contraseña:",
                                                        posicion_x=0.83,
                                                        posicion_y=0.62,
                                                        fuente=var.Andika_small
                                                       )
     
    def inputs_password(self):
        self.input_actual_contraseña = ctk.CTkEntry(master=self.master,
                                            width=240,
                                            height=30,
                                            text_color=var.text_black,
                                            font=var.Andika_small,
                                            validate="key",
                                            bg_color=var.bg_gray,
                                            placeholder_text="Ingrese Contraseña"
                                            )
        self.input_actual_contraseña.place(relx=0.75, rely=0.43,anchor="e")
        
        self.input_nueva_contraseña = ctk.CTkEntry(master=self.master,
                                            width=240,
                                            height=30,
                                            text_color=var.text_black,
                                            font=var.Andika_small,
                                            validate="key",
                                            bg_color=var.bg_gray,
                                            placeholder_text="Repita Contraseña"
                                            
                                            )
        self.input_nueva_contraseña.place(relx=0.75, rely=0.56,anchor="e")

        self.input_repita_contraseña = ctk.CTkEntry(master=self.master,
                                            width=240,
                                            height=32,
                                            text_color=var.text_black,
                                            font=var.Andika_small,
                                            validate="key",
                                            bg_color=var.bg_gray,
                                            placeholder_text="Repita Contraseña"           
                                            )
        self.input_repita_contraseña.place(relx=0.75, rely=0.68,anchor="e")

    def boton_aceptar(self):
        self.boton_aceptar = ctk.CTkButton(master=self.background_gray,
                                        text="Aceptar",
                                        width=180,
                                        font=var.Amaranth_small,
                                        fg_color=var.buttons_color,
                                        hover_color=var.hover_buttons_color,
                                        corner_radius=30,
                                        command=self.cambiar_contraseña
                                        )
        self.boton_aceptar.place(relx=0.83,rely=0.85,anchor="e")
        
    # Metodos  de creacion generales
    #Metodo para crear texto
    def crear_texto(self, posicion_x, posicion_y, texto,fuente):
        palabras = ctk.CTkLabel(master=self.background_gray,
                                            text=texto,
                                            text_color=var.text_white,
                                            font=fuente,
                                            fg_color=var.bg_gray,
                                            compound="center",
                                            justify="center"
                                            )
        palabras.place(relx=posicion_x, rely=posicion_y,anchor="e")
    
    def cambiar_contraseña(self):
        actual = self.input_actual_contraseña.get()
        nueva = self.input_nueva_contraseña.get()
        confirmar_nueva = self.input_repita_contraseña.get()
        
        contrasena_verificada = self.consultar_contrasena()
        
        print(type(actual))
        print(type(nueva))
        print(type(confirmar_nueva))
        print(type(contrasena_verificada))
        
        if actual == contrasena_verificada and nueva == confirmar_nueva:
           cursor.execute(f'UPDATE Ingreso SET contrasena = {nueva} WHERE usuario = "director";')
          
        
        
    def consultar_contrasena(self):
        conn = sqlite3.connect('./bd_rufino/bd_escuela.db')
        cursor = conn.cursor()

        # Consulta SQL para verificar las credenciales
        # cursor.execute(f'SELECT contraseña FROM Ingreso WHERE usuario = {usuario}')
        cursor.execute(f'SELECT contrasena FROM Ingreso WHERE usuario = "director"')
        result = cursor.fetchone()
        
        conn.close()
        
        return result[0]
        