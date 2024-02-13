#listas y tuplas
#listas=[]
#tuplas=()

# ejercicio 1:Crea un programa usando funciones y lo que necesites para que el usuario inserte
# N números en una Tupla, después de la captura debe desplegar el siguiente menú
# funcional
# 1. Sumatoria de los elementos de la lista
# 2. Numero mayor de la lista  //ya esta
# 3. Numero menor de la lista  //ya esta 
# 4. Promedio
# 5. Moda: es el valor que más se repite de un conjunto de datos
# 6. Rango: es la diferencia entre el valor máximo y el valor mínimo de un
# conjuto de datos}


numeros = input("Ingrese los números que necesite separados por comas: ")

def agregar_numeros(numeros):
    numeros_separados = numeros.split(",")
    lista = []
    for numero in numeros_separados:
        lista.append(int(numero))
    return lista

lista = agregar_numeros(numeros)

tupla = tuple(lista)


def sumatoria(tupla):
    return sum(tupla)

def numero_mayor(tupla):
    return max(tupla)

def numero_menor(tupla):
    return min(tupla)

def promedio(tupla):
    return sum(tupla)/len(tupla)

def moda(tupla):
    return max(set(tupla), key=tupla.count)

def rango(tupla):
    return max(tupla) - min(tupla)






opcion = int(input("ingrese la opcion que desee: (numero del 1 al 6):  "))

if opcion == 1:
    print(sumatoria(tupla))
elif opcion == 2:
    print(numero_mayor(tupla))
elif opcion == 3:
    print(numero_menor(tupla))
elif opcion == 4:
    print(promedio(tupla))
elif opcion == 5:
    print(moda(tupla))
elif opcion == 6:
    print(rango(tupla))
else:
    print("Introduce un numero valido ")
