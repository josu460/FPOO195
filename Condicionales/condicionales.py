#ejercicio if 

'''
condicional if sin else 
z = 4
if z % 2 == 0:
    print("z is even")
    
    '''
'''
if completo  

z = int(input("ingresa el numero que quieras: "))
if z % 2 == 0:
    print("z es par ")
else:
    print("no es par ")
    '''
'''
room = "bed"
area = 14.0 

if room == "kit":
    print("looking around the kitchen")
elif room == "bed":
    print ("looking around the bedroom")
else:
    print("looking around elsewhere")
if area > 15: 
            print("big place!")
else:
            print("pretty small")
'''

#practica 4

# Escribir un programa que almacene la cadena de caracteres una contraseña en
# una variable, después que solicite al usuario una contraseña e imprima en
# pantalla si la contraseña introducida por el usuario coincide con la guardada en
# la variable sin tener en cuenta mayúscula y minúscula.

password = input("Crea una contraseña: ")

repite = input("Escribe nuevamente la contraseña: ")

if password == repite:
    print("Es correcta tu contraseña")
else: 
    print("La contraseña es incorrecta")
    
    
# Escribir un programa que pida al usuario un número entero y muestre por
# pantalla si es par o impar.
'''
numero = int(input("ingresa el numero que quieras: "))
if numero % 2 == 0:
    print("el numero es par ")
else:
    print("el numero no es par ")
    '''
    
#     Escribir un programa para una empresa que tiene salas de juegos para todas las
# edades y quiere calcular de forma automática el precio que debe cobrar a sus
# clientes por entrar. El programa debe preguntar al usuario la edad del cliente y
# mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar
# gratis, si tiene entre 4 y 18 años debe pagar $110 y si es mayor de 18 años, $190
'''
edad= int(input("Ingresa tu edad: "))

if edad <= 4:
    print("es gratis")
elif edad >=18:
    print("Tienes que pagar $190")
else:
    print("Tienes que pagar $110 ")
'''
# Codifica un programa que solicite una cadena de caracteres e imprima como
# resultado si la cadena es palíndromo o no

# palabra = str(input("Ingresa una palabra: "))
# if palabra == palabra[::-1]:
#     print("Es palindromo")
# else:
#     print("No es palindromo")