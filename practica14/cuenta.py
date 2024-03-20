class Cuenta:
    def __init__(self, num_cuenta, titular, edad, saldo):
        self.num_cuenta = num_cuenta
        self.titular = titular
        self.edad = edad
        self.saldo = saldo

    def consultar_saldo(self):
        return self.saldo

    def ingresar_efectivo(self, cantidad):
        self.saldo += cantidad
        return f'Se han ingresado {cantidad} pesos. Nuevo saldo: {self.saldo} pesos'

    def retirar_efectivo(self, cantidad):
        if cantidad > self.saldo:
            return 'No hay saldo suficiente en la cuenta.'
        else:
            self.saldo -= cantidad
            return f'Se han retirado {cantidad} pesos. Nuevo saldo: {self.saldo} pesos'

    def depositar_otra_cuenta(self, otra_cuenta, cantidad):
        if cantidad > self.saldo:
            return 'No hay saldo suficiente en la cuenta para realizar el depósito.'
        else:
            self.saldo -= cantidad
            otra_cuenta.ingresar_efectivo(cantidad)
            return f'Se han depositado {cantidad} pesos en la cuenta {otra_cuenta.num_cuenta}. Nuevo saldo: {self.saldo} pesos'