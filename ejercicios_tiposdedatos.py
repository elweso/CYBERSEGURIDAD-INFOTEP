#Pide al usuario un número entero y muestra su doble.
numero = int(input("Introduce un número entero: "))
resultado = numero * 2
print("El doble de", numero, "es", resultado)


#Solicita dos números enteros y muestra la suma.
num1 = int(input("Introduce el primer número entero: "))
num2 = int(input("Introduce el segundo número entero: "))
suma = num1 + num2
print("La suma de", num1, "y", num2, "es", suma)


#Ingresa un número real (decimal) y muestra su mitad.
numero_real = float(input("Introduce un número real: "))
mitad = numero_real / 2
print("La mitad de", numero_real, "es", mitad)

#Solicita dos números reales y muestra su promedio.

numero1 = float(input("Introduce el primer número real: "))
numero2 = float(input("Introduce el segundo número real: "))   
promedio = (numero1 + numero2) / 2
print("El promedio de", numero1, "y", numero2, "es", promedio)


# Pide al usuario que escriba su edad y muestra Verdadero si es mayor de edad (18+), Falso en caso contrario.

edad = int(input("Escribe tu edad: "))
mayor_de_edad = edad >= 18
print("¿Eres mayor de edad?", mayor_de_edad)



# Pregunta al usuario si tiene internet en casa (1 = Sí, 0 = No) y guarda la respuesta como lógico.

tiene_internet = bool(int(input("¿Tienes internet en casa? (1 = Sí, 0 = No): ")))
print("¿Tienes internet en casa?", tiene_internet)


# Pide al usuario que escriba una letra y muéstrala en pantalla.

letra = input("Escribe una letra: ")
print("La letra que escribiste es:", letra)


# Ingresa un carácter y muestra el mensaje 'Correcto' si es la letra 'A'.

caracter= input("Escribe un carácter: ")
if caracter.upper() == 'A':
    print("Correcto")


# Pide al usuario que escriba su nombre y muéstralo con un saludo.
nombre = input("Escribe tu nombre: ")
print("Hola,", nombre + "!")


# Solicita una palabra y muestra cuántos caracteres tiene.
palabra = input("Escribe una palabra: ")
longitud = len(palabra)
print("La palabra", palabra, "tiene", longitud, "caracteres.")

