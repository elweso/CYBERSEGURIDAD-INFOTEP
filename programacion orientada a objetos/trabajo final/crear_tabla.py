import mysql.connector

try:
    conexion = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="12345",
        database="bd1",
        port=4306
    )
    cursor = conexion.cursor()

    # Crear tabla si no existe
    sql = """
    CREATE TABLE IF NOT EXISTS articulos (
        codigo INT AUTO_INCREMENT PRIMARY KEY,
        descripcion VARCHAR(100) NOT NULL,
        precio DECIMAL(10, 2) NOT NULL
    )
    """
    cursor.execute(sql)
    conexion.commit()
    print("✓ Tabla 'articulos' verificada/creada exitosamente")

    cursor.close()
    conexion.close()

except Exception as e:
    print(f"✗ Error: {e}")
