# ==========================================================
# STRINGS EN PYTHON - GUÍA PARA ANALISTA DE DATOS
# ==========================================================

# Un string es una secuencia de caracteres (texto).
# Los strings son INMUTABLES: una vez creados, no pueden modificarse directamente.

# ==========================================================
# DECLARACIÓN
# ==========================================================

nombre = "Miguel"
apellido = 'Chahua'

print(nombre)
print(apellido)

# String vacío
texto_vacio = ""

# String de varias líneas
mensaje = """
Hola
Bienvenido
a Python
"""

print(mensaje)

# ==========================================================
# ACCEDER A CARACTERES
# ==========================================================

texto = "Python"

print(texto[0])     # Primer carácter
print(texto[2])     # Tercer carácter
print(texto[-1])    # Último carácter
print(texto[-2])    # Penúltimo carácter

# ==========================================================
# RECORRER UN STRING
# ==========================================================

for letra in texto:
    print(letra)

# ==========================================================
# LONGITUD
# ==========================================================

print(len(texto))

# ==========================================================
# BUSCAR SI EXISTE TEXTO
# ==========================================================

frase = "Python para Data Analytics"

print("Python" in frase)
print("Java" in frase)

print("SQL" not in frase)

# ==========================================================
# CONCATENAR
# ==========================================================

nombre = "Miguel"
apellido = "Chahua"

completo = nombre + " " + apellido

print(completo)

# ==========================================================
# REPETIR TEXTO
# ==========================================================

print("-" * 30)

# ==========================================================
# MÉTODOS MÁS IMPORTANTES
# ==========================================================

texto = "   Python Para Data Analytics   "

# ----------------------------------------------------------
# lower() -> Convierte todo a minúsculas
# ----------------------------------------------------------

print(texto.lower())

# ----------------------------------------------------------
# upper() -> Convierte todo a mayúsculas
# ----------------------------------------------------------

print(texto.upper())

# ----------------------------------------------------------
# title() -> Primera letra de cada palabra en mayúscula
# ----------------------------------------------------------

print(texto.title())

# ----------------------------------------------------------
# capitalize() -> Solo la primera letra del texto
# ----------------------------------------------------------

print(texto.capitalize())

# ----------------------------------------------------------
# strip() -> Elimina espacios al inicio y al final
# ----------------------------------------------------------

print(texto.strip())

# ----------------------------------------------------------
# lstrip() -> Elimina espacios solo a la izquierda
# ----------------------------------------------------------

print(texto.lstrip())

# ----------------------------------------------------------
# rstrip() -> Elimina espacios solo a la derecha
# ----------------------------------------------------------

print(texto.rstrip())

# ==========================================================
# replace()
# Reemplaza texto por otro
# ==========================================================

texto = "Python"

print(texto.replace("Python", "Java"))

# También sirve para eliminar caracteres

correo = "miguel@gmail.com"

print(correo.replace("@gmail.com", ""))

# ==========================================================
# split()
# Divide un string en una lista
# ==========================================================

clientes = "Juan,Pedro,Ana,Carlos"

lista_clientes = clientes.split(",")

print(lista_clientes)

# También funciona con espacios

frase = "Python es genial"

print(frase.split())

# ==========================================================
# join()
# Une una lista de strings en un solo texto
# ==========================================================

nombres = ["Juan", "Pedro", "Ana"]

resultado = ", ".join(nombres)

print(resultado)

# ==========================================================
# startswith()
# Verifica cómo comienza un texto
# ==========================================================

correo = "miguel@gmail.com"

print(correo.startswith("miguel"))
print(correo.startswith("admin"))

# ==========================================================
# endswith()
# Verifica cómo termina un texto
# ==========================================================

print(correo.endswith(".com"))
print(correo.endswith(".pe"))

# ==========================================================
# find()
# Devuelve la posición donde encuentra el texto
# Si no existe devuelve -1
# ==========================================================

texto = "Python para Data Analytics"

print(texto.find("Data")) # Cuenta hast que encuentra la 'D' → 12.
print(texto.find("Java")) # Devuelve -1 cuando no encuentra nada.

# ==========================================================
# index()
# Igual que find(), pero genera error si no encuentra
# ==========================================================

print(texto.index("Python"))

# Descomentar para ver el error
# print(texto.index("Java"))

# ==========================================================
# count()
# Cuenta cuántas veces aparece un texto
# ==========================================================

fruta = "banana"

print(fruta.count("a"))
print(fruta.count("na"))

# ==========================================================
# VALIDACIONES
# ==========================================================

# Solo letras

print("Python".isalpha())
print("Python123".isalpha())

# Solo números

print("12345".isdigit())
print("123A".isdigit())

# Solo números (similar a isdigit)

print("123".isnumeric())

# Letras y números

print("Python123".isalnum())
print("Python 123".isalnum())

# Solo espacios

print("     ".isspace())
print("Python".isspace())

# ==========================================================
# CONVERSIONES
# ==========================================================

edad = "25"

edad = int(edad)

print(edad)
print(type(edad))

precio = "19.99"

precio = float(precio)

print(precio)

numero = 100

texto = str(numero)

print(texto)
print(type(texto))

# ==========================================================
# F-STRINGS (Forma recomendada)
# ==========================================================

nombre = "Miguel"
edad = 24

print(f"Hola, soy {nombre} y tengo {edad} años.")

# ==========================================================
# format() (Todavía aparece en proyectos antiguos)
# ==========================================================

print("Hola {}, tienes {} años.".format(nombre, edad))

# ==========================================================
# SLICING (Rebanado)
# ==========================================================

texto = "Python"

# Primeros 3 caracteres

print(texto[0:3])

# Desde la posición 2 hasta el final

print(texto[2:])

# Desde el inicio hasta la posición 4 (sin incluirla)

print(texto[:4])

# Cada dos caracteres

print(texto[::2])

# Invertir el texto

print(texto[::-1])

# ==========================================================
# LOS STRINGS SON INMUTABLES
# ==========================================================

texto = "Python"

# Esto genera error

# texto[0] = "J"

# Forma correcta

texto = "J" + texto[1:]

print(texto)

# ==========================================================
# MÉTODOS MÁS USADOS EN DATA ANALYTICS
# ==========================================================

# strip()      -> Limpiar espacios
# lower()      -> Normalizar texto
# upper()      -> Normalizar texto
# replace()    -> Corregir valores
# split()      -> Separar datos
# join()       -> Unir datos
# find()       -> Buscar texto
# count()      -> Contar apariciones
# startswith() -> Validar prefijos
# endswith()   -> Validar sufijos

# ==========================================================
# EJEMPLO REAL DE LIMPIEZA DE DATOS
# ==========================================================

cliente = "   Miguel Chahua   "

cliente = cliente.strip()      # Elimina espacios
cliente = cliente.title()      # Formato correcto

print(cliente)

correo = "MIGUEL@GMAIL.COM"

correo = correo.lower()

print(correo)

productos = "Laptop,Mouse,Teclado"

lista = productos.split(",")

print(lista)

texto = "Python es excelente"

texto = texto.replace("excelente", "genial")

print(texto)

# ==========================================================
# FIN DEL REPASO
# ==========================================================