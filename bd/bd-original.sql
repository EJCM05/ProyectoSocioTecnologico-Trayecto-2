CREATE DATABASE colegio;
USE colegio;

-- Tabla: Ingreso
CREATE TABLE Ingreso (
    usuario VARCHAR(50),
    contrasena VARCHAR(50) NOT NULL
);

-- Tabla: Escuela
CREATE TABLE Escuela (
    nombre VARCHAR(100) NOT NULL,
    aulas VARCHAR(50),
    personal VARCHAR(100),
    estudiantes VARCHAR(100),
    ubicacion VARCHAR(100)
);

-- Tabla: Personal
CREATE TABLE Personal (
    id_personal INT AUTO_INCREMENT PRIMARY KEY,
    primer_nombre VARCHAR(50),
    segundo_nombre VARCHAR(50),
    apellido_paterno VARCHAR(50),
    apellido_materno VARCHAR(50),
    cedula VARCHAR(20),
    genero CHAR(1)
);

-- Tabla: Grado
CREATE TABLE Grado (
    id_grado INT AUTO_INCREMENT PRIMARY KEY,
    grado VARCHAR(40)
);

-- Tabla: Obreros (hereda de Personal)
CREATE TABLE Obreros (
    id_personal INT,
    tarea VARCHAR(100),
    PRIMARY KEY (id_personal),
    FOREIGN KEY (id_personal) REFERENCES Personal(id_personal)
);

-- Tabla: Administrativos (hereda de Personal)
CREATE TABLE Administrativos (
    id_personal INT,
    cargo VARCHAR(100),
    grado_estudio VARCHAR(100),
    PRIMARY KEY (id_personal),
    FOREIGN KEY (id_personal) REFERENCES Personal(id_personal)
);

-- Tabla: Docente (hereda de Personal)
CREATE TABLE Docente (
    id_maestro INT AUTO_INCREMENT PRIMARY KEY,
    id_personal INT,
    id_grado INT,
    grado_especialidad VARCHAR(100),
    FOREIGN KEY (id_personal) REFERENCES Personal(id_personal),
    FOREIGN KEY (id_grado) REFERENCES Grado(id_grado)
);

-- Tabla: Representante
CREATE TABLE Representante (
    id_representante INT AUTO_INCREMENT PRIMARY KEY,
    primer_nombre VARCHAR(50),
    segundo_nombre VARCHAR(50),
    apellido_paterno VARCHAR(50),
    apellido_materno VARCHAR(50),
    fecha_nacimiento DATE,
    cedula VARCHAR(50),
    genero CHAR(1)
);

-- Tabla: Estudiante
CREATE TABLE Estudiante (
    id_estudiante INT AUTO_INCREMENT PRIMARY KEY,
    id_representante INT,
    id_grado INT,
    primer_nombre VARCHAR(50),
    segundo_nombre VARCHAR(50),
    apellido_paterno VARCHAR(50),
    apellido_materno VARCHAR(50),
    fecha_nacimiento DATE,
    genero CHAR(1),
    FOREIGN KEY (id_representante) REFERENCES Representante(id_representante)
);

-- Tabla: Calificacion
CREATE TABLE Calificacion (
    id_estudiante INT,
    lapso_I INT,
    lapso_II INT,
    lapso_III INT,
    PRIMARY KEY (id_estudiante),
    FOREIGN KEY (id_estudiante) REFERENCES Estudiante(id_estudiante)
);
