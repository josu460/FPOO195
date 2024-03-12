from tkinter import *
from tkinter import ttk, messagebox
from main import Persona

def click_generar():
    nombre = caja1.get().upper()
    apellidoPaterno = caja2.get().upper()
    apellidoMaterno = caja3.get().upper()
    añoNacimiento = int(caja4.get())
    carrera = caja5.get().upper()
    
    persona = Persona(nombre, apellidoPaterno, apellidoMaterno, añoNacimiento, carrera)
    matricula = persona.generarMatricula()
    caja6.insert(0, matricula)
    messagebox.showinfo("Matrícula generada", matricula)
    
ventana = Tk()
ventana.title("Contraseña")
ventana.geometry("600x500")

seccion = Frame(ventana, bg="gray")
seccion.pack(expand=True, fill="both")

titulo = Label(seccion, text="Datos persona ", font=("Arial", 20))
titulo.place(x=200, y=10)

text = Label(seccion, text="Ingresa tu nombre", font=("Arial", 10))
text.place(x=200, y=60)
caja1 = ttk.Entry(seccion)
caja1.place(x=230, y=100, width=100, height=30)

text2 = Label(seccion, text="Ingresa tu apellido paterno", font=("Arial", 10))
text2.place(x=200, y=200)
caja2 = ttk.Entry(seccion)
caja2.place(x=230, y=250, width=100, height=30)

text3 = Label(seccion, text="Ingresa tu apellido materno", font=("Arial", 10))
text3.place(x=200, y=300)
caja3 = ttk.Entry(seccion)
caja3.place(x=230, y=350, width=100, height=30)


text4 = Label(seccion, text="Ingresa tu año de nacimiento", font=("Arial", 10))
text4.place(x=200, y=400)
caja4 = ttk.Entry(seccion)
caja4.place(x=230, y=450, width=100, height=30)

text5 = Label(seccion, text="Ingresa tu Carrera", font=("Arial", 10))
text5.place(x=200, y=500)
caja5 = ttk.Entry(seccion)
caja5.place(x=230, y=550, width=100, height=30)

botonGenerar = Button(seccion, text="Generar Matricula", fg="black", bg="white" , command=click_generar)
botonGenerar.configure(height=2, width=10)
botonGenerar.place(x=230, y=600, width=100, height=30)

text6 = Label(seccion, text="La matricula que se genero es ", font=("Arial", 10))
text6.place(x=200, y=650)
caja6 = ttk.Entry(seccion)
caja6.place(x=230, y=700, width=100, height=30)

ventana.mainloop()
