# Proyecto-Trayecto_2

-Eber colmenares
-Anthony Mora
-Leandro Galavis
-Angel (apellido)

Consultas:

SELECT p.primer_nombre, p.segundo_nombre, p.apellido_paterno, p.apellido_materno, p.genero, d.grado_especialidad, g.grado FROM Personal p JOIN Docente d ON p.id_personal = d.id_personal JOIN Grado g ON d.id_grado = g.id_grado;
