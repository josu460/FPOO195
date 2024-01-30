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

for x in range (1,11):
    multiplicacion= 1 * x
    print(f'1 x {x} = {multiplicacion}')
for x in range (1,11):
    multiplicacion= 2 * x
    print(f'2 x {x} = {multiplicacion}')
for x in range (1,11):
    multiplicacion= 3 * x
    print(f'3 x {x} = {multiplicacion}')