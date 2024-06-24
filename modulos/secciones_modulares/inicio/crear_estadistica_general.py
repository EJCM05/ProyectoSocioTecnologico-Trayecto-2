# codigo nuevo
import matplotlib.pyplot as plt


import matplotlib.pyplot as plt

def crear_estadistica_general(lista_datos):
     nombres_datos = ['Simoncito', 'Inicial A', 'Inicial B', 'Inicial C', '1er Grado', '2do Grado', '3er Grado', '4to Grado', '5to Grado', '6to Grado']

     # Crear una figura y un eje
     fig, ax = plt.subplots()
     ax.plot(lista_datos, marker='o', linestyle='-', color='b')
     ax.set_xlabel('Índice')
     ax.set_ylabel('Cantidad de Estudiantes')
     ax.set_title('Número de Estudiantes por Grado')

     # Establecer las etiquetas en el eje x
     ax.set_xticks(range(len(lista_datos)))
     ax.set_xticklabels(nombres_datos, rotation=20)

     # Agregar etiquetas a los puntos
     for i, valor in enumerate(lista_datos):
         ax.annotate(f'{valor}', (i, valor), textcoords="offset points", xytext=(10, -10), ha='center')

     # Guardar la figura como una imagen
     fig.savefig('matricula_pdf_img/img_estadistica_general/estadistica_general.png')
     plt.close(fig)