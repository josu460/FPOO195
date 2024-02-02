#funciones 

'''
def suma(*numeros):
    resultado= sum (numeros)
    print("suma: ", resultado)
suma(1,2,3,4,5)
'''

'''
def area_cuadrado(lado):
    return lado**2

#def main():

lado_cuadrado = float(input("ingrese valor del lado: "))
area_result= area_cuadrado(lado_cuadrado)
    
print(f"area del cuadrado: {area_result}")
'''

#comienzan los ejercicios

# Escribir una función que calcule el total de una factura tras aplicarle
# el IVA. La función debe recibir la cantidad sin IVA y el porcentaje de
# IVA a aplicar, y devolver el total de la factura. Si se invoca la función
# sin pasarle el porcentaje de IVA, deberá aplicar un 21%.
'''
precio= float(input("Ingresa el total de la factura: "))
iva = int(input("Ingresa el total del iva a aplicar:") or 21)

def total_factura(precio, iva=21):
    return((float(precio)/100)*iva)+precio

    
if iva != "":
    print(f"El total de la factura es: {total_factura(precio,iva)}")
else:
    print(f"El total de la factura es: {total_factura(precio)}")

'''


# Escribir una función que calcule el área de un círculo y otra que
# calcule el volumen de un cilindro usando la primera función.
'''
pi= 3.1416 
radio=int(input("introduce el radio: "))

def circulo(pi,radio):
    area_circulo=(pi*(radio*radio))
    return(area_circulo)
total_circulo= circulo(pi,radio)
print(f"El area del circulo es: {circulo(pi,radio)}")

h = int(input("introduce la altura del cilindro: "))
def cilindro(area_circulo,h):
    area_cilindro=(area_circulo * h)
    return(area_cilindro)
total_cilindro= cilindro(total_circulo,h)
print(f"El area del cilindro es: {total_cilindro}")
'''

# Escribir una función que convierta un número decimal en binario y
# otra que convierta un número binario en decimal.


def decimal_binario(decimal):
    return bin(decimal)[2:]
def binario_decimal(binario):
    return int(binario,2)
    
decimal= int(input("Introduce un numero decimal: "))
print(decimal_binario(decimal))
binario= input("Introduce un numero binario: ")
print(binario_decimal(binario))
