"""Ejercicios: Tuplas, Listas y Diccionarios

Solución y demostración interactiva (imprime resultados al ejecutar).
"""


def ejercicio_tuplas():
    print("EJERCICIO 1: TUPLAS")
    vulnerabilidades = (
        'SQL Injection',
        'Cross-Site Scripting',
        'Buffer Overflow',
        'Denegación de Servicio',
    )

    # a) Muestra el segundo elemento (índice 1)
    segundo = vulnerabilidades[1]
    print("a) Segundo elemento:", segundo)

    # b) Muestra los dos últimos elementos
    ultimos_dos = vulnerabilidades[-2:]
    print("b) Dos últimos elementos:", ultimos_dos)

    # c) Intentar modificar un elemento (fallará: las tuplas son inmutables)
    print("c) Intento de modificar el primer elemento (debe lanzar error):")
    try:
        # Usamos exec para evitar que el comprobador estático marque error
        exec("vulnerabilidades[0] = 'Inyección SQL'")
    except TypeError as e:
        print("   Resultado: no se puede modificar una tupla (TypeError):", e)


def ejercicio_listas():
    print("\nEJERCICIO 2: LISTAS")
    puertos_abiertos = [22, 80, 443, 8080]
    print("Estado inicial:", puertos_abiertos)

    # a) Agrega el puerto 21
    puertos_abiertos.append(21)
    print("a) Después de agregar 21:", puertos_abiertos)

    # b) Elimina el puerto 8080
    if 8080 in puertos_abiertos:
        puertos_abiertos.remove(8080)
    print("b) Después de eliminar 8080 (si existía):", puertos_abiertos)

    # c) Muestra la lista ordenada de menor a mayor (sin modificar la original)
    ordenada = sorted(puertos_abiertos)
    print("c) Lista ordenada (menor a mayor):", ordenada)


def ejercicio_diccionarios():
    print("\nEJERCICIO 3: DICCIONARIOS")
    dispositivo_red = {
        'IP': '192.168.1.10',
        'Hostname': 'Firewall-Corp',
        'Estado': 'Activo',
    }

    print("Estado inicial:", dispositivo_red)

    # a) Muestra el valor de la clave 'Hostname'
    hostname = dispositivo_red.get('Hostname')
    print("a) Hostname:", hostname)

    # b) Agrega 'Ubicación'
    dispositivo_red['Ubicación'] = 'Centro de Datos'
    print("b) Después de agregar 'Ubicación':", dispositivo_red)

    # c) Cambia el valor de 'Estado' a 'Inactivo'
    dispositivo_red['Estado'] = 'Inactivo'
    print("c) Después de cambiar 'Estado' a 'Inactivo':", dispositivo_red)

    # d) Muestra todo el diccionario actualizado
    print("d) Diccionario actualizado:")
    for clave, valor in dispositivo_red.items():
        print(f"   {clave}: {valor}")


def main() -> None:
    ejercicio_tuplas()
    ejercicio_listas()
    ejercicio_diccionarios()


if __name__ == '__main__':
    main()

