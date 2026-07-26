import pandas as pd

# 1.

df = pd.read_csv('Archivos/ventas.csv')

print(df.shape)
print(df.isnull().sum())
print(len(df[df['categoria'] == 'Electrónica']))

# 2.

df_no_nulos = df.dropna()
df_limpio = df_no_nulos.drop_duplicates(subset='nombre')
df_limpio['edad'] = df_limpio['edad'].astype(int)

print(df_limpio)

# 3.

filtro = df_limpio[
    (df_limpio["ciudad"].str.contains("Lima")) &
    (df_limpio["categoria"] == "Electrónica") &
    (df_limpio["edad"] >= 26)
]

print(len(filtro))
print(filtro['precio'].max())
print(filtro['precio'].mean())


# 4.

df_limpio['total']  = df_limpio['cantidad'] * df_limpio['precio']

print(df_limpio['total'].sum())
print(df_limpio['total'].max())
print(len(df_limpio[df_limpio['total'] > 1000]))


# 5.

df_col = df_limpio[['nombre','categoria','ciudad','cantidad','precio','total']]

print(df_col)

reporte = df_col[
    (df_col['ciudad'].str.contains('Lima')) &
    (df_col['nombre'].str.contains('a', case = False)) &
    (df_col['total'] > 1000)
]

print(reporte)
print(len(reporte))
print(reporte['total'].mean())
print(reporte['total'].min())