"""Ejercicios de Python: Tuplas, Listas y Diccionarios

Este script implementa las operaciones pedidas en el archivo de tareas
`listas,tuplas.diccionarios` y muestra la salida por consola.
"""

def ejercicio_tuplas():
    print("Ejercicio 1: Tuplas")
    vulnerabilidades = (
        'SQL Injection',
        'Cross-Site Scripting',
        'Buffer Overflow',
        'Denegación de Servicio'
    )

    # a) Muestra el segundo elemento
    print("a) Segundo elemento:", vulnerabilidades[1])

    # b) Muestra los dos últimos elementos
    print("b) Dos últimos elementos:", vulnerabilidades[-2:])

    # c) Intentar modificar un elemento y capturar el resultado
    try:
        vulnerabilidades[1] = 'XSS - modificado'
    except TypeError as e:
        print("c) Intento de modificación -> Error capturado:", type(e).__name__, "-", e)


def ejercicio_listas():
    print("\nEjercicio 2: Listas")
    puertos_abiertos = [22, 80, 443, 8080]
    print("Estado inicial:", puertos_abiertos)

    # a) Agrega el puerto 21
    puertos_abiertos.append(21)
    print("a) Después de agregar 21:", puertos_abiertos)

    # b) Elimina el puerto 8080
    try:
        puertos_abiertos.remove(8080)
        print("b) Después de eliminar 8080:", puertos_abiertos)
    except ValueError:
        print("b) El puerto 8080 no estaba en la lista")

    # c) Muestra la lista ordenada de menor a mayor
    lista_ordenada = sorted(puertos_abiertos)
    print("c) Lista ordenada:", lista_ordenada)


def ejercicio_diccionarios():
    print("\nEjercicio 3: Diccionarios")
    dispositivo_red = {
        'IP': '192.168.1.10',
        'Hostname': 'Firewall-Corp',
        'Estado': 'Activo'
    }

    # a) Muestra el valor de la clave 'Hostname'
    print("a) Hostname:", dispositivo_red.get('Hostname'))

    # b) Agrega 'Ubicación'
    dispositivo_red['Ubicación'] = 'Centro de Datos'
    print("b) Después de agregar 'Ubicación':", dispositivo_red)

    # c) Cambia 'Estado' a 'Inactivo'
    dispositivo_red['Estado'] = 'Inactivo'
    print("c) Después de cambiar 'Estado':", dispositivo_red)

    # d) Muestra todo el diccionario actualizado
    print("d) Diccionario actualizado:", dispositivo_red)


def main():
    ejercicio_tuplas()
    ejercicio_listas()
    ejercicio_diccionarios()


if __name__ == '__main__':
    main()
