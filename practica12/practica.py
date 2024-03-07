class Usuario:
    _lista_usuarios = []

    def __init__(self, id, nombre, apellido_P, apellido_M, correo, contraseña):
        self.__id = id
        self.__nombre = nombre
        self.__apellido_P = apellido_P
        self.__apellido_M = apellido_M
        self.__correo = correo
        self.__contraseña = contraseña

    def getid(self):
        return self.__id

    def getnombre(self):
        return self.__nombre

    def getapellido_P(self):
        return self.__apellido_P

    def getapellido_M(self):
        return self.__apellido_M

    def getcorreo(self):
        return self.__correo

    def getcontraseña(self):
        return self.__contraseña

    def agregar_usuario(self):
        Usuario._lista_usuarios.append(self)

    def consultar_usuarios(self):
        for usuario in Usuario._lista_usuarios:
            print("ID: ", usuario.getid())
            print("Nombre: ", usuario.getnombre())
            print("Apellido Paterno: ", usuario.getapellido_P())
            print("Apellido Materno: ", usuario.getapellido_M())
            print("Correo: ", usuario.getcorreo())
            print("Contraseña: ", usuario.getcontraseña())

    def eliminar_usuario(self, id):
        for usuario in Usuario._lista_usuarios:
            if usuario.getid() == id:
                Usuario._lista_usuarios.remove(usuario)
                break

    def modificar_usuario(self, id, nombre, apellidoP, apellidoM, correo, contraseña):
        for usuario in Usuario._lista_usuarios:
            if usuario.getid() == id:
                usuario.__nombre = nombre
                usuario.__apellido_P = apellidoP
                usuario.__apellido_M = apellidoM
                usuario.__correo = correo
                usuario.__contraseña = contraseña
                break

    def validar_usuario(self, correo, contraseña):
        for usuario in Usuario._lista_usuarios:
            if usuario.getcorreo() == correo and usuario.getcontraseña() == contraseña:
                return True
        return False


opcion = ' '
while opcion != 'X':
    print("--------------USUARIOS--------------")
    print("A - Agregar usuario")
    print("M - Modificar usuario")
    print("E - Eliminar usuario")
    print("C - Consultar usuario")
    print("I - IR A LOGIN")
    print("X - Para salir")
    opcion = input("Selecciona una opción: ")
    if opcion =='X':
        print("Saliendo del programa")
    elif opcion == 'A':
        id = input("Introduce el id del usuario: ")
        nombre = input("Introduce el nombre del usuario: ")
        apellido_P = input("Introduce el apellido paterno del usuario: ")
        apellido_M = input("Introduce el apellido materno del usuario: ")
        correo = input("Introduce el correo del usuario: ")
        contraseña = input("Introduce la contraseña del usuario: ")
        usuarionuevo = Usuario(id, nombre, apellido_P, apellido_M, correo, contraseña)
        usuarionuevo.agregar_usuario()
        print("Usuario creado")
    elif opcion == 'C':
        print("------------Lista de usuarios------------")
        usuarionuevo = Usuario(None, None, None, None, None, None)
        usuarionuevo.consultar_usuarios()
    elif opcion == 'E':
        id_eliminar = input("Introduce el ID del usuario que deseas eliminar: ")
        usuarionuevo = Usuario(None, None, None, None, None, None)
        usuarionuevo.eliminar_usuario(id_eliminar)
        print("El usuario ha sido eliminado")
    elif opcion == 'M':
        id_modificar = input("Ingrese el ID del usuario que quieres modificar: ")
        nombre = input("Ingrese el nuevo nombre: ")
        apellidoP = input("Ingrese el nuevo apellido paterno: ")
        apellidoM = input("Ingrese el nuevo apellido materno: ")
        correo = input("Ingrese el nuevo correo: ")
        contraseña = input("Ingrese la nueva contraseña: ")
        usuarionuevo = Usuario(None, None, None, None, None, None)
        usuarionuevo.modificar_usuario(id_modificar, nombre, apellidoP, apellidoM, correo, contraseña)
        print("El usuario ha sido modificado")
    elif opcion == 'I':
        print("------------LOGIN------------")
        correo_login = input("Ingrese su correo: ")
        contraseña_login = input("Ingrese su contraseña: ")
        usuarionuevo = Usuario(None, None, None, None, None, None)
        if usuarionuevo.validar_usuario(correo_login, contraseña_login):
            print("Bienvenido")
        else:
            print("Acceso denegado")
    else:
        print("Opción no válida")
