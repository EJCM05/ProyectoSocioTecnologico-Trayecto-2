import matplotlib.pyplot as plt
from modulos.variables import variables as var

def crear_estadistica_general(lista_datos):
    nombres_datos = ['Simoncito', 'Inicial A', 'Inicial B', 'Inicial C', '1er Grado', '2do Grado', '3er Grado', '4to Grado', '5to Grado', '6to Grado']

    # Colores para cada barra (puedes personalizar esta lista)
    colores = [var.btn_gray, var.btn_pink, var.btn_beige, var.btn_gold, var.btn_blue, var.btn_red_black, var.btn_purple, var.btn_green, var.btn_lila, var.btn_blueosc]

    # Crear una figura y un eje
    # fig, ax = plt.subplots()
    fig, ax = plt.subplots(figsize=(10, 6))  # Ancho: 10 pulgadas, Alto: 6 pulgadas
    ax.bar(nombres_datos, lista_datos, color=colores)
    ax.set_xlabel('Grado',fontsize=14)
    ax.set_ylabel('Cantidad de Estudiantes',fontsize=14)
    ax.set_title('Estudiantes Totales',fontsize=14)

    # Rotar las etiquetas en el eje x para mayor legibilidad
    plt.xticks(rotation=20, fontsize=12)

    # Agregar etiquetas a las barras
    for i, valor in enumerate(lista_datos):
        ax.text(i, valor, str(valor), ha='center', va='bottom', fontsize=14)
    # Agregar color de fondo a la figura
    fig.set_facecolor('#E5E5E5')  # Cambia el color según tus preferencias

    # Guardar la figura como una imagen
    fig.savefig('matricula_pdf_img/img_estadistica_general/estadistica_general.png')
    plt.close(fig)