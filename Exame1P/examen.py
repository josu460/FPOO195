#escribir un programa que visualice los numeros multiplos de 10 comprendidos entre 10 y 1000

contador = 0
while contador <= 990:
   
    contador += 10
    print(contador)
    

#ejercicio 2:
#Programa con funciones y un menu que nos permita convertir temperaturas a decision del usuario 

grado = str(input("Introduce la inicial del grado al que quieras convertir (f,k,c): "))
numero = float(input("Introduce la cantidad a convertir: "))

def faherenheit(numero):
    conversion1=((numero*9/5)+32)
    return(conversion1)
resultado_f=faherenheit(numero)

def kelvin(numero):
    conversion2=(numero+273.15)
    return(conversion2)
resultado_k=kelvin(numero)

def centigrados(numero):
    conversion3=((numero-32)*5/9)
    return(conversion3)
resultado_c=centigrados(numero)

if grado == "f":
    print(resultado_f)
elif grado =="k":
    print(resultado_k)
elif grado == "c":
    print(resultado_c)
else:
    print("introduce una de las tres letras porfavor ")