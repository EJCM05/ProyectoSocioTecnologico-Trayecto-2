from fpdf import FPDF

class CrearPDF:
    def __init__(self):
        self.pdf = FPDF(orientation='P', unit='cm', format='A3')  # creación del archivo
        self.pdf.add_page()

    
    def creacion(self, nombre_pdf, lista):
        #recibe una lista como parametro y un nombre para poner al archivo pdf
        self.nombre_pdf = nombre_pdf
        self.lista_de_datos = lista

        # Título
        self.pdf.set_font('Arial', '', 16)
        self.pdf.cell(0, 2, 'Datos de Estudiantes', border=1, ln=1, align='C', fill=0)

        # Columnas
        self.pdf.set_font('Arial', '', 12)
        self.pdf.cell(4, 1, "Cedula de ID", border=1, align='C', fill=0)
        self.pdf.cell(9, 1, "Nombres y Apellidos", border=1, align='C', fill=0)
        self.pdf.cell(2, 1, "Edad", border=1, align='C', fill=0)
        self.pdf.cell(4, 1, "Estado", border=1, align='C', fill=0)
        self.pdf.cell(0, 1, "Direccion", border=1, align='C', fill=0, ln=1)

        # Agregar los datos de la lista al PDF
        for valor in self.lista_de_datos:
            self.pdf.cell(4, 1, valor[0], border=1, align='C', fill=0)
            self.pdf.cell(9, 1, valor[1], border=1, align='C', fill=0)
            self.pdf.cell(2, 1, valor[2], border=1, align='C', fill=0)
            self.pdf.cell(4, 1, valor[3], border=1, align='C', fill=0)
            self.pdf.cell(0, 1, valor[4], border=1, align='C', fill=0, ln=1)

        # Guardar el archivo PDF
        self.pdf.output("matricula_pdf_img/pdf/matricula_"+self.nombre_pdf+".pdf")

