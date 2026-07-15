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

llaves = usuario.keys()     # Te da las llaves
print(llaves)
print(list(llaves))         # Convertido a lista

valores = usuario.values()  # Te da los valores
print(valores)

items = usuario.items()     # Te da clave : valor
print(items)


usuario.update({            # Permite actualizar varios elementos al mismo  tiempo, tambien se puede agregar claves y valores nuevos.
    'edad' : 26,
    'notas' : [15,17,15]
})
print(usuario)



edad = usuario.pop('edad') # Método POP elimina un elemento, por su clave, pero antes devuelve su valor

print(edad) # 26
print(usuario) # Saldra ya sin edad

copia = usuario.copy()          # Crea una copia
copia.clear()
print(copia)


x = usuario.setdefault('activo')    # Setdefault prueba si existe la clave y devuelve su valor
print(x) # True

usuario.setdefault('telefono', 'No registrado') # Sino puedes agregarle, como get
print(usuario)


print(usuario['direccion']['ciudad']) # Accediendo a datos internos