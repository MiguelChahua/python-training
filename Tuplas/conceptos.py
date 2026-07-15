numeros = (10,40,60,30,40,50,40)    # Declaracion, se hace con parentesis, son inmutables

print(numeros[0]) # 10              # Acceso a elementos de una tupla
print(numeros[4]) # 40

cantidad = numeros.count(40)        # Cuenta veces que aparece un elemento
print(cantidad) # 3

indice_de_60 = numeros.index(60)    # Devueve indice de un elemento
print(indice_de_60) # 2

alumno = ('Fernando', 20, 1.75, 'Ingeniero', False)

print(
    f'''
    Nombre: {alumno[0]}
    Edad: {alumno[1]}
    Altura: {alumno[2]}
    Profesión: {alumno[3]}
    ¿Casado?: {alumno[4]}
    '''    
)

for dato in alumno:
    print(dato)

nombre, edad, altura, profesion, casado = alumno
print(nombre)
print(edad)
print(altura)
print(profesion)
print(casado)

# En una función:

# Cuando escribes varios valores separados por comas en el return, Python los empaqueta automáticamente en una tupla:

def estadisticas():
    return 100, 250

resultado = estadisticas()

print(resultado)        # (100, 250)
print(type(resultado))  # <class 'tuple'>

# Podemos usar desempaquetado aqui:
cantidad_ventas, ingresos = estadisticas()

print(f'Cantidad de ventas : {cantidad_ventas}')
print(f'Ingresos : {ingresos}')

# Convertir listas a tuplas
lista = ['pan', 'mayonesa', 'apio', 'huevo']
tupla = tuple(lista)
print(f'Lista transformada: {tupla}')
print(type(tupla))