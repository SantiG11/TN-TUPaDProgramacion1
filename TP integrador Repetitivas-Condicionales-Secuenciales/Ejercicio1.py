nombre = input('Ingrese su nombre: ')

while not nombre.isalpha():
    print('Error: ingrese un nombre válido, solo con letras.')
    nombre = input('Ingrese su nombre: ')

cantidad = input('Ingrese en números la cantidad de productos a comprar: ')

while not cantidad.isdigit() or int(cantidad) <= 0:
    print('Error: ingrese una cantidad válida, solo con números enteros positivos.')
    cantidad = input('Ingrese en números la cantidad de productos a comprar: ')

cantidad = int(cantidad)

total_sin_descuentos = 0
total_con_descuentos = 0
productos = ''

for producto in range(1, cantidad + 1):
    precio = input(f'Producto {producto} - Precio: ')

    while not precio.isdigit() or int(precio) <= 0:
        print('Error: ingrese un precio válido, solo con números enteros positivos.')
        precio = input(f'Producto {producto} - Precio: ')

    precio = int(precio)

    descuento = input(f'Producto {producto} - Descuento (S/N): ').lower()

    while descuento != 's' and descuento != 'n':
        print('Error: ingrese solo S o N.')
        descuento = input(f'Producto {producto} - Descuento (S/N): ').lower()

    total_sin_descuentos += precio

    if descuento == 's':
        precio_final = precio * 0.9
    else:
        precio_final = precio

    total_con_descuentos += precio_final
    productos += f'Producto {producto} - Precio: ${precio} Descuento (S/N): {descuento.upper()}\n'

ahorro = total_sin_descuentos - total_con_descuentos
promedio = round(total_con_descuentos / cantidad, 2)

print(f'Cliente: {nombre}')
print(f'Cantidad de productos: {cantidad}')
print(productos)
print(f'Total sin descuentos: ${total_sin_descuentos}')
print(f'Total con descuentos: ${total_con_descuentos:.2f}')
print(f'Ahorro: ${ahorro:.2f}')
print(f'Promedio por producto: ${promedio:.2f}')