#ciclo do while 

'''
contador = 1 
while contador <= 5:
    print(contador)
    if contador == 3:
        break
   
    contador += 1
else:
    print("el bucle esta terminado normalemente ")
'''


# ciclo while con continue

'''
contador = 0
while contador < 5:
    contador += 1
    if contador == 3:
        continue
    print(contador)
    
else:
    print("el bucle esta terminado normalemente ")
'''


#ciclo while con else
'''
contador=1

while contador <= 10:
    print(contador)
    contador += 1
else:
    print("el bucle esta terminado normalemente ")
'''

#ciclo for 
'''
palabra = input("ingresa una palabra: ")

contador_vocales = 0

for letra in palabra:
    if letra.lower() in "aeiou":
        contador_vocales += 1
print(f"la palabra '{palabra}'tiene {contador_vocales} vacal(es).")
'''

#este programa va a calcular la suma de los numeros del 1 al 10 
'''
suma= 0
for num in range(1,11):
    if num % 2 == 0:
        suma += num
print(f"la suma de los numeros pares del 1 al 10 es: {suma}")
'''

# Escribir un programa que pida al usuario un número entero positivo y muestre
# por pantalla todos los números impares desde 1 hasta ese número separados
# por comas.
'''
numero = int(input("ingresa un numero entero positivo: "))

for numero in range(1,numero+1,2):
    print(numero, end=", ")
'''

# Escribir un programa que pida al usuario un número entero positivo y muestre
# por pantalla la cuenta atrás desde ese número hasta cero separados por comas.

'''
numero = int(input("Ingresa un numero entero positivo: "))
for i in range (numero,-1,-1):
    print(i , end =",")
'''

#Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.

'''
for x in range (1,11):
    multiplicacion= 1 * x
    print(f'1 x {x} = {multiplicacion}')
for x in range (1,11):
    multiplicacion= 2 * x
    print(f'2 x {x} = {multiplicacion}')
for x in range (1,11):
    multiplicacion= 3 * x
    print(f'3 x {x} = {multiplicacion}')
for x in range (1,11):
    multiplicacion= 4 * x
    print(f'4 x {x} = {multiplicacion}')
for x in range (1,11):
    multiplicacion= 5 * x
    print(f'5 x {x} = {multiplicacion}')
for x in range (1,11):
    multiplicacion= 6 * x
    print(f'6 x {x} = {multiplicacion}')
for x in range (1,11):
    multiplicacion= 7 * x
    print(f'7 x {x} = {multiplicacion}')
for x in range (1,11):
    multiplicacion= 8 * x
    print(f'8 x {x} = {multiplicacion}')
for x in range (1,11):
    multiplicacion= 9 * x
    print(f'9 x {x} = {multiplicacion}')
for x in range (1,11):
    multiplicacion= 10 * x
    print(f'10 x {x} = {multiplicacion}')
'''

# Escribir un programa que pida al usuario un número entero y muestre por
# pantalla un triángulo rectángulo como el de más abajo, de altura el número
# introducido. (img 1)
'''
base = int(input("Introduce la altura del trinagulo (numero positivo): "))
for i in range(1, base+1, 2):
    for j in range(i, 0, -2):
        print(j, end=" ")
    print("")
'''

# Escribir un programa en el que se pregunte al usuario por una frase y una letra,
# y muestre por pantalla el número de veces que aparece la letra en la frase.

'''
frase = str(input("Escribe una frase: "))
letra = str(input("Escribe una letra: "))

contador_letra = 0

for i in frase:
    if i == letra:
        contador_letra += 1

print(f"La frase tiene '{contador_letra}' letras '{letra}'.")
'''

# Escriba un programa que administre una cuenta bancaria, usando una bitácora
# de operaciones. (img 2)
# La bitácora de operaciones tiene la siguiente forma:
# D 100
# R 50
# D 100 significa que depositó 100 pesos
# R 50 significa que retiró 50 pesos
# Introducir una línea vacía indica que ha finalizado la bitácora e imprime el saldo
# final
'''
saldo = 0

transacciones = int(input("Escribe el numero de operaciones a realizar:  "))

for i in range (transacciones):
    operacion = input("Escribe la operacion (D/R): ")
    cantidad = int(input("Escribe la cantidad: "))
    if operacion == "D":
        saldo += cantidad
    elif operacion == "R":
        saldo -= cantidad
    else:
        print("Operacion invalida")
        break
    print(f"____________")
    print(f"El saldo es: {saldo}")
    
    print(f"las transacciones son: {operacion}  {cantidad}")
'''

# Imprime un árbol de navidad formado con Asteriscos haciendo uso del while,
# Solicitando al usuario la cantidad de * de la base (img 3)


base =int(input("Escribe el tamaño de la base de tu arbol: "))


while base > 0:
    print(" " * base + "*" * (base * 2 - 1))
    base -= 1