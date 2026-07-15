numeros = {1, 2, 2, 3, 4, 4}    # Conjunto se declara con llaves.

print(numeros)  # Declara valores únicos aún si se agregan nuevos.


clientes = [
    "Juan",
    "Ana",
    "Juan",
    "Pedro",
    "Ana"
]

clientes_unicos = set(clientes) # Convierte la lista a conjunto

print(clientes_unicos) # Muestra solo los unicos: {'Ana', 'Pedro', 'Juan'}

# Declaracion de conjunto vacío:
conjunto_vacio = {}     # Forma incorrecta (esto declara un diccionario)
conjunto_vacio = set()  # Forma correcta


# Los conjuntos no permiten elementos mutables
# datos = {[1,2], [3,4]}  # Sale error al tratar de imprimir
datos = {(1,2), (3,4)}
print(datos)


# Para leer los elementos debes recorrerlos
frutas = {'Manzana', 'Pera', 'Uva'}

for fruta in frutas:
    print(fruta) # ¿Que pasa si quiero acceder a cada una?

print('Pera' in frutas) # Para saber si existe un valor, devuelve True
print('Mango' in frutas) # Para saber si existe un valor, devuelve False


frutas.add('Naranja')   # Agrega elementos
print(frutas)

frutas.update(("Kiwi", "Mango")) # Agrega varios elementos, incluso puede ser otro conjunto
print(frutas)

frutas.remove('Pera')   # Elimina un elemento
print(frutas)

# frutas.remove('Plátano')    # Si aliminas un elemento que no existe, te da ERROR.
frutas.discard('Plátano')     # Con discard hace lo mismo pero no genera ERROR.
print(frutas)

frutas.pop()    # Elimina un elemento al azar
print(frutas)

copia_frutas = frutas.copy()    # Crea una copia

copia_frutas.clear() # Limpia el conjuto
print(copia_frutas)  # Resultado: set()

del copia_frutas     # Elimina completamente
# print(copia_frutas)  Sale Error

print(len(frutas))