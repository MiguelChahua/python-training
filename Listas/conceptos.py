frutas = ['manzana', 'plátano', 'uva']  # Declaracion de lista
print(frutas)

frutas.append('mandarina')              # Agregar uno nuevo a la lista
print(frutas)

mas_frutas = ['naranja', 'granadilla']
frutas.extend(mas_frutas)               # Agrega elementos a partir de un iterable
print(frutas)

frutas.insert(2,'insertado')            # Inserta un valor a una posicion especifica
print(frutas)

frutas.remove('manzana')                # Remueve un valor especifico
print(frutas)

frutas.pop(1)                           # Elimina un valor por su posicion
print(frutas)

copia_temporal = frutas.copy()          # Crea una copia de la lista, para trabajar sin modificar la original

copia_temporal.clear()                  # Limpia la lista completa → []
print(copia_temporal)                   # []

posic_naranja= frutas.index('naranja')  # Devuelva la posicion de un elemento
print(posic_naranja)

cantidad = frutas.count('uva')          # Cuenta la cantidad de veces que aparece un elemento
print(cantidad)

frutas.sort()                           # Ordena la lista numero, alfabeto.
print(frutas)

frutas.reverse()                        # Revierte el orden de la lista asi como está
print(frutas)

# sort(), count(), copy() y remove() son métodos que verás mucho cuando hagas limpieza y transformación de datos antes de pasar a pandas.


# Lista de ventas
ventas = [100, 250, 300, 150, 200]

cantidad = len(ventas)      # 1. len() → cantidad de elementos

total = sum(ventas)         # 2. sum() → suma todos los valores

venta_minima = min(ventas)  # 3. min() → obtiene el valor más pequeño

venta_maxima = max(ventas)  # 4. max() → obtiene el valor más grande

print(cantidad)
print(total)
print(venta_minima)
print(venta_maxima)