
# 1.

edades = [15, 22, 67, 35, 12, 18, 59, 74]
menores = []
adultos = []
adt_mayores = []

def clasificacion (edades):
    
    for edad in edades:
        if edad < 18:
            menores.append(edad)
        elif edad < 60:
            adultos.append(edad)
        else:
            adt_mayores.append(edad)
        
    print(f'''
          
          Menores de edad: {menores} | Cantidad = {len(menores)}
          Adultos: {adultos} | Cantidad = {len(adultos)}
          Adultos mayores: {adt_mayores} | Cantidad = {len(adt_mayores)}
    
          ''')
    
clasificacion(edades)


# 2. Registro de ventas

def registrar_ventas():

    ventas = []

    while True:

        dato = input("Ingrese una venta (o 'fin'): ")

        if dato.lower() == "fin":
            break

        try:
            venta = float(dato)

            if venta < 0:
                print("La venta no puede ser negativa.")
                continue

            ventas.append(venta)

        except ValueError:
            print("Dato inválido.")

    return ventas


def mostrar_resumen(ventas):

    if not ventas:
        print("No se registraron ventas.")
        return

    print("\nResumen")
    print(f"Cantidad: {len(ventas)}")
    print(f"Total: {sum(ventas)}")
    print(f"Promedio: {sum(ventas)/len(ventas):.2f}")
    print(f"Mayor venta: {max(ventas)}")
    print(f"Menor venta: {min(ventas)}")


ventas = registrar_ventas()

mostrar_resumen(ventas)
        
# 3. Limpieza de datos

datos = ["120", "85", "A12", "300", "", "95", "-20", "250", "XYZ", "180"]

def limpiar_datos(datos):
    
    lista = []
    
    for dato in datos:
        if dato.isdigit():
            lista.append(int(dato))
    
    return lista

validos = limpiar_datos(datos)
rechazados = len(datos) - len(validos)
promedio = sum(validos)/len(validos)
maximo = max(validos)
minimo = min(validos)

print(f'''
      
    La lista de valores válidos: {validos}
    La cantidad de registros descartados: {rechazados}
    El promedio de los valores válidos: {promedio}
    El valor máximo: {maximo}
    El valor mínimo: {minimo}
      
    ''')

########################## ¿OTRA SOLUCIÓN? ##########################

# def limpiar_datos(datos):

#     valores_validos = []
#     descartados = 0

#     for dato in datos:

#         try:
#             numero = int(dato)

#             if numero < 0:
#                 descartados += 1
#                 continue

#             valores_validos.append(numero)

#         except ValueError:
#             descartados += 1

#     return valores_validos, descartados


# def mostrar_resultados(valores, descartados):

#     print("Valores válidos:", valores)
#     print("Descartados:", descartados)
#     print("Promedio:", sum(valores)/len(valores))
#     print("Máximo:", max(valores))
#     print("Mínimo:", min(valores))


# datos = ["120", "85", "A12", "300", "", "95", "-20", "250", "XYZ", "180"]

# valores, descartados = limpiar_datos(datos)

# mostrar_resultados(valores, descartados)



############################

# 4. Análisis de productos

inventario = {
    "Laptop": 8,
    "Mouse": 0,
    "Monitor": 12,
    "Teclado": 4,
    "USB": 25,
    "Webcam": 1,
    "Impresora": 6
}


def generar_reporte (inventario):
    
    agotado = []
    bajo = []
    suficiente = []
    
    for producto, cantidad in inventario.items():
        
        if cantidad == 0:
            agotado.append(producto)
        elif cantidad < 5:
            bajo.append(producto)
        else:
            suficiente.append(producto)

    print(f'''
        
        ******** Reporte de Inventario ********
        
        Productos sin stock → {agotado}; Cantidad: {len(agotado)}; Porcentaje: {round(len(agotado)*100/len(inventario),2)} %
        Productos con stock bajo → {bajo}; Cantidad: {len(bajo)}; Porcentaje: {round(len(bajo)*100/len(inventario),2)} %
        Productos con stock suficiente → {suficiente}; Cantidad: {len(suficiente)}; Porcentaje: {round(len(suficiente)*100/len(inventario),2)} %
        
        ''')


generar_reporte(inventario)


##########################################

# 5. Nivel entrevista (Analista de Datos Junior)

def procesando_tiempos (tiempos):
    
    reg_val = []
    
    total_reg_val = 0
    total_reg_desc = 0
    
    rapidas = 0
    normales = 0
    lentas = 0
    
    for tiempo in tiempos :
        try:
            tiempo_entero = int(tiempo)
            
            if tiempo_entero <= 0 :
                total_reg_desc += 1
                continue
            elif tiempo_entero <= 40:
                rapidas += 1
            elif tiempo_entero <= 60:
                normales += 1
            else:
                lentas += 1
            
            reg_val.append(tiempo_entero)
            
        except ValueError:
            total_reg_desc += 1
        
    total_reg = len(tiempos)
    total_reg_val = len(reg_val)
    
    tiempo_min = min(reg_val)
    tiempo_max = max(reg_val)
    tiempo_prom = round(sum(reg_val)/total_reg_val, 2)
    
    print(f'''
        
        ****************** Reporte de Tiempos de Entrega ******************
        
        Tiempos Válidos: {reg_val}
        
        Total de registros recibidos:{total_reg}
        Total de registros válidos: {total_reg_val}
        Total de registros descartados: {total_reg_desc}
        Tiempo promedio de las entregas válidas: {tiempo_prom}
        Tiempo mínimo: {tiempo_min}
        Tiempo máximo: {tiempo_max}
        
        Tipo de entregas
        rápidas = {rapidas}
        normales = {normales}
        lentas = {lentas}
        
        ''')
    

tiempos = [
    "35", "42", "error", "28", "51", "",
    "39", "60", "47", "-5", "55",
    "NA", "44", "31", "70"
]

procesando_tiempos(tiempos)