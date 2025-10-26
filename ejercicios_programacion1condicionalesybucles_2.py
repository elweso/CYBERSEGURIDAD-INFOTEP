#Ejercicios con Condicionales

#1. Pide la edad al usuario. Si es mayor o igual a 18 muestra 'Eres mayor de edad', sino 'Eres menor de edad'.
edad = int(input("escribe ru dad"))
if edad >= 18:
    print ("eres mayor de edad")
else:
    print ("eres menor de edad")


#2. Solicita un número y determina si es positivo, negativo o cero.
numero = float(input("escribe un numero"))
if numero > 0:
    print ("el numero es positivo")
elif numero < 0:
    print ("el numero es negativo")
else:
    print ("el numero es cero")



#3. Pide un número e indica si es par o impar.
numero = int(input("escribe un numero"))
if numero % 2 == 0:
    print ("el numero es par")
else:
    print ("el numero es impar")    


#4. Introduce una nota (0-100). Muestra 'Aprobado con A' si es >=90, 'Aprobado' si es >=70 y 'Reprobado' en caso contrario.
nota = int(input("escribe una nota del 0 al 100"))
if nota >= 90:
    print ("Aprobado con A")
elif nota >= 70:
    print ("Aprobado")
else:
    print ("Reprobado")
    



#5. Ingresa el monto de una compra. Si es mayor a 500 aplica un 10% de descuento, sino paga precio normal. 
monto = float(input("Ingresa el monto de la compra: "))
if monto > 500:
    descuento = monto * 0.1
    print ("El monto final con descuento es:", monto - descuento)
else:
    print ("El monto a pagar es:", monto)




#Ejercicios con Bucle I

#1. Muestra los números del 1 al 10 usando mientras.
numero = 1
while numero <= 101:
    print (numero)
    numero += 1

#2. Pide números al usuario y suma todos hasta que escriba 0.
suma = 0
while True:
    num = int(input("Escribe un número (0 para terminar): "))
    if num == 0:
        break
    suma += num
print ("La suma total es:", suma)

#3. Adivina el número secreto (ejemplo: 7).
numero_secreto = 7
while True:
    intento = int(input("Adivina el número secreto: "))
    if intento == numero_secreto:
        print ("¡Correcto!")
        break
    else:
        print ("Intenta de nuevo.")

#4. Valida una contraseña. Mientras no sea '1234', vuelve a pedirla.
contrasena = ""
while contrasena != "1234":
    contrasena = input("Introduce la contraseña: ")
print ("Contraseña correcta.")  

#5. Crea un contador regresivo desde un número dado hasta 1.
numero = int(input("Introduce un número para el contador regresivo: "))
while numero > 0:
    print (numero)
    numero -= 1


#Ejercicios con Bucles  II

#1. Muestra la tabla de multiplicar de un número ingresado por el usuario.
numero = int(input("Introduce un número para ver su tabla de multiplicar: "))
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")



#2. Pide 10 números y calcula la suma total.
suma = 0
for _ in range(10):
    num = int(input("Introduce un número: "))
    suma += num
print("La suma total es:", suma)
    


#3. Calcula el factorial de un número.
numero = int(input("Introduce un número para calcular su factorial: "))
factorial = 1
for i in range(1, numero + 1):
    factorial *= i
print("El factorial de", numero, "es:", factorial)

#4. Muestra todos los números pares entre 1 y 50.
print("Números pares entre 1 y 50:")
for i in range(2, 51, 2):
    print(i)

#5. Pide 5 notas, calcula la suma y el promedio final.
suma = 0
for _ in range(5):
    nota = float(input("Introduce una nota: "))
    suma += nota
promedio = suma / 5
print("La suma es:", suma)
print("El promedio es:", promedio)
print("La palabra tiene", len(palabra), "caracteres.")

