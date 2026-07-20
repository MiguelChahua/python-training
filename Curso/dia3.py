# Strings

frase = input('Escribe un texto de al menos 10 palabras: ')

caracteres = len(frase.strip())
caracteres_se = len(frase.strip()) - frase.count(' ')
vocales = frase.count('a') + frase.count('e') + frase.count('i') + frase.count('o') + frase.count('u')
letras = len(frase.strip().split(' '))

ft = frase.split(maxsplit=1)
frase_spp = ft[1]
reemplazo = frase.replace(' ','-')
frase_swap = frase.swapcase()

print(f'''
      
    Cantidad de caracteres: {caracteres}
    Cantidad de caracteres sin espacios: {caracteres_se}
    Cantidad de vocales: {vocales}
    Cantidad de letras: {letras}

    Frase sin primera palabra: {frase_spp}
    Frase reemplazada: {reemplazo}
    Frase invertida: {frase_swap}
    
    '''

    )