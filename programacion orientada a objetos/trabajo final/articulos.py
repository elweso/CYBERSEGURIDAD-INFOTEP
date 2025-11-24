import mysql.connector


class Articulos:

    def abrir(self):
        conexion = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="12345",
            database="bd1",
            port=4306
        )
        return conexion

    def alta(self, datos):
        cone = self.abrir()
        cursor = cone.cursor()
        sql = "insert into articulos(descripcion, precio) values (%s,%s)"
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()

    def consulta(self, datos):
        cone = self.abrir()
        cursor = cone.cursor()
        sql = "select descripcion, precio from articulos where codigo=%s"
        cursor.execute(sql, datos)
        resultado = cursor.fetchall()
        cursor.close()
        cone.close()
        return resultado

    def recuperar_todos(self):
        cone = self.abrir()
        cursor = cone.cursor()
        sql = "select codigo, descripcion, precio from articulos"
        cursor.execute(sql)
        resultado = cursor.fetchall()
        cursor.close()
        cone.close()
        return resultado

    def eliminar(self, datos):
        cone = self.abrir()
        cursor = cone.cursor()
        sql = "delete from articulos where codigo=%s"
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()

    def actualizar(self, datos):
        cone = self.abrir()
        cursor = cone.cursor()
        sql = "update articulos set descripcion=%s, precio=%s where codigo=%s"
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()
