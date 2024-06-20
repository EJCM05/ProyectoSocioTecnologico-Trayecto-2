import customtkinter as ctk
from modulos.variables import variables as var
from PIL import ImageTk, Image
import fitz  # Importar PyMuPDF
from modulos.crear_descargar_pdf.descarga_pdf import descargar_pdf

class SubGradosVentana:
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
                                           font=var.Amaranth_medium
                                           )
        
        self.texto_seleccion.place(relx=0.5, rely=0.06, anchor="center")
    
    
    """ # importando imagenes e iconos
    def importar_img_matricula(self):
        # importardo imagen
        self.img_matricula_original = Image.open(f"matricula_pdf_img/img/matricula_{self.nombre_archivo}.jpg")
        
        # ajustando al tamaño deseado. imagen.resize((nuevo_ancho, nuevo_alto), suavizar y mejorar la calidad)
        self.img_matricula_ajustada = self.img_matricula_original.resize((1000, 1415), Image.LANCZOS)

        # asignando a la variable que va a ser usada
        self.img_matricula = ImageTk.PhotoImage(self.img_matricula_ajustada)"""
    
    
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
                             font=var.Amaranth_small,
                             fg_color=var.buttons_color,
                             hover_color=var.hover_buttons_color,
                             corner_radius=10,
                             command=lambda: descargar_pdf(nombre_archivo=self.nombre_archivo)
                             )
        boton.place(relx=0.5, rely=0.94, anchor="center")



"""import customtkinter as ctk
from modulos.variables import variables as var
from PIL import ImageTk, Image

class SubGradosVentana:
    def __init__(self, master, nombre_grado):
        self.master = master
        self.nombre_grado = nombre_grado
    
    
    def mostrar(self):
        # Eliminar widgets anteriores en el área de contenido
        for widget in self.master.winfo_children():
            widget.destroy()
        
        self.importar_img_matricula()
        self.texto_titulo()
        self.area_matricula()
    
    
    def texto_titulo(self):
        self.texto_seleccion = ctk.CTkLabel(master=self.master,
                                           text=self.nombre_grado,
                                           text_color=var.text_black,
                                           font=var.Amaranth_medium
                                           )
        
        self.texto_seleccion.place(relx=0.5, rely=0.06, anchor="center")
    
    
    # importando imagenes e iconos
    def importar_img_matricula(self):
        # importardo imagen
        self.img_matricula_original = Image.open("matricula_pdf_img/pagina_0.jpg")
        
        # ajustando al tamaño deseado. imagen.resize((nuevo_ancho, nuevo_alto), suavizar y mejorar la calidad)
        self.img_matricula_ajustada = self.img_matricula_original.resize((1000, 1415), Image.LANCZOS)

        # asignando a la variable que va a ser usada
        self.img_matricula = ImageTk.PhotoImage(self.img_matricula_ajustada)
    
    
    def area_matricula(self):
        self.contenedor_matricula = ctk.CTkFrame(master=self.master,
                                 width=1000,
                                 height=1415,
                                 corner_radius=0,
                                 fg_color="green"
                                 )
        
        self.matricula = ctk.CTkLabel(master=self.contenedor_matricula,
                                    image=self.img_matricula,
                                    text="",
                                    )
        
        self.contenedor_matricula.place(relx=0.5, rely=0.1, anchor="n")
        self.matricula.place(relx=0.5, rely=0, anchor="n")"""


#--------------------

"""import customtkinter as ctk
from modulos.variables import variables as var
from PIL import ImageTk, Image

class SubGradosVentana:
    def __init__(self, master, nombre_grado):
        self.master = master
        self.nombre_grado = nombre_grado
    
    
    def mostrar(self):
        # Eliminar widgets anteriores en el área de contenido
        for widget in self.master.winfo_children():
            widget.destroy()
        
        self.importar_img_matricula()
        self.texto_titulo()
        self.area_matricula()
    
    
    def texto_titulo(self):
        self.texto_seleccion = ctk.CTkLabel(master=self.master,
                                           text=self.nombre_grado,
                                           text_color=var.text_black,
                                           font=var.Amaranth_medium
                                           )
        
        self.texto_seleccion.place(relx=0.5, rely=0.06, anchor="center")
    
    
    # importando imagenes e iconos
    def importar_img_matricula(self):
        # importardo imagen
        self.img_matricula_original = Image.open("imagenes/pagina_0.jpg")
        
        # ajustando al tamaño deseado. imagen.resize((nuevo_ancho, nuevo_alto), suavizar y mejorar la calidad)
        self.img_matricula_ajustada = self.img_matricula_original.resize((1000, 1415), Image.LANCZOS)

        # asignando a la variable que va a ser usada
        self.img_matricula = ImageTk.PhotoImage(self.img_matricula_ajustada)
    
    
    def area_matricula(self):
        self.contenedor_matricula = ctk.CTkFrame(master=self.master,
                                 width=1000,
                                 height=500,
                                 corner_radius=0,
                                 fg_color="green"
                                 )
        
        self.matricula = ctk.CTkLabel(master=self.contenedor_matricula,
                                    image=self.img_matricula,
                                    text="",
                                    )
        
        self.contenedor_matricula.place(relx=0.5, rely=0.5, anchor="center")
        self.matricula.place(relx=0.5, rely=0.5, anchor="center")"""



"""import os
import fitz  # Importa PyMuPDF
from PIL import Image

# Ruta completa al archivo PDF
pdf_file = "imagenes/matricula.pdf"
pdf_document = fitz.open(pdf_file)

# Crea la carpeta "imagenes" si no existe
if not os.path.exists("imagenes"):
    os.makedirs("imagenes")

# Convierte cada página a imagen JPG y guárdala en la carpeta "imagenes"
for page_number in range(len(pdf_document)):
    page = pdf_document[page_number]
    image = page.get_pixmap(matrix=fitz.Matrix(2, 2))  # Ajusta la escala según tus necesidades
    img_bytes = image.samples  # Obtiene los bytes de la imagen
    img = Image.frombytes("RGB", (image.width, image.height), img_bytes)
    img_path = os.path.join("imagenes", f"pagina_{page_number}.jpg")
    img.save(img_path, "JPEG")  # Guarda la imagen como JPG

# Cierra el archivo PDF
pdf_document.close()"""
