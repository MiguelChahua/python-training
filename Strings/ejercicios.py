
# Ejercicio 1

nombre = "   miguel angel chahua villanueva   "
limpio = nombre.strip()
mejorado = limpio.title()

print(limpio)
print(mejorado)
print(len(limpio))
print(mejorado.find('Angel'))
print(mejorado.replace('Villanueva', 'Flores'))

# Ejercicio 2

correo = "   MIGUEL.CHAHUA@GMAIL.COM   "

espacios = correo.strip()
minusculas = espacios.lower()
termina = minusculas.endswith('.com')
empieza = minusculas.startswith('miguel')
reemplazar = minusculas.replace('@gmail.com', '')
print(termina)
print(empieza)
print(reemplazar)

# Ejercicio 3

productos = "Laptop,Mouse,Teclado,Monitor,USB,Cámara"
lista = productos.split(',')
unido = ' | '.join(lista)

print(lista)
print(len(lista))
print(unido)
print(productos.find('Monitor')>0)
print(productos.find('USB'))
print(productos.count('a'))

# Ejercicio 4

dato1 = "Python"
dato2 = "123456"
dato3 = "Python2026"
dato4 = "     "
dato5 = "2026A"

print(dato1.isalpha())
print(dato2.isdigit())
print(dato3.isalnum())
print(dato4.isspace())

print(int(dato2))
print(str(1500))


# Ejercicio 5

registro = "   juan perez|25|LIMA|Analista de Datos|juan.perez@gmail.com   "

lista = registro.strip().split('|')

print(f'''
    Cliente: {lista[0].title()}
    Edad: {int(lista[1])}
    Ciudad: {lista[2].lower()}
    Cargo: {lista[3]}
    Correo: {lista[4].replace('@gmail.com','')}
''')

print(f'Cargo contiene datos?: {'Datos' in lista[3]}')
print(f'Correo contiene .com?: {'.com' in lista[4]}')
print(f'Cantidad de caracteres: {len(registro.strip())}')