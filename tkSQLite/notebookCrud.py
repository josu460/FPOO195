from tkinter import *
from tkinter import ttk
import tkinter as tk
import tkinter as messagebox
from Controlador import Controlador

objControlador= Controlador()
def ejecutarInsert():
    objControlador.insertUsuario(var1.get(),var2.get(),var3.get())

def busUsuario():
    usuarioBD=objControlador.buscarUsuario(varBus.get())
    if usuarioBD == []:
        messagebox.showwarning("nada", " ID no existe en la BD ")
    else:
        resultado_text.config(state="normal")
        resultado_text.delete(1.0, END)  # Limpiar el contenido anterior
        resultado_text.insert(END, usuarioBD)
        resultado_text.config(state="disabled")

Ventana= Tk()
Ventana.title("CRUD de usuarios")
Ventana.geometry("500x300")

#2 preparar el notebook para pestañas
panel= ttk.Notebook(Ventana)
panel.pack(fill='both', expand='yes')

#3 definir las pestañas del nootbook
pestana1= ttk.Frame(panel)
pestana2= ttk.Frame(panel)
pestana3= ttk.Frame(panel)
pestana4= ttk.Frame(panel)
pestana5= ttk.Frame(panel)


#4 agregamos las pestañas
panel.add(pestana1,text="Crear usuario")
panel.add(pestana2,text="Buscar usuario")
panel.add(pestana3,text="Consultar usuario")
panel.add(pestana4,text="Editar usuario")
panel.add(pestana5,text="Eliminar usuario")

#5 Pestaña 1: Formuladrio de insert
Label(pestana1, text="Registro de usuaios", fg="blue", font=("Modern",18)).pack()

var1= tk.StringVar()
Label(pestana1, text="Nombre: ").pack()
Entry(pestana1, textvariable=var1).pack()

var2= tk.StringVar()
Label(pestana1, text="Correo: ").pack()
Entry(pestana1, textvariable=var2).pack()

var3= tk.StringVar()
Label(pestana1, text="Contraseña: ").pack()
Entry(pestana1, textvariable=var3).pack()

Button(pestana1, text= "Guardar usuario",command=ejecutarInsert).pack()
# Pestaña 6: Buscar usuario
Label(pestana2, text="Buscar Usuario", fg="red", font=("Mono",18)).pack()

varBus = tk.StringVar()
Label(pestana2, text="Id: ").pack()
Entry(pestana2, textvariable=varBus).pack()

Button(pestana2, text= "Buscar Usuario", command=busUsuario).pack()

Label(pestana2, text="registrado: ", fg="blue", font=("Mono",16)).pack()



resultado_text = Text(pestana2, height=5, width=52)
resultado_text.pack()


Ventana.mainloop()