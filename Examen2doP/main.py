class Persona:
    def __init__(self, nombre, apellidoPaterno, apellidoMaterno, añoNacimiento, carrera,añoactual = 24,digitos = 897):
        self.nombre = nombre
        self.apellidoPaterno = apellidoPaterno
        self.apellidoMaterno = apellidoMaterno
        self.añoNacimiento = añoNacimiento
        self.carrera = carrera
        self.añoactual = añoactual
        self.digitos = digitos
        
    def generarMatricula(self):
        matricula = self.carrera[0:3] + str(self.añoactual) + self.añoNacimiento[2::2] + self.añoNacimiento[3::2]+ self.nombre[0:1] + self.apellidoPaterno[0:3] + self.apellidoMaterno[0:3]    + str(self.digitos)
        return matricula
    

  