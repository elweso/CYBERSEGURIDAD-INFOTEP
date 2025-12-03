"""
Ejercicios usando Herencia y Polimorfismo
Asignación de Programación Orientada a Objetos
"""

import math

# ============================================
# Ejercicio 1: Animal con Perro y Gato
# ============================================

class Animal:
    """Clase base Animal"""
    def __init__(self, nombre):
        self.nombre = nombre
    
    def hablar(self):
        """Método base que será sobreescrito por las clases hijas"""
        return "El animal hace un sonido"


class Perro(Animal):
    """Clase Perro que hereda de Animal"""
    def __init__(self, nombre, raza):
        super().__init__(nombre)
        self.raza = raza
    
    def hablar(self):
        """Sobreescribe el método hablar()"""
        return f"{self.nombre} dice: ¡Guau guau!"


class Gato(Animal):
    """Clase Gato que hereda de Animal"""
    def __init__(self, nombre, color):
        super().__init__(nombre)
        self.color = color
    
    def hablar(self):
        """Sobreescribe el método hablar()"""
        return f"{self.nombre} dice: ¡Miau miau!"


# ============================================
# Ejercicio 2: Empleado con Gerente y Técnico
# ============================================

class Empleado:
    """Clase base Empleado"""
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario
    
    def calcular_bono(self):
        """Método base para calcular bono"""
        return self.salario * 0.05


class Gerente(Empleado):
    """Clase Gerente que hereda de Empleado"""
    def __init__(self, nombre, salario, departamento):
        super().__init__(nombre, salario)
        self.departamento = departamento
    
    def calcular_bono(self):
        """Gerente recibe 20% de bono"""
        return self.salario * 0.20


class Tecnico(Empleado):
    """Clase Técnico que hereda de Empleado"""
    def __init__(self, nombre, salario, especialidad):
        super().__init__(nombre, salario)
        self.especialidad = especialidad
    
    def calcular_bono(self):
        """Técnico recibe 10% de bono"""
        return self.salario * 0.10


# ============================================
# Ejercicio 3: Figura con Círculo y Cuadrado
# ============================================

class Figura:
    """Clase base Figura"""
    def area(self):
        """Método base para calcular área"""
        return 0


class Circulo(Figura):
    """Clase Círculo que hereda de Figura"""
    def __init__(self, radio):
        self.radio = radio
    
    def area(self):
        """Calcula el área del círculo: π * r²"""
        return math.pi * (self.radio ** 2)


class Cuadrado(Figura):
    """Clase Cuadrado que hereda de Figura"""
    def __init__(self, lado):
        self.lado = lado
    
    def area(self):
        """Calcula el área del cuadrado: lado²"""
        return self.lado ** 2


# ============================================
# Ejercicio 4: Vehículo con Carro y Bicicleta
# ============================================

class Vehiculo:
    """Clase base Vehículo"""
    def __init__(self, marca):
        self.marca = marca
    
    def mover(self):
        """Método base para mover el vehículo"""
        return "El vehículo se está moviendo"


class Carro(Vehiculo):
    """Clase Carro que hereda de Vehículo"""
    def __init__(self, marca, modelo):
        super().__init__(marca)
        self.modelo = modelo
    
    def mover(self):
        """Sobreescribe el método mover()"""
        return f"El carro {self.marca} {self.modelo} se mueve con motor a gasolina"


class Bicicleta(Vehiculo):
    """Clase Bicicleta que hereda de Vehículo"""
    def __init__(self, marca, tipo):
        super().__init__(marca)
        self.tipo = tipo
    
    def mover(self):
        """Sobreescribe el método mover()"""
        return f"La bicicleta {self.marca} tipo {self.tipo} se mueve pedaleando"


# ============================================
# Ejercicio 5: Dispositivo con Laptop y Teléfono
# ============================================

class Dispositivo:
    """Clase base Dispositivo"""
    def __init__(self, marca):
        self.marca = marca
        self.encendido = False
    
    def encender(self):
        """Método base para encender el dispositivo"""
        self.encendido = True
        return "Dispositivo encendido"


class Laptop(Dispositivo):
    """Clase Laptop que hereda de Dispositivo"""
    def __init__(self, marca, procesador):
        super().__init__(marca)
        self.procesador = procesador
    
    def encender(self):
        """Sobreescribe el método encender()"""
        self.encendido = True
        return f"Laptop {self.marca} iniciando sistema operativo con procesador {self.procesador}..."


class Telefono(Dispositivo):
    """Clase Teléfono que hereda de Dispositivo"""
    def __init__(self, marca, sistema_operativo):
        super().__init__(marca)
        self.sistema_operativo = sistema_operativo
    
    def encender(self):
        """Sobreescribe el método encender()"""
        self.encendido = True
        return f"Teléfono {self.marca} encendiendo {self.sistema_operativo}..."


# ============================================
# DEMOSTRACIÓN DE USO
# ============================================

def main():
    print("=" * 60)
    print("EJERCICIOS DE HERENCIA Y POLIMORFISMO")
    print("=" * 60)
    
    # Ejercicio 1: Animales
    print("\n--- Ejercicio 1: Animales ---")
    perro = Perro("Max", "Labrador")
    gato = Gato("Luna", "Blanco")
    
    print(perro.hablar())
    print(gato.hablar())
    
    # Ejercicio 2: Empleados
    print("\n--- Ejercicio 2: Empleados ---")
    gerente = Gerente("Carlos", 5000, "Ventas")
    tecnico = Tecnico("Ana", 3000, "Redes")
    
    print(f"{gerente.nombre} - Salario: ${gerente.salario} - Bono: ${gerente.calcular_bono():.2f}")
    print(f"{tecnico.nombre} - Salario: ${tecnico.salario} - Bono: ${tecnico.calcular_bono():.2f}")
    
    # Ejercicio 3: Figuras
    print("\n--- Ejercicio 3: Figuras ---")
    circulo = Circulo(5)
    cuadrado = Cuadrado(4)
    
    print(f"Área del círculo (radio {circulo.radio}): {circulo.area():.2f}")
    print(f"Área del cuadrado (lado {cuadrado.lado}): {cuadrado.area():.2f}")
    
    # Ejercicio 4: Vehículos
    print("\n--- Ejercicio 4: Vehículos ---")
    carro = Carro("Toyota", "Corolla")
    bicicleta = Bicicleta("Trek", "Montaña")
    
    print(carro.mover())
    print(bicicleta.mover())
    
    # Ejercicio 5: Dispositivos
    print("\n--- Ejercicio 5: Dispositivos ---")
    laptop = Laptop("Dell", "Intel i7")
    telefono = Telefono("Samsung", "Android")
    
    print(laptop.encender())
    print(telefono.encender())
    
    # Demostración de polimorfismo
    print("\n--- Demostración de Polimorfismo ---")
    animales = [perro, gato]
    for animal in animales:
        print(animal.hablar())
    
    empleados = [gerente, tecnico]
    for empleado in empleados:
        print(f"{empleado.nombre}: Bono = ${empleado.calcular_bono():.2f}")
    
    figuras = [circulo, cuadrado]
    for figura in figuras:
        print(f"Área: {figura.area():.2f}")
    
    print("\n" + "=" * 60)


if __name__ == "__main__":
    main()