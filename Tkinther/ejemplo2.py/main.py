import math

class Fraccion:
    def __init__(self, numerador, denominador):
        self.__numerador = numerador
        self.__denominador = denominador
        
    def getnumerador(self):
        return self.__numerador
    def getdenominador(self):
        return self.__denominador
    
    
    def sumar(self, fraccion):
        numerador = self.getnumerador() * fraccion.getdenominador() + fraccion.getnumerador() * self.getdenominador()
        denominador = self.getdenominador() * fraccion.getdenominador()
        return Fraccion(numerador, denominador)
    
    def restar(self, fraccion):
        numerador = self.getnumerador() * fraccion.getdenominador() - fraccion.getnumerador() * self.getdenominador()
        denominador = self.getdenominador() * fraccion.getdenominador()
        return Fraccion(numerador, denominador)
    
    def multiplicar(self, fraccion):
        numerador = self.getnumerador() * fraccion.getnumerador()
        denominador = self.getdenominador() * fraccion.getdenominador()
        return Fraccion(numerador, denominador)
    
    def dividir(self, fraccion):
        numerador = self.getnumerador() * fraccion.getdenominador()
        denominador = self.getdenominador() * fraccion.getnumerador()
        return Fraccion(numerador, denominador)
    
    def simplificar(self):
        numerador = self.getnumerador()
        denominador = self.getdenominador()
        mcd = math.gcd(numerador, denominador)
        numerador = numerador // mcd
        denominador = denominador // mcd
        return Fraccion(numerador, denominador)