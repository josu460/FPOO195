class Serie:
    def __init__(self, titulo, genero, calificacion=None, status='sin reproducir', horasestimadas=10):
        self.titulo = titulo
        self.genero = genero
        self.calificacion = calificacion
        self.status = status
        self.horasestimadas = horasestimadas

    def reproducir(self):
        return f"Reproduciendo {self.titulo}"

    def agregar_a_lista(self, lista):
        lista.append(self)
        return f"{self.titulo} agregada a la lista"

    def marcar_como_completada(self):
        self.status = "Completada"

    def calificar(self, calificacion):
        self.calificacion = calificacion
        return f"Se ha calificado {self.titulo} con {calificacion} estrellas"

    def ver_series(self, lista):
        for serie in lista:
            print(f"{serie.titulo} - {serie.genero} - {serie.calificacion} - {serie.status} - {serie.horasestimadas}")

    def detalles(self):
        return f"{self.titulo} - {self.genero} - {self.calificacion} - {self.status} - {self.horasestimadas}"

lista = []


