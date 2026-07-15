import pandas as pd

# Leer un DF seria un Dataframe que es una tabla
df = pd.read_csv('Archivos/ventas.csv') 

print(df)               # Imprime la tabla
# print(df.head())        # Imprime los primeros 5 registros
# print(df.tail())        # Imprime los ultimos registros
# print(df.info())        # Imprime: número de filas, col, tip datos, valores nulos.
# print(df.describe())    # Estadísticas rápidas
# print(df.columns)       # Nombres de columnas

# print(df.shape)         # Tamaño del DF: (filas, columnas) → (4, 3)

# Agregar filas
df.loc[len(df)] = ['Webcam', 50, 10] # len(df) → Da el indice siguiente para registrar, en este caso 4
print(df)

# Actualizar filas
df.loc[4] = ['Parlantes', 150, 5]
print(df)

# Tambien se puede actualizar solo una columna
df.loc[4, "Producto"] = 'Impresora'
print(df)


# Eliminar una fila
df = df.drop(4)
print(df)


# Guardar un CSV
df.to_csv("resultado.csv", index=False)