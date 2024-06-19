from modulos.modelo import Modelo

class Controlador():
    def __init__(self, modelo):
        self.modelo = modelo

    def consultar_usuario(self):
        info = self.modelo.SelectAll_usuarios()
        print(info)
        return info

modelo = Modelo()  # Crear una instancia de la clase Modelo
controlador = Controlador(modelo)  # Pasar la instancia al controlador
controlador.consultar_usuario()  # Llamar al método
