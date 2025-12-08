CREATE DATABASE ventas;
USE ventas;

CREATE TABLE clientes (
    cliente_id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    telefono VARCHAR(15)
);

CREATE TABLE productos (
    producto_id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    precio DECIMAL(10, 2) NOT NULL,
    stock INT NOT NULL DEFAULT 0
);

CREATE TABLE facturas (
    factura_id INT PRIMARY KEY AUTO_INCREMENT,
    cliente_id INT NOT NULL,
    fecha DATE NOT NULL,
    total DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (cliente_id) REFERENCES clientes(cliente_id)
);

CREATE TABLE detalle_factura (
    detalle_id INT PRIMARY KEY AUTO_INCREMENT,
    factura_id INT NOT NULL,
    producto_id INT NOT NULL,
    cantidad INT NOT NULL,
    precio_unitario DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (factura_id) REFERENCES facturas(factura_id),
    FOREIGN KEY (producto_id) REFERENCES productos(producto_id)
);


INSERT INTO clientes (nombre, apellido, email, telefono) VALUES
('Juan', 'Pérez', 'juan.perez@email.com', '111-222-3333'),
('Ana', 'Gómez', 'ana.gomez@email.com', '444-555-6666'),
('Luis', 'Ramírez', 'luis.ramirez@email.com', '777-888-9999');

INSERT INTO productos (nombre, precio, stock) VALUES
('Laptop Pro', 1200.00, 15),
('Mouse Inalámbrico', 25.50, 50),
('Monitor Curvo 27"', 350.99, 10),
('Teclado Mecánico', 85.00, 20);

INSERT INTO facturas (cliente_id, fecha, total) VALUES
(1, '2025-10-01', 1225.50);

INSERT INTO facturas (cliente_id, fecha, total) VALUES
(2, '2025-10-05', 785.99);

INSERT INTO detalle_factura (factura_id, producto_id, cantidad, precio_unitario) VALUES
(1, 1, 1, 1200.00),
(1, 2, 1, 25.50);

INSERT INTO detalle_factura (factura_id, producto_id, cantidad, precio_unitario) VALUES
(2, 3, 2, 350.99),
(2, 4, 1, 85.00);


-- 1. Todas las Ventas con Nombre del Cliente
SELECT
    f.factura_id,
    CONCAT(c.nombre, ' ', c.apellido) AS Nombre_Cliente,
    f.fecha,
    f.total
FROM facturas f
JOIN clientes c ON f.cliente_id = c.cliente_id
ORDER BY f.fecha DESC;

-- 2. Detalle de la Factura ID 2
SELECT
    f.factura_id,
    p.nombre AS Producto,
    df.cantidad,
    df.precio_unitario,
    (df.cantidad * df.precio_unitario) AS Subtotal
FROM detalle_factura df
JOIN facturas f ON df.factura_id = f.factura_id
JOIN productos p ON df.producto_id = p.producto_id
WHERE f.factura_id = 2;

-- 3. Productos con Stock Bajo (menos de 20)
SELECT
    nombre,
    stock
FROM productos
WHERE stock < 20
ORDER BY stock ASC;

-- 4. Gasto Total por Cliente
SELECT
    CONCAT(c.nombre, ' ', c.apellido) AS Cliente,
    SUM(f.total) AS Gasto_Total
FROM clientes c
JOIN facturas f ON c.cliente_id = f.cliente_id
GROUP BY c.cliente_id, c.nombre, c.apellido
ORDER BY Gasto_Total DESC;