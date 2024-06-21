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
        consulta_sql = """SELECT E.primer_nombre, E.segundo_nombre, E.primer_apellido,
                          E.segundo_apellido, E.fecha_nacimiento, G.grado_nombre, R.primer_nombre, R.primer_apellido, R.cedula
                          FROM Estudiante as E
                          JOIN Grado as G ON G.id_grado = E.id_grado
                          JOIN Representante as R ON E.id_representante = R.id_representante""" 
                          #consulta_sql aqui
        consulta_sql = """
                      SELECT * FROM Ingreso
                      """
        cursor.execute(consulta_sql)
        info = cursor.fetchall()
        con.close()
        print(info)

modelo = Modelo()  # Crear una instancia de la clase
modelo.SelectAll_usuarios()

#modelo.Validate_login()  # Llamar al método