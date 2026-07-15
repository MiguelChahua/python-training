# Ejercicio 1

# tareas = ["estudiar", "comprar comida", "hacer ejercicio"]

# tareas.append('leer')

# nuevas_tareas = ['cocinar', 'ordenar cuarto']
# tareas.extend(nuevas_tareas)

# tareas.remove('comprar comida')

# print(tareas)
# print(len(tareas))


# Ejercicio 2

# notas = [14, 18, 12, 20, 15, 18, 10]

# print(len(notas))
# print(sum(notas)/len(notas))
# print(max(notas))
# print(min(notas))
# print(notas.count(18))
# notas.sort()
# print(notas)

# Ejercicio 3 

productos = ["Laptop", "Mouse", "Teclado", "Mouse", "Monitor"]

copia_inventario = productos.copy()
copia_inventario.append('Audífonos')
copia_inventario.remove('Mouse')

print(productos.count('Mouse'))
print(productos.index('Monitor'))

productos.reverse()

print(f'Inventario original: {productos}')
print(f'Inventario modificado: {copia_inventario}')