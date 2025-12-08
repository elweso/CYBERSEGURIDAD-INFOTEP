CREATE DATABASE biblioteca;
USE biblioteca;

CREATE TABLE autores (
  
    autor_id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    nacionalidad VARCHAR(50)
);

CREATE TABLE libros (
    
    libro_id INT PRIMARY KEY AUTO_INCREMENT,
    titulo VARCHAR(255) NOT NULL,
    anio_publicacion INT,
   
    autor_id INT,
    
    FOREIGN KEY (autor_id) REFERENCES autores(autor_id)
     
      
);


INSERT INTO autores (nombre, nacionalidad) VALUES
('Gabriel García Márquez', 'Colombiano'),
('Jane Austen', 'Británica'),
('George Orwell', 'Británico'),
('Isabel Allende', 'Chilena');


INSERT INTO libros (titulo, anio_publicacion, autor_id) VALUES
('Cien años de soledad', 1967, 1), 
('El amor en los tiempos del cólera', 1985, 1),
('Orgullo y prejuicio', 1813, 2), 
('1984', 1949, 3), 
('Rebelión en la granja', 1945, 3),
('La casa de los espíritus', 1982, 4); 


SELECT * FROM autores;


SELECT titulo, anio_publicacion FROM libros;


SELECT
    l.titulo AS Titulo_del_Libro,
    a.nombre AS Nombre_del_Autor,
    l.anio_publicacion
FROM
    libros l
JOIN
    autores a ON l.autor_id = a.autor_id;


SELECT
    l.titulo
FROM
    libros l
JOIN
    autores a ON l.autor_id = a.autor_id
WHERE
    a.nombre = 'Gabriel García Márquez';


SELECT
    nombre,
    nacionalidad
FROM
    autores
WHERE
    nacionalidad = 'Británica';