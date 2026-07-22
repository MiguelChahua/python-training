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