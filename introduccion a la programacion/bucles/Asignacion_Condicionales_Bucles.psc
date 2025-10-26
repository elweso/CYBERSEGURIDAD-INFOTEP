Algoritmo MayorEdad
	Escribir 'Ingresa tu edad: '
	Leer edad
	Si edad>=18 Entonces
		Escribir 'Eres mayor de edad'
	SiNo
		Escribir 'Eres menor de edad'
	FinSi
FinAlgoritmo

Algoritmo numerosq
    Escribir "Ingresa un número: "
    Leer num
    Si num > 0 Entonces
        Escribir "El número es positivo"
    SiNo
        Si num < 0 Entonces
            Escribir "El número es negativo"
        SiNo
            Escribir "El número es cero"
        FinSi
    FinSi
FinAlgoritmo


Algoritmo ParImpar
    Escribir "Ingresa un número: "
    Leer num
    Si num MOD 2 = 0 Entonces
        Escribir "El número es par"
    SiNo
        Escribir "El número es impar"
    FinSi
FinAlgoritmo


Algoritmo  NotaFinal
    Escribir "Ingresa tu nota (0-100): "
    Leer nota
    Si nota >= 90 Entonces
        Escribir "Aprobado con A"
    SiNo
        Si nota >= 70 Entonces
            Escribir "Aprobado"
        SiNo
            Escribir "Reprobado"
        FinSi
    FinSi
FinAlgoritmo


Algoritmo  DescuentoCompra
    Escribir "Ingresa el monto de la compra: "
    Leer monto
    Si monto > 500 Entonces
        descuento <- monto * 0.10
        total <- monto - descuento
        Escribir "Tienes un 10% de descuento. Total a pagar: ", total
    SiNo
        Escribir "No aplica descuento. Total a pagar: ", monto
    FinSi
FinAlgoritmo




	
	Algoritmo  Numeros1a10
		num <- 1
		Mientras num <= 10 Hacer
			Escribir num
			num <- num + 1
		FinMientras
FinAlgoritmo


Algoritmo  SumaHastaCero
    suma <- 0
    Repetir
        Escribir "Ingresa un número (0 para terminar): "
        Leer num
        suma <- suma + num
    Mientras Que num <> 0
    Escribir "La suma total es: ", suma
FinAlgoritmo


Algoritmo AdivinaNumero
    secreto <- 7
    Repetir
        Escribir "Adivina el número secreto (1-10): "
        Leer intento
        Si intento <> secreto Entonces
            Escribir "Incorrecto, intenta de nuevo."
        FinSi
    Mientras Que intento <> secreto
    Escribir "¡Correcto! El número secreto es 7."
FinAlgoritmo


Algoritmo  ValidarContrasena
    Repetir
        Escribir "Introduce la contraseña: "
        Leer clave
    Mientras Que clave <> "1234"
    Escribir "Acceso concedido."
FinAlgoritmo


Algoritmo  ContadorRegresivo
    Escribir "Ingresa un número para iniciar el conteo regresivo: "
    Leer num
    Mientras num >= 1 Hacer
        Escribir num
        num <- num - 1
    FinMientras
    Escribir "¡Despegue!"
FinAlgoritmo




	
	Algoritmo  TablaMultiplicar
		Escribir "Ingresa un número: "
		Leer num
		Para i <- 1 Hasta 10 Con Paso 1 Hacer
			Escribir num, " x ", i, " = ", num * i
		FinPara
FinAlgoritmo


Algoritmo SumaDiezNumeros
    suma <- 0
    Para i <- 1 Hasta 10 Con Paso 1 Hacer
        Escribir "Ingresa el número ", i, ": "
        Leer num
        suma <- suma + num
    FinPara
    Escribir "La suma total es: ", suma
FinAlgoritmo


Algoritmo Factorial
   
    Escribir "Ingresa un número: "
    Leer num
	
    factorial <- 1
	
    Para i <- 1 Hasta num Con Paso 1 Hacer
        factorial <- factorial * i
    FinPara
	

    Escribir "El factorial de ", num, " es: ", factorial
FinAlgoritmo


Proceso NumerosPares
    Para i <- 1 Hasta 50 Con Paso 1 Hacer
        Si i MOD 2 = 0 Entonces
            Escribir i
        FinSi
    FinPara
FinProceso

Proceso PromedioNotas
    suma <- 0
    Para i <- 1 Hasta 5 Con Paso 1 Hacer
        Escribir "Ingresa la nota ", i, ": "
        Leer nota
        suma <- suma + nota
    FinPara
    promedio <- suma / 5
    Escribir "La suma total es: ", suma
    Escribir "El promedio final es: ", promedio
FinProceso
