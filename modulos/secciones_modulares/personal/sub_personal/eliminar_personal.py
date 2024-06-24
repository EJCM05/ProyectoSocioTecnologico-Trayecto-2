from CTkMessagebox import CTkMessagebox
import sqlite3

def eliminar_personal(cedula):
    print(cedula)
    
    # Conectarse a la base de datos
    conn = sqlite3.connect('./bd_rufino/bd_escuela.db')
    c = conn.cursor()

    # Insertar valores en la tabla
    c.execute(f"DELETE FROM Estudiante WHERE cedula = {cedula}")

    # Confirmar los cambios y cerrar la conexión
    conn.commit()
    conn.close()
    
    #No eliminar
    texto_emergente = "Personal Eliminado Correctamente"
    CTkMessagebox(title="Información", message=texto_emergente)