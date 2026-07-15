
# Ejercicio 1

clientes = [
    "Ana",
    "Luis",
    "Pedro",
    "Ana",
    "Carlos",
    "Luis",
    "Miguel",
    "Pedro",
    "Ana"
]

clientes_unicos = set(clientes)
cantidad_cu = len(clientes_unicos)

print(clientes_unicos)
print(cantidad_cu)
print('Miguel' in clientes_unicos)
print('José' not in clientes_unicos)
clientes_unicos.add('Maria')
print(clientes_unicos)

# Ejercicio 2

sucursal_a = {
    "Laptop",
    "Mouse",
    "Teclado",
    "Monitor",
    "Webcam"
}

sucursal_b = {
    "Mouse",
    "Monitor",
    "Impresora",
    "Laptop",
    "USB"
}

print(sucursal_a | sucursal_b)
print(sucursal_a & sucursal_b)
print(sucursal_a - sucursal_b)
print(sucursal_b - sucursal_a)
print(sucursal_a ^ sucursal_b)


# Ejercicio 3

ciudades = [
    "Lima",
    "Cusco",
    "Arequipa",
    "Lima",
    "Piura",
    "Cusco",
    "Tacna",
    "Lima"
]

conj_ciu = set(ciudades)
conj_ciu.update(['Ica','Puno'])
conj_ciu.remove('Tacna')
conj_ciu.discard('Tumbes')
copia = conj_ciu.copy()
copia.clear()
print(conj_ciu)
print(copia)


# Ejercicio 4

registrados = {'Ana', 'Pedro', 'Luis', 'Miguel', 'Carlos', 'Lucía'}
compraron = {'Pedro', 'Miguel', 'Lucía'}

print(compraron.issubset(registrados))
print(registrados.issuperset(compraron))
print(len(registrados - compraron) > 0)
print(len(compraron - registrados) > 0)
print(not registrados.isdisjoint(compraron))

# Ejercicio 5

sistema_rrhh = {"E001","E002","E003","E004","E005","E006"}
sistema_biometrico = {"E003","E004","E005","E007","E008"}

a = sistema_rrhh | sistema_biometrico
b = sistema_rrhh & sistema_biometrico
c = sistema_rrhh - sistema_biometrico
d = sistema_biometrico - sistema_rrhh
e = sistema_rrhh ^ sistema_biometrico
f = sistema_biometrico.issubset(sistema_rrhh)
g = sistema_rrhh.issuperset(sistema_biometrico)


print(f'''
      
    ======== REPORTE ========
    Total de empleados distintos registrados entre ambos sistemas: {a}
    Empleados presentes en ambos sistemas: {b}
    Empleados que aparecen solo en RRHH: {c}
    Empleados que aparecen solo en el biométrico: {d}
    Empleados que aparecen únicamente en uno de los sistemas: {e}
    ¿Todos los empleados del biométrico están registrados en RRHH?: {f}
    ¿RRHH contiene completamente al biométrico?: {g}

    ''')