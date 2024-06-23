import sqlite3

def obtener_info_estudiante():
  # Conectarse a la base de datos
  conn = sqlite3.connect('./bd_rufino/bd_escuela.db')
  c = conn.cursor()

  user = input("Ingrese la cedula del estudiante a actualizar:  ")

  # Insertar valores en la tabla
  c.execute(f"SELECT primer_nombre, segundo_nombre, primer_apellido, segundo_apellido, cedula, fecha_nacimiento, genero FROM Estudiante WHERE cedula = {user}")

  info = c.fetchall()
  print(info)

  for tupla in info:
    nombres = f"{tupla[0]} {tupla[1]}"
    apellidos = f"{tupla[2]} {tupla[3]}"
    cedula = tupla[4]
    fecha_nacimiento = tupla[5]
    genero = tupla[6]

  año, mes, dia = fecha_nacimiento.split("/")

  lista = [nombres, apellidos, cedula, año, mes, dia, genero]
  print(lista)

  # Confirmar los cambios y cerrar la conexión
  conn.commit()
  conn.close()
  
  return lista

def actualizar_informacion():
  # Conectarse a la base de datos
  conn = sqlite3.connect('./bd_rufino/bd_escuela.db')
  c = conn.cursor()
  
  lista = obtener_info_estudiante()
  
  nombre_1, nombre_2 = lista[0].split()
  apellido_1, apellido_2 = lista[1].split()
  cedula = lista[2]
  fecha_nacimiento = f"{lista[3]}/{lista[4]}/{lista[5]}"
  genero = lista[6]
  
  valores_nuevos = (nombre_1, nombre_2, apellido_1, apellido_2, cedula, fecha_nacimiento, genero)
  print(valores_nuevos)
  
  # Insertar valores en la tabla
  # c.execute("""UPDATE Estudiante SET primer_nombre = ?, segundo_nombre = ?, primer_apellido, segundo_apellido, cedula, fecha_nacimiento, genero WHERE cedula = ?; """, (nombre_1, nombre_2, apellido_1, apellido_2, cedula, fecha_nacimiento, genero, user))
  
  # Confirmar los cambios y cerrar la conexión
  conn.commit()
  conn.close()
  
actualizar_informacion()