class Serie:
    #título, horas estimadas, status, género y calificación. 
    def __init__(self,titulo, genero,horas_estimadas = 10,status ="sin reproducir" ,calificacion = None):
        self.__titulo = titulo 
        self.__genero = genero
        self.__horas_estimadas = horas_estimadas
        self.__status = status
        
        self.__calificacion = calificacion
        
    def gettitulo(self):
        return self.__titulo
    def getgenero(self):
        return self.__genero
    def gethoras_estimadas(self):
        return self.__horas_estimadas
    def getstatus(self):
        return self.__status
    def getcalificacion(self):
        return self.__calificacion

        
        #las horas estimadas serán de 10 horas y status sin reproducir.
        
# Marcar como completada y Calificar, los cuales
# se encargar de modificar los atributos correspondientes del objeto a selección del
# usuario

    def reproducir(self):
        return f"Reproduciendo {self.__titulo}"

    def agregar_a_lista(self, lista):
        lista.append(self)
        return f"{self.__titulo} agregada a la lista"

    def marcar_como_completada(self):
        self.status = "Completada"

    def calificar(self, calificacion):
        self.__calificacion = calificacion
        return f"Se ha calificado {self.__titulo} con {calificacion} estrellas"


lista = []