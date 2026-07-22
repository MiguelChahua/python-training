# contador = 0
# while contador <= 15:
#     if contador == 5 or contador == 10:
#         contador += 1
#         continue
    
#     print(contador)
#     contador += 1
    
################################################################
################################################################
################################################################

# def pedir_numeros():
#     x1 = int(input('Ingrese primer numero: '))
#     x2 = int(input('Ingrese segundo numero: '))
    
#     return x1,x2
    
# def sumar():
#     suma = sum(pedir_numeros())
#     print(f'La suma es {suma}')
    
# sumar()

################################################################
################################################################
################################################################

def solicitar_numero():
    num = int(input('Ingrese un número entero positivo: '))
    return num
    
def calcular_factorial(n):
    fac = 1
    for x in range(1,n+1):
        fac = fac*x
    return fac

x = calcular_factorial(solicitar_numero())

print(f'El factorial es {x}')