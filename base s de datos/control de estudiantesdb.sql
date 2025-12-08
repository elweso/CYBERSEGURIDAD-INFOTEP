-- CREACIÓN DE LA BASE DE DATOS Y TABLAS
CREATE DATABASE colegio;
USE colegio;

CREATE TABLE estudiantes (
    estudiante_id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    fecha_nacimiento DATE,
    direccion VARCHAR(255)
);

CREATE TABLE cursos (
    curso_id INT PRIMARY KEY AUTO_INCREMENT,
    nombre_curso VARCHAR(100) NOT NULL UNIQUE,
    creditos INT NOT NULL
);

CREATE TABLE matriculas (
    estudiante_id INT NOT NULL,
    curso_id INT NOT NULL,
    fecha_matricula DATE NOT NULL,
    nota DECIMAL(4, 2),
    PRIMARY KEY (estudiante_id, curso_id),
    FOREIGN KEY (estudiante_id) REFERENCES estudiantes(estudiante_id),
    FOREIGN KEY (curso_id) REFERENCES cursos(curso_id)
);

-- INSERCIÓN DE DATOS
INSERT INTO estudiantes (nombre, apellido, fecha_nacimiento, direccion) VALUES
('Sofía', 'Castro', '2008-05-15', 'Calle Falsa 123'),
('Pedro', 'López', '2007-11-20', 'Avenida Siempreviva 742'),
('Elena', 'Vargas', '2009-01-01', 'Bulevar de los Sueños 45');

INSERT INTO cursos (nombre_curso, creditos) VALUES
('Matemáticas Avanzadas', 5),
('Literatura Contemporánea', 4),
('Física Moderna', 6),
('Historia Mundial', 3);

INSERT INTO matriculas (estudiante_id, curso_id, fecha_matricula, nota) VALUES
(1, 1, '2025-08-01', 9.50),
(1, 2, '2025-08-01', 8.25);

INSERT INTO matriculas (estudiante_id, curso_id, fecha_matricula, nota) VALUES
(2, 3, '2025-08-05', 7.80),
(2, 4, '2025-08-05', 9.10);

INSERT INTO matriculas (estudiante_id, curso_id, fecha_matricula, nota) VALUES
(3, 1, '2025-08-10', 6.90);

-- CONSULTAS
-- 1. Estudiantes y sus Cursos
SELECT
    CONCAT(e.nombre, ' ', e.apellido) AS Estudiante,
    c.nombre_curso AS Curso,
    m.fecha_matricula
FROM estudiantes e
JOIN matriculas m ON e.estudiante_id = m.estudiante_id
JOIN cursos c ON m.curso_id = c.curso_id
ORDER BY Estudiante, Curso;

-- 2. Notas por Estudiante (Sofía Castro)
SELECT
    c.nombre_curso AS Curso,
    m.nota
FROM estudiantes e
JOIN matriculas m ON e.estudiante_id = m.estudiante_id
JOIN cursos c ON m.curso_id = c.curso_id
WHERE e.nombre = 'Sofía' AND e.apellido = 'Castro';

-- 3. Total de Estudiantes por Curso
SELECT
    c.nombre_curso AS Curso,
    COUNT(m.estudiante_id) AS Total_Estudiantes
FROM cursos c
JOIN matriculas m ON c.curso_id = m.curso_id
GROUP BY c.nombre_curso
ORDER BY Total_Estudiantes DESC;

-- 4. Estudiantes Aprobados (Nota > 7.0)
SELECT DISTINCT
    CONCAT(e.nombre, ' ', e.apellido) AS Estudiante_Aprobado
FROM estudiantes e
JOIN matriculas m ON e.estudiante_id = m.estudiante_id
WHERE m.nota > 7.0
ORDER BY Estudiante_Aprobado;