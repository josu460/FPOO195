import string
import random
class Generador_Contraseñas:
    def __init__(self, longitud=8, caja_mayusculas=True, caja_caracteres=True):
        self.longitud = longitud
        self.caja_mayusculas = caja_mayusculas
        self.caja_caracteres = caja_caracteres

    def generar(self):
        caracteres = string.ascii_lowercase
        if self.caja_mayusculas:
            caracteres += string.ascii_uppercase
        if self.caja_caracteres:
            caracteres += string.punctuation
        return ''.join(random.choice(caracteres) for _ in range(self.longitud))

