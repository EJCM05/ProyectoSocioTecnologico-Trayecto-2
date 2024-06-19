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


SELECT E.primer_nombre, E.segundo_nombre, E.primer_apellido,
 E.segundo_apellido, E.fecha_nacimiento, G.grado_nombre, R.primer_nombre, R.primer_apellido, R.cedula, R.genero
FROM Estudiante as E
JOIN Grado as G ON G.id_grado = E.id_grado
JOIN Representante as R ON E.id_representante = R.id_representante