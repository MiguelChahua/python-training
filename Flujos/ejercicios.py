# 1 
ventas = [1200, 850, -150, 980, 0, 450, -20, 1500]

for venta in ventas:
    if venta < 0:
        continue
    elif venta == 0:
        break
    else:
        print(venta)
    

# 2

notas = [18, 11, 15, 9, 20, 13, 17, 8, 16]
ce = 0
ca = 0
cr = 0
cd = 0


for nota in notas:
    if nota >= 18:
        ce += 1
    elif nota >= 14:
        ca += 1
    elif nota >= 11:
        cr += 1
    else:
        cd += 1

print(f'Cantidad de excelente: {ce}')
print(f'Cantidad de aprobados: {ca}')
print(f'Cantidad de recuperación: {cr}')
print(f'Cantidad de desaprobados: {cd}')


# 3.

# usuarios = []

# while True:

#     nombre = input("Ingrese un nombre: ").strip()

#     if nombre == "":
#         print("El nombre no puede estar vacío.\n")
#         continue

#     if nombre.lower() == "salir":
#         break

#     usuarios.append(nombre)

# print("\nUsuarios registrados")

# for indice, usuario in enumerate(usuarios, start=1):
#     print(f"{indice} - {usuario}")


# 4.

inventario = {
    "Laptop": 12,
    "Mouse": 0,
    "Teclado": 8,
    "Monitor": 15,
    "USB": 2,
    "Webcam": 0
}

agotados = []
stock_bajo = []
stock_suficiente = []

print('======================')
for producto, stock in inventario.items():
    if stock == 0:
        agotados.append(producto)
    elif stock < 5:
        stock_bajo.append(producto)
    else:
        stock_suficiente.append(producto)

print(f'''
      Productos agotados: {', '.join(agotados)}; Cantidad: {len(agotados)}
      Productos con stock bajo: {', '.join(stock_bajo)}; Cantidad: {len(stock_bajo)}
      Productos con stock suficiente: {', '.join(stock_suficiente)}; Cantidad: {len(stock_suficiente)}
    ''')

# 5.

temperaturas = [35, 38, 40, 41, 39, None, 37, 45, 46, 44, None, 42, 39, 41]
normal = []
advertencia = []
alta = []
detector = False

for temperatura in temperaturas:
    if temperatura == None:
        continue
    if temperatura > 45:
        print('Se detectó una temperatura crítica')
        detector = True
        break
    
    if temperatura < 38:
        normal.append(temperatura)
    elif  temperatura <= 42:
        advertencia.append(temperatura)
    else:
        alta.append(temperatura)
    
suma_total = sum(normal) + sum(advertencia) + sum(alta)
cantidad_total = len(normal) + len(advertencia) + len(alta)

print(f'''
      ====================================================================================
      Cantidad de temperaturas normales: {len(normal)}
      Cantidad de advertencias: {len(advertencia)}
      Cantidad de temperaturas altas: {len(alta)}
      Promedio de las temperaturas válidas procesadas: {round(suma_total/cantidad_total,2)}
    ''')

if detector:
    print(f'¿Se detectó un temperatura crítica?: {detector}')