# ---------------------------------------------------------
# 1. Clase Usuario
# ---------------------------------------------------------
class Usuario:
    def __init__(self, nombre, edad):
        # El método __init__ inicializa los atributos
        self.nombre = nombre
        self.edad = edad

    def mostrar_datos(self):
        print(f"--- Datos del Usuario ---")
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad} años")

# ---------------------------------------------------------
# 2. Clase Rectangulo
# ---------------------------------------------------------
class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        # Área = base * altura
        return self.base * self.altura

# ---------------------------------------------------------
# 3. Clase Coche
# ---------------------------------------------------------
class Coche:
    def __init__(self, marca, velocidad_inicial=0):
        self.marca = marca
        self.velocidad = velocidad_inicial

    def aumentar_velocidad(self, incremento):
        self.velocidad += incremento
        print(f"El coche {self.marca} aceleró. Nueva velocidad: {self.velocidad} km/h")

# ---------------------------------------------------------
# 4. Clase CuentaBancaria
# ---------------------------------------------------------
class CuentaBancaria:
    def __init__(self, titular, balance_inicial=0):
        self.titular = titular
        self.balance = balance_inicial

    def depositar(self, cantidad):
        self.balance += cantidad
        print(f"Depósito de ${cantidad} exitoso. Nuevo balance: ${self.balance}")

    def retirar(self, cantidad):
        if cantidad > self.balance:
            print("Fondos insuficientes para realizar el retiro.")
        else:
            self.balance -= cantidad
            print(f"Retiro de ${cantidad} exitoso. Nuevo balance: ${self.balance}")

# ---------------------------------------------------------
# 5. Clase Estudiante
# ---------------------------------------------------------
class Estudiante:
    def __init__(self, nombre, calificaciones):
        self.nombre = nombre
        self.calificaciones = calificaciones # Esto espera una lista de números

    def calcular_promedio(self):
        if len(self.calificaciones) == 0:
            return 0
        suma = sum(self.calificaciones)
        promedio = suma / len(self.calificaciones)
        return promedio

# =========================================================
# BLOQUE DE PRUEBA (Ejecución de las clases)
# =========================================================
if __name__ == "__main__":
    print("\n=== EJERCICIO 1: USUARIO ===")
    usuario1 = Usuario("Ana Pérez", 28)
    usuario1.mostrar_datos()

    print("\n=== EJERCICIO 2: RECTÁNGULO ===")
    rect = Rectangulo(10, 5)
    print(f"El área del rectángulo es: {rect.calcular_area()}")

    print("\n=== EJERCICIO 3: COCHE ===")
    mi_coche = Coche("Toyota", 60)
    mi_coche.aumentar_velocidad(20) # Aumenta 20 km/h

    print("\n=== EJERCICIO 4: CUENTA BANCARIA ===")
    cuenta = CuentaBancaria("Carlos Ruiz", 1000)
    cuenta.depositar(500)
    cuenta.retirar(200)
    cuenta.retirar(5000) # Prueba de fondos insuficientes

    print("\n=== EJERCICIO 5: ESTUDIANTE ===")
    notas_juan = [90, 85, 88, 92]
    estudiante1 = Estudiante("Juan Lopez", notas_juan)
    promedio = estudiante1.calcular_promedio()
    print(f"El promedio de {estudiante1.nombre} es: {promedio}")