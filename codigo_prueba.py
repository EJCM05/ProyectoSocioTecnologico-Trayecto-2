# import sqlite3

# # Conectarse a la base de datos
# conn = sqlite3.connect('./bd_rufino/bd_escuela.db')
# c = conn.cursor()

# # Insertar valores en la tabla
# c.execute(f"""SELECT G.grado_nombre, COUNT(E.id_estudiante) AS cantidad_alumnos FROM Grado G LEFT JOIN Estudiante E ON G.id_grado = E.id_grado GROUP BY G.id_grado, G.grado_nombre ORDER BY G.id_grado;""")
# result = c.fetchall()

# print(result)

# lista = []
        
# for element in result:
#   lista.append(element[1])
# print(lista)

# # Confirmar los cambios y cerrar la conexión
# conn.commit()
# conn.close()