DROP DATABASE IF EXISTS gestion_academica;
CREATE DATABASE gestion_academica;
USE gestion_academica;

CREATE TABLE Departamento (
    id_departamento INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL
);

CREATE TABLE Estudiante (
    id_estudiante INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100),
    fecha_nacimiento DATE
);

CREATE TABLE Profesor (
    id_profesor INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    id_departamento INT,
    FOREIGN KEY (id_departamento) REFERENCES Departamento(id_departamento)
);

CREATE TABLE Curso (
    id_curso INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    id_departamento INT,
    FOREIGN KEY (id_departamento) REFERENCES Departamento(id_departamento)
);

CREATE TABLE Clase (
    id_clase INT PRIMARY KEY AUTO_INCREMENT,
    id_curso INT NOT NULL,
    id_profesor INT NOT NULL,
    semestre VARCHAR(20),
    anio INT,
    FOREIGN KEY (id_curso) REFERENCES Curso(id_curso),
    FOREIGN KEY (id_profesor) REFERENCES Profesor(id_profesor)
);

CREATE TABLE Inscripcion (
    id_inscripcion INT PRIMARY KEY AUTO_INCREMENT,
    id_estudiante INT NOT NULL,
    id_clase INT NOT NULL,
    fecha_inscripcion DATE,
    FOREIGN KEY (id_estudiante) REFERENCES Estudiante(id_estudiante),
    FOREIGN KEY (id_clase) REFERENCES Clase(id_clase)
);

CREATE TABLE Calificacion (
    id_calificacion INT PRIMARY KEY AUTO_INCREMENT,
    id_inscripcion INT NOT NULL,
    nota DECIMAL(5,2),
    fecha_registro DATE,
    FOREIGN KEY (id_inscripcion) REFERENCES Inscripcion(id_inscripcion)
);

INSERT INTO Departamento(nombre) VALUES
('Ingeniería'),
('Ciencias'),
('Administración');

INSERT INTO Estudiante(nombre, apellido, fecha_nacimiento) VALUES
('Carlos','Ramírez','2002-05-10'),
('Ana','Gómez','2001-08-21');

INSERT INTO Profesor(nombre, id_departamento) VALUES
('Juan Pérez',1),
('Laura Méndez',2);

INSERT INTO Curso(nombre,id_departamento) VALUES
('Programación',1),
('Matemática',2);

INSERT INTO Clase(id_curso,id_profesor,semestre,anio) VALUES
(1,1,'Enero-Mayo',2025),
(2,2,'Agosto-Diciembre',2025);

INSERT INTO Inscripcion(id_estudiante,id_clase,fecha_inscripcion) VALUES
(1,1,'2025-02-01'),
(2,2,'2025-09-01');

INSERT INTO Calificacion(id_inscripcion,nota,fecha_registro) VALUES
(1,95,'2025-03-10'),
(1,87,'2025-04-05'),
(2,72,'2025-10-15');

SELECT * FROM Departamento;
SELECT * FROM Estudiante;
SELECT * FROM Profesor;
SELECT * FROM Curso;
SELECT * FROM Clase;
SELECT * FROM Inscripcion;
SELECT * FROM Calificacion;

SELECT nombre FROM Estudiante;
SELECT nombre, apellido FROM Estudiante WHERE apellido='Gómez';
SELECT nombre FROM Curso WHERE id_departamento=1;



SELECT Curso.nombre AS curso, Departamento.nombre AS departamento
FROM Curso
JOIN Departamento ON Curso.id_departamento = Departamento.id_departamento;

SELECT Estudiante.nombre AS estudiante, Curso.nombre AS curso, Profesor.nombre AS profesor
FROM Inscripcion
JOIN Estudiante USING(id_estudiante)
JOIN Clase USING(id_clase)
JOIN Curso USING(id_curso)
JOIN Profesor USING(id_profesor);

SELECT Estudiante.nombre AS estudiante, Clase.semestre, Curso.nombre AS curso
FROM Inscripcion
JOIN Estudiante USING(id_estudiante)
JOIN Clase USING(id_clase)
JOIN Curso USING(id_curso);


SELECT Estudiante.nombre, AVG(Calificacion.nota) AS promedio
FROM Calificacion
JOIN Inscripcion USING(id_inscripcion)
JOIN Estudiante USING(id_estudiante)
GROUP BY Estudiante.id_estudiante;

SELECT Curso.nombre, COUNT(Inscripcion.id_estudiante) AS total_inscritos
FROM Curso
JOIN Clase USING(id_curso)
JOIN Inscripcion USING(id_clase)
GROUP BY Curso.id_curso;

SELECT Estudiante.nombre AS estudiante, COUNT(Calificacion.id_calificacion) AS cantidad_notas
FROM Estudiante
JOIN Inscripcion USING(id_estudiante)
JOIN Calificacion USING(id_inscripcion)
GROUP BY Estudiante.id_estudiante;

INSERT INTO Estudiante(nombre, apellido, fecha_nacimiento)
VALUES ('Miguel','Santos','2003-06-15');

UPDATE Estudiante SET apellido='Martínez' WHERE id_estudiante=1;

DELETE FROM Calificacion WHERE id_calificacion=2;
