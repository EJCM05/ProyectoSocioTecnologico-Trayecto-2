import sqlite3

# Ejemplo de consulta de datos (reemplaza 'nombre_tabla' con el nombre real de tu tabla)

class Modelo():
    def conectar(self):
        try:
            # Conectar a la base de datos (o crearla si no existe)
            conn = sqlite3.connect('./bd_rufino/bd_escuela.db')
            return conn
        except sqlite3.Error as e:
            print(f"Error al ejecutar la consulta: {e}")

    def SelectAll_usuarios(self):
        con = self.conectar()
        cursor = con.cursor()
        consulta_sql = "SELECT * FROM Ingreso" #consulta_sql aqui
        cursor.execute(consulta_sql)
        info = cursor.fetchall()
        con.close()
        return info

modelo = Modelo()  # Crear una instancia de la clase
modelo.SelectAll_usuarios()  # Llamar al método