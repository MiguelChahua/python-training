# Diccionarios: alamcena datos clave:valor

persona = {
    'nombre' : 'Miguel',
    'edad' : 30,
    'ciudad' : 'Lima'
}

datos = {} # Dicc. vacio

# Diccioarios acepta varios tipos de datos, incluso otros diccionarios
usuario = {
    "nombre": "Miguel",
    "edad": 25,
    "activo": True,
    "notas": [18, 17, 20],
    "direccion": {
        "ciudad": "Lima",
        "pais": "Perú"
    }
}

print(persona["nombre"]) # Acceder a datos, es mediante clave
print(persona.get("nombre")) # get es mas usado en Data Analyst

# Si una clave no existe, podemos colocar un valor por defecto
print(persona.get('telefono','No registrado'))


persona['edad'] = 26 # Actualizar valores
print (persona) # Saldra ya actualizado

persona['telefono'] = '999130371' # Agregando nueva clave y su valor
print(persona)

del persona['telefono'] # Eliminar elemento
print(persona)