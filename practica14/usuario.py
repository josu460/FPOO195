class Usuario:
    def __init__(self, nombre, numero_cuenta):
        self.nombre = nombre
        self.numero_cuenta = numero_cuenta
    
    def __str__(self):
        return f"Nombre: {self.nombre}, Número de cuenta: {self.numero_cuenta}"