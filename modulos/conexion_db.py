import sqlite3

# Conectar a la base de datos (o crearla si no existe)
conn = sqlite3.connect('./bd_rufino/bd_escuela.db')

# Crear un cursor para interactuar con la base de datos
cursor = conn.cursor()

# Ejemplo de consulta de datos (reemplaza 'nombre_tabla' con el nombre real de tu tabla)
consulta_sql = "SELECT * FROM Estudiante WHERE id_grado = 2"

try:
    cursor.execute(consulta_sql)
    filas = cursor.fetchall()
    for fila in filas:
        print(fila)
except sqlite3.Error as e:
    print(f"Error al ejecutar la consulta: {e}")

# Cerrar la conexión
conn.close()
