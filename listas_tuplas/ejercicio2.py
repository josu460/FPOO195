# Crea un programa que llene una lista de 30 valores aleatorios en un rango del 10
# al 20, con la lista llena el usuario podrá
# a. Contar número repetidos
# b. Eliminar numero repetidos
# c. Remplazar los repetidos con 0



import random

def contar_repetidos(lista):
    repetidos = []
    for i in lista:
        if lista.count(i) > 1 and i not in repetidos:
            repetidos.append(i)
    return repetidos

def reemplazar_repetidos(lista):
    for i in range(len(lista)):
        if lista[i] in repetidos:
            lista[i] = 0

def eliminar_repetidos(lista):
    for elemento in repetidos:
        while elemento in lista:
            lista.remove(elemento)
    return lista

aleatorios = [random.randint(10, 20) for _ in range(30)]
print(aleatorios)

seleccion = input("Introduce la letra de la opción que quieras realizar (a, b, c): ")

repetidos = contar_repetidos(aleatorios)

if seleccion == "a":
    print(f'los valores repetidos son : {contar_repetidos(aleatorios)}')
elif seleccion == "b":
    print(f'los que no se eliminaron fueron:{eliminar_repetidos(aleatorios.copy())}')
elif seleccion == "c":
    reemplazar_repetidos(aleatorios)
    print(f'los valores remplazados quedaron asi: {aleatorios}')
else:
    print("Introduce una de las tres letras, por favor.")
