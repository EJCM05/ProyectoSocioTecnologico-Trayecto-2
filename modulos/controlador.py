from modulos.modelo import Modelo

class Controlador():
    def __init__(self, modelo):
        self.modelo = modelo

    def consultar_usuario(self):
        info = self.modelo.SelectAll_usuarios()
        # print(info) aca se testea
        return info
    # insertar la validacion aca
    
    def Validate_login(self, username, password):
        return self.modelo.Validate_login(username, password)





modelo = Modelo()  # Crear una instancia de la clase Modelo
controlador = Controlador(modelo)  # Pasar la instancia al controlador
controlador.consultar_usuario()  # Llamar al método
