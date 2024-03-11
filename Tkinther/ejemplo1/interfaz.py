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
    
def click_marcar_como_completada():
    mi_serie.marcar_como_completada()
    messagebox.showinfo('La serie se completó', f"{mi_serie.titulo} se ha marcado como completada")
    

def click_ver_lista():
    text_widget.delete('1.0', tk.END)
    for serie in lista:
        text_widget.insert(tk.END, serie.detalles() + "\n")
        
def click_calificar():
    calificacion = entry2.get()
    resultado = mi_serie.calificar(calificacion)
    messagebox.showinfo('Calificación', resultado)

# Crear la ventana principal
root = tk.Tk()
root.title("SERIES")

# Etiqueta estática
label = tk.Label(root, text="¡Qué serie deseas ver!")
label.pack()

# Botón para reproducir la serie
button = tk.Button(root, text="Reproducir", command=reproducir_serie, bg='blue', fg='white')
button.pack(pady=10)

# Botón para agregar a la lista
button2 = tk.Button(root, text="Agregar a la lista", command=click_agregar_lista, bg='green', fg='white')
button2.pack(pady=10)

button4 = tk.Button(root, text="Marcar como completada", command=click_marcar_como_completada, bg='red', fg='white')
button4.pack(pady=10)

entry2 = tk.Entry(root)
entry2.pack(pady=10)

button5 = tk.Button(root, text="Calificar", command=click_calificar, bg='yellow', fg='black')
button5.pack(pady=10)


button3 = tk.Button(root, text="Ver lista", command=click_ver_lista, bg='purple', fg='white')
button3.pack(pady=10)

# Cuadro de entrada
entry = tk.Entry(root, width=50 )
entry.pack(pady=10)

# Cuadro de texto
text_widget = tk.Text(root)
text_widget.pack(pady=10)

# Crear una lista para almacenar las series
lista = []

# Ejecutar el bucle de eventos
root.mainloop()
