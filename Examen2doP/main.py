class Persona:
    def __init__(self, nombre, apellidoPaterno, apellidoMaterno, añoNacimiento, carrera,añoactual = 20,digitos = 897):
        self.nombre = nombre
        self.apellidoPaterno = apellidoPaterno
        self.apellidoPaterno = apellidoMaterno
        self.apellidoMaterno = apellidoMaterno
        self.añoNacimiento = añoNacimiento
        self.carrera = carrera
        self.añoactual = añoactual
        self.digitos = digitos
    def generarMatricula(self):
        matricula = self.nombre[0:3] + self.apellidoPaterno[0:3] + self.apellidoMaterno[0:3] + str(self.añoNacimiento[0:2]) + self.carrera[0:3] + str(self.añoactual) + str(self.digitos)
        return matricula
    
    
  