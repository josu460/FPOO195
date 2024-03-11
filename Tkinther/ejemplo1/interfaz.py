import tkinter as tk
from tkinter import messagebox
from main import Serie

# Crear una instancia de la clase Serie
mi_serie = Serie(titulo="emily in paris", genero="romance")

def reproducir_serie():
    resultado = mi_serie.reproducir()
    entry.insert(0, resultado)
    messagebox.showinfo("La serie es: ", resultado)

def click_agregar_lista():
    global lista
    resultado = mi_serie.agregar_a_lista(lista)
    messagebox.showinfo('La serie se agregó a la lista', resultado)

# Crear la ventana principal
root = tk.Tk()
root.title("SERIES")

# Etiqueta estática
label = tk.Label(root, text="¡Qué serie deseas ver!")
label.pack()

# Botón para reproducir la serie
button = tk.Button(root, text="Reproducir", command=reproducir_serie)
button.pack()

# Botón para agregar a la lista
button2 = tk.Button(root, text="Agregar a la lista", command=click_agregar_lista)
button2.pack()

# Cuadro de entrada
entry = tk.Entry(root)
entry.pack()

# Cuadro de texto
text_widget = tk.Text(root)
text_widget.pack()

# Crear una lista para almacenar las series
lista = []

# Ejecutar el bucle de eventos
root.mainloop()
