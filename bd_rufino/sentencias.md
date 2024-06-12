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
