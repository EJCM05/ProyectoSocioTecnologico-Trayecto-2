import sqlite3

# Establecer la conexión con la base de datos
conexion = sqlite3.connect('bd/bd-rufino.db')

# Crear un cursor para ejecutar consultas
cursor = conexion.cursor()

# Ejecutar una consulta
# cursor.execute("""SELECT E.est_nombre, E.est_apellido, E.est_edad, G.grado, G.seccion, R.repre_nombre, R.repre_apellido, R.repre_edad, R.repre_cedula
# FROM estudiantes as E
# INNER JOIN representante as R ON E.id_representante = R.id_representante
# INNER JOIN grado_rufino as G ON E.id_grado = G.id_grado;""")
cursor.execute("""SELECT * From Director """)

# Obtener los resultados de la consulta
resultados = cursor.fetchall()

# Recorrer los resultados
for fila in resultados:
    print(fila)

# Cerrar la conexión
conexion.close()