from ejeprac2 import *

mi_serie = Serie("The Office", "Comedia")
mi_serie2 = Serie("emily in paris", "romance")

print(mi_serie.reproducir())
print(mi_serie.agregar_a_lista(lista))

mi_serie.marcar_como_completada()
print(f"El status de la serie es ahora: {mi_serie.getstatus()}")

print(mi_serie2.calificar(5))

print(mi_serie2.reproducir())
print(mi_serie2.agregar_a_lista(lista))

mi_serie2.marcar_como_completada()
print(f"El status de la serie es ahora: {mi_serie2.getstatus()}")

print(mi_serie2.calificar(5))
