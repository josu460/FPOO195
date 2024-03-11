import tkinter

from main import Fraccion


ventana = tkinter.Tk()
ventana.title("Fracciones")
ventana.geometry("+400+180")


def click_sumar():
    Nfraccion1 = int(e_fraccion1.get())
    Dfraccion1 = int(e_fraccion1_D.get())
    Nfraccion2 = int(e_fraccion2.get())
    Dfraccion2 = int(e_fraccion2_D.get())
    
    fraccion1 = Fraccion(Nfraccion1, Dfraccion1)
    fraccion2 = Fraccion(Nfraccion2, Dfraccion2)
    
    resultado = fraccion1.sumar(fraccion2).simplificar()
    
    label_resultado['text'] = f"La suma es {resultado.getnumerador()}/{resultado.getdenominador()}"
    label_resultado.grid(row=7, column=0, columnspan=2)


def click_restar():
    Nfraccion1 = int(e_fraccion1.get())
    Dfraccion1 = int(e_fraccion1_D.get())
    Nfraccion2 = int(e_fraccion2.get())
    Dfraccion2 = int(e_fraccion2_D.get())
    
    fraccion1 = Fraccion(Nfraccion1, Dfraccion1)
    fraccion2 = Fraccion(Nfraccion2, Dfraccion2)
    
    resultado = fraccion1.restar(fraccion2).simplificar()
    label_resultado['text'] = f"La resta es {resultado.getnumerador()}/{resultado.getdenominador()}"
    label_resultado.grid(row=7, column=0, columnspan=2)   
    
def click_multiplicar():
    Nfraccion1 = int(e_fraccion1.get())
    Dfraccion1 = int(e_fraccion1_D.get())
    Nfraccion2 = int(e_fraccion2.get())
    Dfraccion2 = int(e_fraccion2_D.get())
    
    fraccion1 = Fraccion(Nfraccion1, Dfraccion1)
    fraccion2 = Fraccion(Nfraccion2, Dfraccion2)
    
    resultado = fraccion1.multiplicar(fraccion2).simplificar()
    label_resultado['text'] = f"La multiplicacion es {resultado.getnumerador()}/{resultado.getdenominador()}"
    label_resultado.grid(row=7, column=0, columnspan=2)   
    
def click_dividir():
    Nfraccion1 = int(e_fraccion1.get())
    Dfraccion1 = int(e_fraccion1_D.get())
    Nfraccion2 = int(e_fraccion2.get())
    Dfraccion2 = int(e_fraccion2_D.get())
    
    fraccion1 = Fraccion(Nfraccion1, Dfraccion1)
    fraccion2 = Fraccion(Nfraccion2, Dfraccion2)
    
    resultado = fraccion1.dividir(fraccion2).simplificar()
    label_resultado['text'] = f"La division es {resultado.getnumerador()}/{resultado.getdenominador()}"
    label_resultado.grid(row=7, column=0, columnspan=2)   
   
ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=1)


ventana.rowconfigure(0, weight=1)
ventana.rowconfigure(1, weight=1)



ventana.rowconfigure(2, weight=1)
ventana.rowconfigure(3, weight=1)
ventana.rowconfigure(4, weight=1)
ventana.rowconfigure(5, weight=1)
ventana.rowconfigure(6, weight=1)


label_titulo = tkinter.Label(ventana, text="Operaciones con fracciones", font=("Arial", 25))

label_fraccion1 = tkinter.Label(ventana, text="Fracción 1", font=("Arial", 12))

label_fraccion2 = tkinter.Label(ventana, text="Fracción 2", font=("Arial", 12))


e_fraccion1 = tkinter.Entry(ventana, font=("Arial", 15))
e_fraccion1_D = tkinter.Entry(ventana, font=("Arial", 15)) 

e_fraccion2 = tkinter.Entry(ventana, font=("Arial", 15))
e_fraccion2_D = tkinter.Entry(ventana, font=("Arial", 15))  

boton_suma = tkinter.Button(ventana, text="Sumar",bg="black",fg="white",font ="arial 12", width = 25, command=click_sumar)
boton_resta = tkinter.Button(ventana, text="Restar",bg="black",fg="white",font ="arial 12", width = 25 , command=click_restar)
boton_multiplicacion = tkinter.Button(ventana, text="Multiplicar",bg="black",fg="white",font ="arial 12", width = 25, command=click_multiplicar )
boton_division = tkinter.Button(ventana, text="Dividir",bg="black",fg="white",font ="arial 12", width = 25 , command=click_dividir)

boton_suma.grid(row=3, column=0, columnspan=2, pady=10)
boton_resta.grid(row=4, column=0, columnspan=2, pady=5)
boton_multiplicacion.grid(row=5, column=0, columnspan=2, pady=5)
boton_division.grid(row=6, column=0, columnspan=2, pady=5)

label_titulo.grid(row=0, column=0, columnspan=2, pady=8)


label_fraccion1.grid(row=1, column=0, pady=5)
label_fraccion2.grid(row=2, column=0)

e_fraccion1.grid(row=1, column=1, pady=8)
e_fraccion1_D.grid(row=1, column=2, pady=8)  # Posicionamiento del nuevo Entry

e_fraccion2.grid(row=2, column=1)
e_fraccion2_D.grid(row=2, column=2)  # Posicionamiento del nuevo Entry


label_resultado = tkinter.Label(ventana)

ventana.mainloop()
