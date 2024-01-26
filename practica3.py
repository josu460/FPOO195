#Crea un programa que pregunte al usuario por el número de horas trabajadas y el
#coste por hora. Después debe mostrar por pantalla la paga que le corresponde.

'''
horas = int(input("Introduce el número de horas trabajadas: "))
costo = int(input("Introduce el coste por hora: "))
#aqui multiplicamos las horas trabajadas por el costo de las horas
paga = horas * costo

print ("la paga total fue de" , paga, "pesos")

'''

# ejercicio 2:Codifica un programa que pregunte el nombre completo del usuario en la consola y
# después muestre por pantalla el nombre completo del usuario tres veces, una con
# todas las letras minúsculas, otra con todas las letras mayúsculas y otra solo con la
# primera letra del nombre y de los apellidos en mayúscula. El usuario puede
# introducir su nombre combinando mayúsculas y minúsculas como quiera.
'''
nombre = str(input("Introduce tu nombre: "))
apellido = str(input("Introduce tus apellidos: "))
nombre_minusculas = nombre.lower(),apellido.lower()

nombre_mayusculas = nombre.upper(),apellido.upper()

print(nombre_minusculas)
print(nombre_mayusculas)
print(nombre[0],apellido.upper())

'''

# Escribir un programa que solicite un entero X, introducido por el usuario y después
# muestre en pantalla la suma de todos los enteros desde 1 hasta X .

'''
x = int(input("introduce el valor de x: "))

suma = sum(range(1, x +1))

print(suma)

'''

# Codifica un programa que pregunte el nombre del usuario y después de que el
# usuario lo introduzca muestre por pantalla <NOMBRE> tiene <n> letras, donde
# <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número de letras
# que tienen el nombre.
'''
nombre= str(input("Introduce tu nombre completo: "))
nombre_mayusculas=nombre.upper()
contar=len(nombre)
print(len( nombre))
print(nombre_mayusculas)
print(nombre_mayusculas, "tiene un total de:",contar)
'''

# Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas.
# Suele hacer venta por correo y la empresa de logística les cobra por peso de cada
# paquete así que deben calcular el peso de los payasos y muñecas que saldrán en
# cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un
# programa que lea el número de payasos y muñecas vendidos en el último pedido y
# calcule el peso total del paquete que será enviado.

payaso = int(input("Cuantos payasos quieres: "))
muneca = int(input("cuantas nuñecas quieres: "))
peso_payaso = 112
peso_muñeca = 75
total = (payaso*peso_payaso)+(muneca*peso_muñeca)
print= (total)
# Crea un programa que pida al usuario que introduzca una frase en y muestre en
# pantalla la frase invertida.

'''
frase = str(input("escribe una frese: "))

frase_invertido= frase[::-1]

print(frase_invertido)
'''