# import sqlite3

# def asignar_representante_repetido(cedula):
#       # Conectarse a la base de datos
#         conn = sqlite3.connect('./bd_rufino/bd_escuela.db')
#         c = conn.cursor()

#         # Insertar valores en la tabla
#         c.execute(f"SELECT id_representante FROM Representante WHERE cedula = {cedula}")
#         info = c.fetchall()
        
#         print(info)

#         for tupla in info:
#           id_representante = (str(tupla[0]))
          
#         print(id_representante)
        
#         c.execute(f"SELECT id_estudiante FROM Estudiante ORDER BY id_estudiante DESC LIMIT 1;")
#         result = c.fetchall()
#         valor = result[0][0]
#         print(valor)
        
#         c.execute(f"UPDATE Estudiante SET id_representante = {id_representante} WHERE id_estudiante = {valor};")
        
#         # Confirmar los cambios y cerrar la conexión
#         conn.commit()
#         conn.close()
        
# asignar_representante_repetido(555)