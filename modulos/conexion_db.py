import sqlite3

# Conectar a la base de datos (o crearla si no existe)
conn = sqlite3.connect('./bd_rufino/bd_escuela.db')

# Crear un cursor para interactuar con la base de datos
cursor = conn.cursor()

# Ejemplo de consulta de datos
cursor.execute("""
               SELECT
p.id_personal,
p.primer_nombre,
p.segundo_nombre,
p.primer_apellido,
p.segundo_apellido,
p.genero,
g.grado
FROM
Personal p
JOIN
Docente d ON p.id_personal = d.id_personal
JOIN
Grado g ON d.id_grado = g.id_grado;
""")
filas = cursor.fetchall()

for fila in filas:
    print(fila)

# Cerrar la conexión
conn.close()
