# Ejercicio 1: Información de un cliente
# Debes:
# Mostrar el nombre.
# Mostrar la ciudad usando índices.
# Recorrer la tupla con un for.
# Mostrar cada dato en una línea.

cliente = ("Miguel", 22, "Lima")

print(cliente[0])
print(cliente[2])

for x in cliente:
    print(x)


# Ejercicio 2: Análisis de ventas repetidas
# Debes:
# Contar cuántas veces aparece 100.
# Encontrar la posición de 300.
# Mostrar los resultados con mensajes descriptivos.

ventas = (100, 250, 100, 300, 100, 400)

print(f'Veces que aparece 100: {ventas.count(100)}')
print(f'Posicion de 300: {ventas.index(300)}')


# Ejercicio 3: Datos de un producto
# Debes:
# Usar desempaquetado para guardar:

producto = ("Laptop Lenovo", 2500, 15)

nombre, precio, stock = producto

print(
    f'''
    Producto: {nombre}
    Precio: {precio}
    Stock: {stock}
    '''
)


# Ejercicio 4: Función de estadísticas

def resumen_ventas():
    return 150, 25000

c, i = resumen_ventas()

print(
    f'''
    Cantidad de ventas: {c}
    Ingreso total: {i}
    '''
)

# Ejercicio 5

def info_vendedor():
    return "Juan Pérez", 45, 18500

nombre, ventas, monto = info_vendedor()

print(
    f'''
    ===== REPORTE DE VENDEDOR =====
    Nombre: {nombre}
    Ventas realizadas: {ventas}
    Monto vendido: S/. {monto}
    '''
)


if monto>15000:
    print('Superó la meta')
else:
    print('Por debajo de la meta')