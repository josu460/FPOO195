import tkinter
from tkinter import messagebox
from cuenta import Cuenta

def ingresar_efectivo():
    num_cuenta = int(caja_num_cuenta.get())
    cantidad = float(caja1.get())
    if num_cuenta in cuentas:
        cuenta = cuentas[num_cuenta]
        cuenta.ingresar_efectivo(cantidad)
        messagebox.showinfo("Éxito", f'Se han ingresado {cantidad} pesos a la cuenta {num_cuenta}. Nuevo saldo: {cuenta.consultar_saldo()} pesos')
    else:
        messagebox.showerror("Error", "La cuenta especificada no existe")

def retirar_efectivo():
    num_cuenta = int(caja_num_cuenta.get())
    cantidad = float(caja1.get())
    if num_cuenta in cuentas:
        cuenta = cuentas[num_cuenta]
        mensaje = cuenta.retirar_efectivo(cantidad)
        messagebox.showinfo("Resultado", mensaje)
    else:
        messagebox.showerror("Error", "La cuenta especificada no existe")

def depositar_cuenta():
    num_cuenta_origen = int(caja_num_cuenta.get())
    num_cuenta_destino = int(caja2.get())
    cantidad = float(caja1.get())
    if num_cuenta_origen in cuentas and num_cuenta_destino in cuentas:
        cuenta_origen = cuentas[num_cuenta_origen]
        cuenta_destino = cuentas[num_cuenta_destino]
        mensaje = cuenta_origen.depositar_otra_cuenta(cuenta_destino, cantidad)
        messagebox.showinfo("Resultado", mensaje)
    else:
        messagebox.showerror("Error", "Una de las cuentas especificadas no existe")

def consultar_cuenta():
    num_cuenta = int(caja4.get())
    if num_cuenta in cuentas:
        saldo = cuentas[num_cuenta].consultar_saldo()
        titular = cuentas[num_cuenta].titular
        messagebox.showinfo("Consulta de Cuenta", f"El titular de la cuenta {num_cuenta} es: {titular}. El saldo de la cuenta es: {saldo} pesos.")
    else:
        messagebox.showerror("Error", "La cuenta especificada no existe")

def crear_usuario():
    ventana_creacion = tkinter.Toplevel(ventana)
    ventana_creacion.title("Crear nuevo usuario")

    label_nombre = tkinter.Label(ventana_creacion, text="Nombre de usuario", font=("Arial", 12))
    label_numero_cuenta = tkinter.Label(ventana_creacion, text="Número de cuenta", font=("Arial", 12))
    caja_nombre = tkinter.Entry(ventana_creacion, font=("Arial", 12))
    caja_numero_cuenta = tkinter.Entry(ventana_creacion, font=("Arial", 12))

    def guardar_usuario():
        nombre = caja_nombre.get()
        numero_cuenta = int(caja_numero_cuenta.get())
        nueva_cuenta = Cuenta(numero_cuenta, nombre, 0, 0)  
        cuentas[numero_cuenta] = nueva_cuenta
        messagebox.showinfo("Éxito", f"Usuario {nombre} creado con éxito")
        ventana_creacion.destroy()

    boton_guardar = tkinter.Button(ventana_creacion, text="Guardar", command=guardar_usuario)

    label_nombre.grid(row=0, column=0, padx=10, pady=5)
    label_numero_cuenta.grid(row=1, column=0, padx=10, pady=5)
    caja_nombre.grid(row=0, column=1, padx=10, pady=5)
    caja_numero_cuenta.grid(row=1, column=1, padx=10, pady=5)
    boton_guardar.grid(row=2, column=0, columnspan=2, pady=10)

cuentas = {}
cuenta_actual = None

ventana = tkinter.Tk()
ventana.title("Caja popular")
ventana.geometry("+400+180")

label_titulo = tkinter.Label(ventana, text="Caja popular", font=("Arial", 25))
label_caja1 = tkinter.Label(ventana, text="Cantidad", font=("Arial", 12))
label_caja2 = tkinter.Label(ventana, text="Número de cuenta destino", font=("Arial", 12))

label_caja4 = tkinter.Label(ventana, text="Número de cuenta a consultar", font=("Arial", 12))
label_num_cuenta = tkinter.Label(ventana, text="Número de cuenta", font=("Arial", 12))

caja1 = tkinter.Entry(ventana, font=("Arial", 15))
caja2 = tkinter.Entry(ventana, font=("Arial", 15))

caja4 = tkinter.Entry(ventana, font=("Arial", 15))
caja_num_cuenta = tkinter.Entry(ventana, font=("Arial", 15))

boton_ingresar = tkinter.Button(ventana, text="Ingresar efectivo", bg="black", fg="white", font="arial 12", width=25, command=ingresar_efectivo)
boton_retirar = tkinter.Button(ventana, text="Retirar", bg="black", fg="white", font="arial 12", width=25, command=retirar_efectivo)
boton_depositar = tkinter.Button(ventana, text="Depositar", bg="black", fg="white", font="arial 12", width=25, command=depositar_cuenta)
boton_consultar_cuenta = tkinter.Button(ventana, text="Consultar cuenta", bg="black", fg="white", font="arial 12", width=25, command=consultar_cuenta)
boton_crear_usuario = tkinter.Button(ventana, text="Crear usuario", bg="black", fg="white", font="arial 12", width=25, command=crear_usuario)

label_titulo.pack(pady=10)
label_num_cuenta.pack(pady=5)
caja_num_cuenta.pack(pady=5)
label_caja1.pack(pady=5)
caja1.pack(pady=5)
label_caja2.pack(pady=5)
caja2.pack(pady=5)

label_caja4.pack(pady=5)
caja4.pack(pady=5)
boton_ingresar.pack(pady=5)
boton_retirar.pack(pady=5)
boton_depositar.pack(pady=5)
boton_consultar_cuenta.pack(pady=5)
boton_crear_usuario.pack(pady=5)

ventana.mainloop()
