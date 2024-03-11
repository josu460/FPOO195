class Serie:
    def __init__(self, titulo, genero, calificacion=None, status='sin reproducir', horasestimadas=10):
        self.__titulo = titulo
        self.__genero = genero
        self.__calificacion = calificacion
        self.__status = status
        self.__horasestimadas = horasestimadas

    def gettitulo(self):
        return self.__titulo
    def getgenero(self):
        return self.__genero
    def getcalificacion(self):
        return self.__calificacion
    def getstatus(self):
        return self.__status
    def gethorasestimadas(self):
        return self.__horasestimadas
    
    def reproducir(self):
        return f"Reproduciendo {self.gettitulo()}"

    def agregar_a_lista(self, lista):
        lista.append(self)
        return f"{self.gettitulo()} agregada a la lista"

    def marcar_como_completada(self):
        self.__status = "Completada"

    def calificar(self, calificacion):
        self.__calificacion = calificacion
        return f"Se ha calificado {self.gettitulo()} con {calificacion} estrellas"

    def ver_series(self, lista):
        for serie in lista:
            print(f"{serie.gettitulo()} - {serie.getgenero()} - {serie.getcalificacion()} - {serie.getstatus()} - {serie.gethorasestimadas()}")

    def detalles(self):
        return f"{self.gettitulo()} - {self.getgenero()} - {self.getcalificacion()} - {self.getstatus()} - {self.gethorasestimadas()}"

lista = []
