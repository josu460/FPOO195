from tkinter import *
from tkinter import ttk
import tkinter as tk
import tkinter as messagebox
from Controlador import *
from GeneradorPDF import *
import os


objPDF = GeneradorPDF()

objControlador= Controlador()
def ejecutarInsert():
    objControlador.insertUsuario(var1.get(),var2.get(),var3.get())
    consultarUsuario()

def busUsuario():
    usuarioBD=objControlador.buscarUsuario(varBus.get())
    if usuarioBD == []:
        messagebox.showwarning("nada", " ID no existe en la BD ")
    else:
        resultado.config(state="normal")
        resultado.delete(1.0, END)
        resultado.insert(END, usuarioBD)
        resultado.config(state="disabled")

def consultarUsuario():
    usuarios = objControlador.consultarUsuarios()
    resultado_consulta.delete(*resultado_consulta.get_children()) 
    for usuario in usuarios:
        resultado_consulta.insert('', 'end', values=usuario)
        
def ejecutaPdf():
    if varTitulo == "":
        messagebox.showwarning("Importante", "Escribe el titulo del PDF")
    else:
        objPDF.add_page()
        objPDF.chapter_body()
        objPDF.output(varTitulo.get()+".pdf")
        rutaPDF = "C:/Users/josuu/OneDrive/Documentos/POO/FPOO195/tkSQLite" + varTitulo.get()+".pdf"
        messagebox.showinfo("Archivo creado", "PDF disponible en carpeta: "+rutaPDF)
        os.system(f'start {rutaPDF}')
        # rutaPDF = "C:/Users/josuu/OneDrive/Documentos/POO/FPOO195/tkSQLite/GeneradorPDF.py"
        

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
pestana6= ttk.Frame(panel)

#4 agregamos las pestañas
panel.add(pestana1,text="Crear usuario")
panel.add(pestana2,text="Buscar usuario")
panel.add(pestana3,text="Consultar usuario")
panel.add(pestana4,text="Editar usuario")
panel.add(pestana5,text="Eliminar usuario")
panel.add(pestana6,text="Generar PDF")

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



resultado = Text(pestana2, height=5, width=52)
resultado.pack()

#PESTAÑA 7 : Consultar Usuario
Label(pestana3, text="Consultar Usuario", fg="red", font=("Mono",18)).pack()



resultado_consulta = ttk.Treeview(pestana3, columns=('ID', 'Nombre', 'Correo', 'Contraseña'), show='headings')
resultado_consulta.heading('ID', text='ID')
resultado_consulta.heading('Nombre', text='Nombre')
resultado_consulta.heading('Correo', text='Correo')
resultado_consulta.heading('Contraseña', text='Contraseña')
resultado_consulta.pack(fill='both', expand=True)


consultarUsuario()


#generar PDF

Label(pestana6, text="Usuario en PDF", fg="green", font=("Mono",18)).pack()

varTitulo = tk.StringVar()
Label(pestana6, text="Escribe el titulo del PDF: ").pack()
Entry(pestana6, textvariable=varTitulo).pack()

Button(pestana6, text= "Crear PDF", command=ejecutaPdf).pack()
Ventana.mainloop()
