from practica import *



opcion = ' '
while(opcion != 'X'):
    print("--------------USUARIOS--------------")
    print("A - Agregar usuario")
    print("M - Modificar usuario")
    print("E - Eliminar usuario")
    print("C - Consultar usuario")
    print("X - Para salir")
    opcion = input("Selecciona una opción: ")
    if(opcion =='X'):
        print("Saliendo del programa")
    elif(opcion == 'A'):
        usuarionuevo = Usuario(None,None,None,None,None,None)
        usuarionuevo.agregar_usuario()
        print("  ")
        print("usuario creado")
    elif(opcion == 'C'):
        print("------------Lista de usuarios------------")
        usuarionuevo = Usuario(None,None,None,None,None,None)
        usuarionuevo.consultar_usuario()
    elif(opcion == 'E'):
        usuarionuevo= Usuario(None,None,None,None,None,None)
        usuarionuevo.eliminar_usuario()
        print("  ")
        print("El usuario ha sido eliminado")
    elif(opcion == 'M'):
        usuarionuevo = Usuario(None,None,None,None,None,None)
        usuarionuevo.modificar_usuario()
        print("  ")
        print("El usuario ha sido modificado")
    else:
        print("Opción no válida")