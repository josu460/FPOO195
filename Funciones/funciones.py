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

# Escribir una función que calcule el total de una factura tras aplicarle
# el IVA. La función debe recibir la cantidad sin IVA y el porcentaje de
# IVA a aplicar, y devolver el total de la factura. Si se invoca la función
# sin pasarle el porcentaje de IVA, deberá aplicar un 21%.

precio= int(input("Ingresa el precio: "))

def total_factura(precio):
    