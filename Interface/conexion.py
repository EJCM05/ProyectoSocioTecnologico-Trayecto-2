# para empezar tenemos que iniciar los servicios en xampp
# luego iniciar los servicio de apache y mysql
# posteriormente en el navegador introducimos : localhost/phpmyadmin

# eliminar y crear Base de datos desde phpmyadmin
# eliminar: DROP DATABASE NOMBRE_TABLA
# crear: CREATE DATABASE NOMBRE_TABLA

# aca es el codigo, reecordar el import

import sys
from tkinter import *
import mariadb 

# codigo para conectarse y comprobar la base de datos

try:
    conexion = mariadb.connect(
        # todo debe de ir en strings menos el port
        user = "root", #nombre del usuario con privilegios
        password = "", #contraseña en caso de tenerla, si no la tiene se deja vacio
        host = "127.0.0.1", #se agreda la direccion ip del localhost
        port =3306, #este es el puerto por defecto 
        database = "colegio"  #nombre de la base de datos
        
    )
#la conexion.variable del nombre de la tabla es obligario
    cursor = conexion.cursor()    # esto va importante

except mariadb.Error as error:
    print(f"hay un error en la conexion: {error}")
    sys.exit(1)    #importar la libreria sys


def execute():
    try:
        # simplemente lo que cambia es la instruccion SQL el resto queda    
        consulta = cursor.execute("""
                    SELECT p.primer_nombre, p.segundo_nombre, p.apellido_paterno, p.apellido_materno, p.genero, d.grado_especialidad, g.grado FROM Personal p JOIN Docente d ON p.id_personal = d.id_personal JOIN Grado g ON d.id_grado = g.id_grado;
                    """)
        
        resultado = cursor.fetchall()
        
        for row in resultado:
            print("\t".join(map(str, row)))
        
        conexion.commit() 
    
    except mariadb.Error as error_registro:
        print(f"error en el registro {error_registro}")

execute()
    

