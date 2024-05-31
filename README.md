# Proyecto-Trayecto_2

-Eber colmenares
-Anthony Mora
-Leandro Galavis
-Angel (apellido)

SELECT E.est_nombre, E.est_apellido, E.est_edad, G.grado, G.seccion, R.repre_nombre, R.repre_apellido, R.repre_edad, R.repre_cedula
FROM estudiantes as E
INNER JOIN representante as R ON E.id_representante = R.id_representante
INNER JOIN grado_rufino as G ON E.id_grado = G.id_grado;
