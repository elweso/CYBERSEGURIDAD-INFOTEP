import articulos

art = articulos.Articulos()

articulos_prueba = [
    ('Laptop Dell', 800),
    ('Mouse Logitech', 25),
    ('Teclado Mecanico', 120),
    ('Monitor 24 pulgadas', 250),
    ('Auriculares Gamer', 90)
]

for desc, prec in articulos_prueba:
    try:
        art.alta((desc, prec))
        print(f'Agregado: {desc} - ${prec}')
    except Exception as e:
        print(f'Error: {e}')

print("\nAhora prueba en la aplicacion")
