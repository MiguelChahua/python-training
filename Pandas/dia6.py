import pandas as pd

# datos = {
#     'nombre' : ['Pedro', 'Juan', 'Lorena'],
#     'edad' : [25, 39, 33]
# }

# df = pd.DataFrame(datos)

# print(df)
# print(df['nombre'])     # Son iguales
# print(df.nombre)        # Son iguales

# print(df.index)

# df = pd.read_csv('Archivos/Precipitaciones.csv')
# print(df)
# print(df.head())
# print(df.tail())
# print(df.shape)
# print(df.info())
# print(df.describe())

numeros = [10, 20, 30, 40]
indices = ['a', 'b', 'c', 'd']

serie_con_indices = pd.Series(numeros,indices)

valor_c = serie_con_indices.c

print(serie_con_indices)
print(valor_c)

# import pandas as pd

dict = {'a': 30, 'b': 70, 'c': 160, 'd': 50}

serie_desde_diccionario = pd.Series(dict)

suma_ad = serie_desde_diccionario.a + serie_desde_diccionario.d

def imprimir_suma_ad():
    print(suma_ad)

imprimir_suma_ad()

# Operaciones con Series
# import pandas as pd

serie1 = pd.Series([4,15,8,71])
serie2 = pd.Series([12,1,37,60])

serie_sumada = serie1 + serie2

print(serie_sumada)


serie_numerica = pd.Series([2, 7, 5])

serie_doble = serie_numerica*2
serie_dividida = serie_numerica/10

print(serie_doble)
print(serie_dividida)


data = {
    'ID': [1, 2, 3, 4, 5],
    'Producto': ['Producto A', 'Producto B', None, 'Producto D', 'Producto E'],
    'Cantidad': [10, 20, 30, None, 50],
    'Precio': [100, 200, 300, 400, None]
}

df = pd.DataFrame(data)

print(df.isnull().sum())


# import pandas as pd

datos = {
    'ID': [1, 2, 3, 4, 1],
    'Producto': ['Producto A', 'Producto B', 'Producto C', 'Producto D', 'Producto A'],
    'Cantidad': [10, 20, 30, 40, 50],
    'Precio': [100, 200, 300, 400, 100]
}

df_sin_duplicados = pd.DataFrame(datos).drop_duplicates(subset='ID')

print(df_sin_duplicados)


datax = {
    'ID': [1, 2, 3, 4],
    'Producto': ['Producto A', 'Producto B', 'Producto C', 'Producto D'],
    'Cantidad': [10, 20, 30, 40],
    'Precio': [100, None, 300, None]
}

df = pd.DataFrame(datax)
valores_nuevos = { 'Precio' : df['Precio'].mean() }
df = df.fillna(valores_nuevos)

print(df)


# Filtrado de Series

valores = pd.Series([18, 22, 7, 9, 15, 8])
condicion_valores_pares = valores % 2 == 0
print(valores[condicion_valores_pares])


frutas = pd.Series(["manzana", "banana", "cereza", "durazno", "frambuesa"])
frutas_con_e = frutas.str.contains('e')
print(frutas[frutas_con_e])


# Agregaciones

edades = [23, 30, 26, 27, 22, 24, 25, 28]
edades_df = pd.Series(edades)
promedio_edades = edades_df.mean()
print(promedio_edades)


ventas = [120, 150, 90, 200, 210, 130, 160]
serie = pd.Series(ventas,['Lunes','Martes','Miércoles','Jueves','Viernes','Sábado','Domingo'])
suma_total_ventas = serie.sum()
dia_mayores_ventas = serie.idxmax()
promedio_ventas = serie.mean()

print(suma_total_ventas)
print(dia_mayores_ventas)
print(promedio_ventas)


ventas_mes = pd.Series([220, 235, 260, 213, 202, 298, 265, 198, 220, 230, 190, 215, 275, 222, 218, 245, 233, 210, 290, 210,
                        215, 220, 225, 230, 245, 250, 260, 270, 280, 295])
                        
total_ventas_mes = ventas_mes.sum()
dia_ventas_mas_bajas = ventas_mes.min()
promedio_ventas_mes = ventas_mes.mean()

print(total_ventas_mes)
print(dia_ventas_mas_bajas)
print(promedio_ventas_mes)