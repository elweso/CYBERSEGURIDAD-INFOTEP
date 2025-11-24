import mysql.connector

try:
    print("1. Conectando a BD...")
    conexion = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="12345",
        database="bd1",
        port=4306
    )
    print("2. Conexión exitosa")
    
    cursor = conexion.cursor()
    print("3. Probando INSERT...")
    
    sql = "insert into articulos(descripcion, precio) values (%s,%s)"
    datos = ("Laptop HP", 1500)
    cursor.execute(sql, datos)
    conexion.commit()
    
    print("4. INSERT exitoso")
    
    print("\n5. Verificando datos...")
    cursor.execute("SELECT * FROM articulos")
    resultados = cursor.fetchall()
    for fila in resultados:
        print(f"   Código: {fila[0]}, Descripción: {fila[1]}, Precio: {fila[2]}")
    
    cursor.close()
    conexion.close()
    print("\n¡TODO FUNCIONA CORRECTAMENTE!")
    
except Exception as e:
    print(f"ERROR: {e}")
    import traceback
    traceback.print_exc()
