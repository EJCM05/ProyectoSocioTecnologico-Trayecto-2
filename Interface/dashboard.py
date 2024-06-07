import tkinter as tk
import customtkinter as CustomTK
import variables as var
from PIL import ImageTk, Image

class Dashboard():
    def __init__(self):
        # Las nuevas funciones constructoras se ejecutan aqui
        self.ConfigurarcionDeApariencia()
        self.CreacionDeVentana()
        self.ImportacionDeImagenes()
        self.count_total()
        self.TextVars()
        self.agregar_widgets()   #esto siempre va de ultimo

    def ImportacionDeImagenes(self):
        # importacion de imagenes background e iconos
        self.img_bg = ImageTk.PhotoImage(Image.open("imagen/background_dashboard.png"))
        self.bg_cian = ImageTk.PhotoImage(Image.open("imagen/bg_cian.png"))
        self.bg_blue_light = ImageTk.PhotoImage(Image.open("imagen/bg_blue_light.png"))
        self.bg_pink = ImageTk.PhotoImage(Image.open("imagen/bg_pink.png"))
        self.bg_yellow = ImageTk.PhotoImage(Image.open("imagen/bg_yellow.png"))
        self.icono_user_dashboard = ImageTk.PhotoImage(file="imagen/ico_user_dashboard.png")

    def CrearFrames(self):
        # Frames de ventanas
        self.panel_central = CustomTK.CTkFrame(master=self.app,fg_color=var.bg_gray_light)
        self.panel_izquierdo = CustomTK.CTkFrame(master=self.panel_central, width=200, height=656, fg_color=var.bg_gray_light, corner_radius=20)
        self.panel_derecho = CustomTK.CTkFrame(master=self.panel_central,width=750,height=656, fg_color=var.bg_white, corner_radius=38)
        self.estadistica_frame = CustomTK.CTkFrame(master=self.panel_derecho,height=220,width=690 ,fg_color=var.bg_gray_light,corner_radius=30)
        self.estadistica_frame_2 = CustomTK.CTkFrame(master=self.panel_derecho,height=320,width=690 ,fg_color=var.bg_gray_light,corner_radius=30)
        self.frame_user = CustomTK.CTkFrame(master=self.panel_derecho,height=50,width=130 ,fg_color=var.bg_gray_light,corner_radius=30)
        # ---------------------------------------------------------------
        self.panel_central.pack()
        self.panel_izquierdo.grid(row=0,column=0,padx=0,pady=10)
        self.panel_derecho.grid(row=0,column=1,padx=20,pady=10,rowspan=4)
        # ----------------------------------------------------------------
        self.estadistica_frame.place(x=30, y=80)
        self.estadistica_frame_2.place(x=30, y=310)
        self.frame_user.place(x=585, y=15)
        # ---------------------------------------------------------------
        # Frames personalizados
        self.frame_estadistica_profesor = CustomTK.CTkFrame(master=self.estadistica_frame,width=155,height=128,fg_color=var.bg_gray_light, corner_radius=20)
        self.frame_estadistica_estudiantes = CustomTK.CTkFrame(master=self.estadistica_frame,width=155,height=128,fg_color=var.bg_gray_light, corner_radius=20)
        self.frame_estadistica_aulas = CustomTK.CTkFrame(master=self.estadistica_frame,width=150,height=128,fg_color=var.bg_gray_light, corner_radius=20)
        self.frame_estadistica_trabajadores = CustomTK.CTkFrame(master=self.estadistica_frame,width=170,height=128,fg_color=var.bg_gray_light, corner_radius=20)
    #    -----------------------------------------------------
        self.frame_estadistica_profesor.place(x=20,y=80)
        self.frame_estadistica_estudiantes.place(x=185,y=80)
        self.frame_estadistica_aulas.place(x=350,y=80)
        self.frame_estadistica_trabajadores.place(x=510,y=80)
        # ------------------------------------------------------



    def CrearLabel(self):
        # Imagenes
        self.bg_izq = CustomTK.CTkLabel(master=self.panel_izquierdo, text=" ",image=self.img_bg)
        self.ico_user_panel = CustomTK.CTkLabel(master=self.frame_user, text=" ",image=self.icono_user_dashboard)
        self.bg_izq.place(x=0,y=0,relwidth=1, relheight=1)
        self.ico_user_panel.place(x=75,y=25,anchor=tk.W)
        # background cajas personalizadas
        self.backgound_1 = CustomTK.CTkLabel(master=self.frame_estadistica_profesor, text=" ",image=self.bg_pink)
        self.backgound_2 = CustomTK.CTkLabel(master=self.frame_estadistica_estudiantes, text=" ",image=self.bg_cian)
        self.backgound_3 = CustomTK.CTkLabel(master=self.frame_estadistica_aulas, text=" ",image=self.bg_yellow)
        self.backgound_4 = CustomTK.CTkLabel(master=self.frame_estadistica_trabajadores, text=" ",image=self.bg_blue_light)
        self.backgound_1.place(x=0,y=0,relwidth=1, relheight=1)
        self.backgound_2.place(x=0,y=0,relwidth=1, relheight=1)
        self.backgound_3.place(x=0,y=0,relwidth=1, relheight=1)
        self.backgound_4.place(x=0,y=0,relwidth=1, relheight=1)
        # labels frame nav
        
        
        # -----------------------------------------------------------------------------------------
        #texto#
        self.tituloDeEstadistica = CustomTK.CTkLabel(master=self.estadistica_frame,text="Estadisticas Generales",font=var.font_text_bold_small)
        
        self.textProfesores = CustomTK.CTkLabel(master=self.frame_estadistica_profesor,text="Profesores",
                                                text_color=var.text_white,
                                                bg_color=var.bg_pink,
                                                font=var.font_text_amaranth_medium,
                                                )
        
        self.numProfesores = CustomTK.CTkLabel(master=self.frame_estadistica_profesor,
                                                text=(self.var1),
                                                text_color=var.text_white,
                                                bg_color=var.bg_pink,
                                                font=var.font_text_amaranth_hight,
                                                )
        # ----------------------------------------------------------------------------
        self.textEstudiantes = CustomTK.CTkLabel(master=self.frame_estadistica_estudiantes,text="Estudiantes",
                                                text_color=var.text_white,
                                                bg_color=var.bg_cian,
                                                font=var.font_text_amaranth_medium,
                                                )
        
        self.numEstudiantes = CustomTK.CTkLabel(master=self.frame_estadistica_estudiantes,
                                                text=(self.var2),
                                                text_color=var.text_white,
                                                bg_color=var.bg_cian,
                                                font=var.font_text_amaranth_hight,
                                                )
        # -----------------------------------------------------------------------------
        self.textAulas = CustomTK.CTkLabel(master=self.frame_estadistica_aulas,text="Aulas",
                                                text_color=var.text_white,
                                                bg_color=var.bg_yellow,
                                                font=var.font_text_amaranth_medium,
                                                )
        
        self.numAulas = CustomTK.CTkLabel(master=self.frame_estadistica_aulas,
                                                text=(self.var3),
                                                text_color=var.text_white,
                                                bg_color=var.bg_yellow,
                                                font=var.font_text_amaranth_hight,
                                                )
        # ---------------------------------------------------------------------
        self.textTrabajadores = CustomTK.CTkLabel(master=self.frame_estadistica_trabajadores,text="Trabajadores",
                                                text_color=var.text_white,
                                                bg_color=var.bg_blue_light,
                                                font=var.font_text_amaranth_medium,
                                                )
        
        self.numTrabajadores = CustomTK.CTkLabel(master=self.frame_estadistica_trabajadores,
                                                text=(self.var4),
                                                text_color=var.text_white,
                                                bg_color=var.bg_blue_light,
                                                font=var.font_text_amaranth_hight,
                                                )
        # ---------------------------------------------------------------------
        self.textPanel = CustomTK.CTkLabel(master=self.panel_izquierdo,
                                                text="Panel Administrativo",
                                                text_color=var.text_white,
                                                bg_color=var.bg_blue_osc,
                                                font=var.font_text_amaranth_small,
                                                )
        
        # ---------------------------------------------------------------------
        self.textPanelUser = CustomTK.CTkLabel(master=self.frame_user,
                                                text=self.textuser,
                                                text_color=var.text_black,
                                                font=var.font_text_amaranth_ultra_small,
                                                )
        
        
        # ---------------------------------------------------------------------
        
        self.tituloDeEstadistica.place(x=340,y=40,anchor=tk.CENTER)
        self.textProfesores.place(x=80,y=30,anchor=tk.CENTER)
        self.textEstudiantes.place(x=78,y=30,anchor=tk.CENTER)
        self.textAulas.place(x=75,y=30,anchor=tk.CENTER)
        self.textTrabajadores.place(x=85,y=30,anchor=tk.CENTER)
        self.textPanel.place(x=100,y=50,anchor=tk.CENTER)
        # ----------------------------------------------------------------------
        self.numProfesores.place(x=80,y=80,anchor=tk.CENTER)
        self.numEstudiantes.place(x=80,y=80,anchor=tk.CENTER)
        self.numAulas.place(x=80,y=80,anchor=tk.CENTER)
        self.numTrabajadores.place(x=80,y=80,anchor=tk.CENTER)
        # -------------------------------------------------------------------------------------------
        self.textPanelUser.place(x=15,y=25,anchor=tk.W)        
        # -------------------------------------------------------------------------------------------

    def count_total(self):
        self.var1 = 17
        self.var2 = 100
        self.var3 = 6
        self.var4 = 10
        
    def TextVars(self):
        self.textuser = "Director"
    
    def crear_botones(self):

        self.Inicio = CustomTK.CTkButton(master=self.panel_izquierdo,
                                    width=115,
                                    text="Inicio",
                                    corner_radius=10,
                                    hover_color="#0355C0",
                                    bg_color="#0462CF",
                                    fg_color=var.blue_panel_button,
                                    font=var.font_text_button)
    
        self.Perfil = CustomTK.CTkButton(master=self.panel_izquierdo,
                                    width=115,
                                    text="Perfil",
                                    corner_radius=10,
                                    hover_color="#0355C0",
                                    bg_color="#045DC9",
                                    fg_color=var.blue_panel_button,
                                    font=var.font_text_button)

        self.Administracion = CustomTK.CTkButton(master=self.panel_izquierdo,
                                    width=100,
                                    text="Administracion",
                                    corner_radius=10,
                                    hover_color="#0355C0",
                                    bg_color="#0458C3",
                                    fg_color=var.blue_panel_button,
                                    font=var.font_text_button_medium)

        self.Configuracion = CustomTK.CTkButton(master=self.panel_izquierdo,
                                    width=115,
                                    text="Configuracion",
                                    corner_radius=10,
                                    hover_color="#0355C0",
                                    bg_color="#0353BD",
                                    fg_color=var.blue_panel_button,
                                    font=var.font_text_button_medium)
        
        self.Salir = CustomTK.CTkButton(master=self.panel_izquierdo,
                                    width=115,
                                    text="Salir",
                                    corner_radius=10,
                                    hover_color="#0355C0",
                                    bg_color="#022A8B",
                                    fg_color=var.blue_panel_button,
                                    font=var.font_text_button_medium)

        self.Inicio.place(x=100,y=120,anchor=tk.CENTER)
        self.Perfil.place(x=100,y=165,anchor=tk.CENTER)
        self.Administracion.place(x=100,y=210,anchor=tk.CENTER)
        self.Configuracion.place(x=100,y=255,anchor=tk.CENTER)
        self.Salir.place(x=100,y=600,anchor=tk.CENTER)

        
        
        #--------------------------------------------------------------------------------
    def ConfigurarcionDeApariencia(self):
        # definicion de apariencia
        CustomTK.set_appearance_mode("light")
        CustomTK.set_default_color_theme("blue")

    def CreacionDeVentana(self):
        # creacion de ventana
        self.app = CustomTK.CTk()
        self.app.geometry("1024x700")
        self.app.resizable(0,0)
        self.app.title("Dashboard")

    def agregar_widgets(self):
        # Agregar Funciones costructoras de nuevos wighets
        self.CrearFrames()
        self.CrearLabel()
        self.crear_botones()

    def run(self):
        # Funcion auto-ejecutable
        self.app.mainloop() #esto tiene que ir de ultimo

# Crear y ejecutar aplicación
app = Dashboard()
app.run()