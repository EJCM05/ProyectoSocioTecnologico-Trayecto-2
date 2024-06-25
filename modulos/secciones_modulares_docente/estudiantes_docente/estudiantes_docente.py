import customtkinter as ctk
from modulos.variables import variables as var
from PIL import ImageTk, Image
import fitz  # Importar PyMuPDF
from modulos.crear_descargar_pdf.descarga_pdf import descargar_pdf

class EstudiantesDocenteVentana:
    def __init__(self, master, nombre_grado):
        self.master = master
        self.nombre_grado = nombre_grado
    
    
    def pdf_a_img(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo
        pdf_ruta = "matricula_pdf_img/pdf/matricula_"+self.nombre_archivo+".pdf"  # Ruta al archivo PDF

        # Abrir el archivo PDF
        pdf_documento = fitz.open(pdf_ruta)

        # Obtener la primera página del PDF
        pagina = pdf_documento[0]

        # Renderizar la página como una imagen
        pix = pagina.get_pixmap(matrix=fitz.Matrix(2, 2))  # Ajusta el factor de escala según tus necesidades

        # Guardar la imagen como un archivo temporal
        temp_image_path = "matricula_pdf_img/img/matricula_"+self.nombre_archivo+".jpg"
        pix.pil_save(temp_image_path)

        img_matricula_original = Image.open(temp_image_path)

        # Ajustar al tamaño deseado. imagen.resize((nuevo_ancho, nuevo_alto), suavizar y mejorar la calidad)
        img_matricula_ajustada = img_matricula_original.resize((1000, 1415), Image.LANCZOS)

        # Asignar a la variable que va a ser usada
        self.img_matricula = ImageTk.PhotoImage(img_matricula_ajustada)
    
    
    def mostrar(self):
        # Eliminar widgets anteriores en el área de contenido
        for widget in self.master.winfo_children():
            widget.destroy()
        
        self.texto_titulo()
        self.area_matricula()
        self.boton_descargar()
    
    
    def texto_titulo(self):
        self.texto_seleccion = ctk.CTkLabel(master=self.master,
                                           text=self.nombre_grado,
                                           text_color=var.text_black,
                                           font=var.Andika_large
                                           )
        
        self.texto_seleccion.place(relx=0.5, rely=0.06, anchor="center")
    
    
    def area_matricula(self):
        self.contenedor_matricula = ctk.CTkScrollableFrame(master=self.master,
                                 width=1000,
                                 height=500,
                                 corner_radius=0,
                                 fg_color=var.bg_white
                                 )
        
        self.matricula = ctk.CTkLabel(master=self.contenedor_matricula,
                                    image=self.img_matricula,
                                    text="",
                                    )
        
        self.contenedor_matricula.place(relx=0.5, rely=0.1, anchor="n")
        self.matricula.pack()
    
    
    def boton_descargar(self):
        boton = ctk.CTkButton(master=self.master,
                             text="Descargar Matricula",
                             width=180,
                             height=50,
                             font=var.Andika_small,
                             text_color=var.text_white,
                             fg_color=var.btn_blue,
                             hover_color=var.hover_button_blue,
                             corner_radius=10,
                             command=lambda: descargar_pdf(nombre_archivo=self.nombre_archivo)
                             )
        boton.place(relx=0.5, rely=0.94, anchor="center")