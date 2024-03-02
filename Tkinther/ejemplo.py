from tkinter import Tk, Frame

#1. Creamos la ventana 

ventana = Tk() # USO DE POO creando un objeto ventana 
ventana.title("Ejemplo con 3 frames")
ventana.geometry("600x400")

#colocamos frames de la ventana 
seccion1 = Frame(ventana, bg="red")
seccion1.pack(expand=True, fill="both")

seccion2 = Frame(ventana, bg="yellow", )
seccion2.pack(expand=True, fill="both")

seccion3 = Frame(ventana,bg="green" )
seccion3.pack(expand=True, fill="both")

#ejecuta
ventana.mainloop()
