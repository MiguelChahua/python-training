ventas = [120, 150, 80, 200]

for venta in ventas:
    print(venta)


# Range() → Sirve para repetir algo cierta cantidad de veces

for i in range(5): # Empieza en 0
    print(i)

for i in range(2,8): # Empieza en 2 y termina antes del 8
    print(i)

for i in range(2,10,2): # Tercer parámetro es el salto
    print(i)


# Enumerate()

ventas = [100,150,200]

for indice, venta in enumerate(ventas):
    print(indice, venta)

# WHILE

contador = 1

while contador <=5:
    print(contador)
    contador +=1


# BREAK

for numero in range(10):

    if numero ==5:
        break # Rompe el ciclo

    print(numero)
    

for numero in range(6):

    if numero==3:
        continue # Solo omite el valor y continua

    print(numero)
    

# Por ejemplo break serviria par encontrar un cliente e imprimir si lo encontro
# continue si se quiere omitir datos nulos y seguir.