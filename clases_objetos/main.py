#Asi se importan las clases de otros archivos
from Personaje import * 
from Armas import *



#solicitar datos SPARTANs
print("========Datos del Heroe==========")
especieS = input("Escribe la especie de tu Spartan: ")
nombreS = input("Escribe el nombre de tu Spartan: ")
alturaS =float(input("Escribe la altura de tu Spartan: "))
print("============Datos del Heroe==========")
#solicitar datos Nemesis

print("========Datos del Nemesis==========")
especieN = input("Escribe la especie de tu Nemesis: ")
nombreN = input("Escribe el nombre de tu Nemesis: ")
alturaN =float(input("Escribe la altura de tu Nemesis: "))
print("============Datos del Nemesis==========")



# creamos el objeto de la clase personaje   
spartan = Personaje(especieS,nombreS,alturaS)
nemesis = Personaje(especieN,nombreN,alturaN)
Arma= Armas()
#usamos los atributos del spartan
print("============El objeto spartan contiene==========")
print(spartan.nombre)
print(spartan.especie)
print(spartan.altura)
print("")

#usamos los atributos del nemesis
print("============El objeto nemesis contiene==========")
print(nemesis.nombre)
print(nemesis.especie)
print(nemesis.altura)
#usamos los metodos del spartan
print("============Metodos del objeto spartan==========") 
spartan.correr(False)
spartan.lanzarGranada()
print("")

print("============Metodos del objeto nemesis==========") 
nemesis.correr(False)
nemesis.lanzarGranada()
print("")

#usamos los metodos del arma
Arma.seleccionar_arma(spartan.nombre)
Arma.recargarArma(65)   