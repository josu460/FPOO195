from tkinter import Tk, Frame, Button, messagebox

#metodos que vamos a utilizar (para mensaje)

def mostarMensajes():
    print(messagebox.showinfo('showinfo','Information'))
    print(messagebox.showerror('showerror','Error'))
    print(messagebox.showwarning('showwarning','Warning'))
    print(messagebox.askokcancel(message="Desea continuar", title="Soy el titulo"))
    
def addbtn():
    botonVerde.config(text="+")
    botonRosa = Button(seccion3,text="Nuevo", bg="#F7089c")
    botonRosa.configure(height=3,width=5)
    botonRosa.pack()

#1. Creamos la ventana 

ventana = Tk() # USO DE POO creando un objeto ventana 
ventana.title("Ejemplo con 3 frames")
ventana.geometry("600x400")

#colocamos frames de la ventana 
seccion1 = Frame(ventana, bg="red")
seccion1.pack(expand=True, fill="both")

seccion2 = Frame(ventana, bg="gray", )
seccion2.pack(expand=True, fill="both")
#bg = al color del fondo 
seccion3 = Frame(ventana,bg="black" )
seccion3.pack(expand=True, fill="both")

# Botones
#aqui es por cordenadas
botonAzul = Button(seccion1, text="Azul", fg="black")
botonAzul.place(x=80,y=75, width=100,height=30)

#grind
#Aqui se mueve por filas y columnas
botonNegro= Button(seccion2, text="Negro", fg="red", bg="green")
botonNegro.configure(height=2, width=10)
botonNegro.grid(row=0,column=1)


botonAmarillo = Button(seccion2,text="amarillo", bg="white", command=mostarMensajes)
botonAmarillo.configure(height=2,width=10)
botonAmarillo.grid(row=1,column=1)

#boton con pack 
#Aqui no se puede mover 
botonVerde = Button(seccion3,text="black", bg="green", command=addbtn)
botonVerde.configure(height=2,width=10)
botonVerde.pack()
#ejecuta
ventana.mainloop()
