# Ejercicio 1

# Compresion de listas
#ventas_validas = [venta for venta in ventas if venta != 0]


ventas = [1200, 850, 980, 0, 1500, 2300, 450]

a = 0
b = 0
acum = 0
validacion = False
dia_vta_mx = max(ventas)
dia = 0

for i , venta in enumerate(ventas):
    if venta < 1000:
        a += 1
        
    if venta != 0:
        b += 1
        acum += venta

    if venta == 0:
        validacion = True
    
    if venta == dia_vta_mx:
        dia = i+1
    
    
    
prom = acum/b


print(f'''
    Venta Total: {sum(ventas)}
    Venta Promedio: {prom}
    Venta mas alta: {dia_vta_mx}, dia {dia}
    Ventas inferiores a 1000: {a}
    ''')

if validacion:
    print('Hubo problemas en la operación')