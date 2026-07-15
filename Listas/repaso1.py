# 1.
ventas=[]

ventas.append(100)
ventas.append(250)
ventas.append(300)
ventas.insert(0,150)
c = len(ventas)

print(ventas)
print(c)


# 2.
ventas = [100, 250, 100, 300, 100, 400]
print(ventas.count(100))
print(ventas.index(300))
ventas.remove(100)

print(ventas)


# 3.
semana1 = [500, 600, 700]
semana2 = [800, 900]

semana1.extend(semana2)

semana1.sort()

minimo = min(semana1)
maximo = max(semana1)
print(semana1)
print(minimo)
print(maximo)


# 4.
clientes = ["Ana", "Luis", "Pedro", "María"]

copia = clientes.copy()
copia.pop(-1)
copia.reverse()

print(clientes)
print(copia)

# 5.

ventas = [800, 1200, 500, 3000, 1500]

ventas.append(2200)
ventas.sort()

minimo = min(ventas)
maximo = max(ventas)
cantidad = len(ventas)

print(minimo)
print(maximo)
print(cantidad)


copia = ventas.copy()
baja = min(copia)
copia.remove(baja)

print(ventas)
print(copia)