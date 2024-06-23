import customtkinter as ctk
from modulos.vista import Vistadoc
from modulos.controlador import Controlador
from modulos.modelo import Modelo


bd = Modelo() #Instanciamos el modelo
vista = Vista() #Instanciamos la vista sin pasar 'ventana' como argumento
controlador = Controlador(bd) #Instanciamos el controlador y le pasamos el modelo
vista.set_controlador(controlador) #Establecemos el controlador para la vista

#Programa principal
if __name__ == '__main__':
    vista.run()