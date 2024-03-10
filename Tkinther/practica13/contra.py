from tkinter import *
from tkinter import ttk, messagebox

from main import Generador_Contraseñas
def click_generar():
    length = int(caja1.get()) if caja1.get()else 8
    
    caja_mayusculas = caja2.get().lower() == 'si'
    caja_caracteres = caja3.get().lower() == 'si'
    generador_contraseña = Generador_Contraseñas(length, caja_mayusculas, caja_caracteres)
    contraseña = generador_contraseña.generar()
    caja4.insert(0, contraseña)
    messagebox.showinfo("Contraseña generada", contraseña)

def click_verificar():
    contraseña = caja4.get()
    caja_mayusculas = caja2.get().lower() == 'si'
    caja_caracteres = caja3.get().lower() == 'si'
    
    if len(contraseña) < 8 or not caja_mayusculas or not caja_caracteres:
        messagebox.showinfo("Verificación de contraseña", "La contraseña es débil.")
    else:
        messagebox.showinfo("Verificación de contraseña", "La contraseña es fuerte.")

ventana = Tk()
ventana.title("Contraseña")
ventana.geometry("600x500")

seccion = Frame(ventana, bg="gray")
seccion.pack(expand=True, fill="both")

titulo = Label(seccion, text="Contraseñas", font=("Arial", 20))
titulo.place(x=200, y=10)

text = Label(seccion, text="Ingresa la longitud de la contraseña", font=("Arial", 10))
text.place(x=200, y=60)
caja1 = ttk.Entry(seccion)
caja1.place(x=230, y=100, width=100, height=30)

text2 = Label(seccion, text="Ingrese si quiere mayúsculas", font=("Arial", 10))
text2.place(x=200, y=200)
caja2 = ttk.Entry(seccion)
caja2.place(x=230, y=250, width=100, height=30)

text3 = Label(seccion, text="Ingrese si quiere caracteres especiales", font=("Arial", 10))
text3.place(x=200, y=300)
caja3 = ttk.Entry(seccion)
caja3.place(x=230, y=350, width=100, height=30)

botonContra = Button(seccion, text="Generar", fg="black", bg="white", command=click_generar)
botonContra.configure(height=2, width=10)
botonContra.place(x=230, y=400, width=100, height=30)

botonVerificar = Button(seccion, text="Verificar", fg="black", bg="white", command=click_verificar)
botonVerificar.configure(height=2, width=10)
botonVerificar.place(x=230, y=450, width=100, height=30)

text4 = Label(seccion, text="La contraseña que se generó es:", font=("Arial", 10))
text4.place(x=200, y=500)
caja4 = ttk.Entry(seccion)
caja4.place(x=230, y=550, width=100, height=30)

ventana.mainloop()
