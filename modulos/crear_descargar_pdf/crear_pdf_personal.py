from fpdf import FPDF

class CrearPDFPersonal:
    def __init__(self):
        self.pdf = FPDF(orientation='P', unit='cm', format='A3')
        self.pdf.add_page()
    
    
    def creacion(self, nombre_pdf, lista):
        self.nombre_pdf = nombre_pdf
        self.lista_de_datos = lista

        # Título
        titulo = self.nombre_pdf.capitalize()
        self.pdf.set_font('Arial', '', 16)
        self.pdf.cell(0, 2, f'Informacion del Personal {titulo}', border=1, ln=1, align='C', fill=0)

        # Columnas
        self.pdf.set_font('Arial', '', 12)
        self.pdf.cell(4, 1, "Cedula", border=1, align='C', fill=0)
        self.pdf.cell(9, 1, "Nombres y Apellidos", border=1, align='C', fill=0)
        self.pdf.cell(2, 1, "Edad", border=1, align='C', fill=0)
        self.pdf.cell(6, 1, "Fecha Nacimiento", border=1, align='C', fill=0)
        self.pdf.cell(0, 1, "Genero", border=1, align='C', fill=0, ln=1)

        # Agregar los datos de la lista al PDF
        for valor in self.lista_de_datos:
            self.pdf.cell(4, 1, valor[0], border=1, align='C', fill=0)
            self.pdf.cell(9, 1, valor[1], border=1, align='C', fill=0)
            self.pdf.cell(2, 1, valor[2], border=1, align='C', fill=0)
            self.pdf.cell(6, 1, valor[3], border=1, align='C', fill=0)
            self.pdf.cell(0, 1, valor[4], border=1, align='C', fill=0, ln=1)

        # Guardar el archivo PDF
        self.pdf.output("matricula_pdf_img/pdf_personal/informacion_personal_" + self.nombre_pdf + ".pdf")