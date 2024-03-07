from tkinter import *
from tkinter import ttk, messagebox
from practica import Usuario


def validar_usuario(input1, input2):
    correo = input1.get()
    contraseña = input2.get()
    if correo == "" or contraseña == "":
        messagebox.showinfo('Error', 'Por favor, introduce tu correo y contraseña')
    else:
        if Usuario.validar_usuario(correo, contraseña):
            messagebox.showinfo('Bienvenido', 'Bienvenido!!')
        else:
            messagebox.showinfo('Acceso denegado', 'Acceso denegado!!')

ventana = Tk()
ventana.title("login")
ventana.geometry("600x500")

seccion = Frame(ventana, bg="gray")
seccion.pack(expand=True, fill="both")

titulo = Label(seccion, text="LOGIN", font=("Arial", 20))
titulo.place(x=250, y=10)

caja1 = ttk.Entry(seccion)
caja1.place(x=230, y=70, width=100, height=30)

seccion2 = Frame(ventana, bg="gray")
seccion2.pack(expand=True, fill="both")

input2 = ttk.Entry(seccion2, show="*")
input2.place(x=230, y=40, width=100, height=30)

botonEnviar = Button(seccion2, text="LOGIN", fg="black", bg="white", command=lambda: validar_usuario(caja1, input2))
botonEnviar.configure(height=2, width=10)
botonEnviar.place(x=230, y=100, width=100, height=30)

ventana.mainloop()
