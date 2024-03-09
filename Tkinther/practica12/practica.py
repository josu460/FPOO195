class Usuario:
    listausuarios = []

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

    def setid(self, id):
        self.__id = id

    def setnombre(self, nombre):
        self.__nombre = nombre

    def setapellido_P(self, apellido_P):
        self.__apellido_P = apellido_P

    def setapellido_M(self, apellido_M):
        self.__apellido_M = apellido_M

    def setcorreo(self, correo):
        self.__correo = correo

    def setcontraseña(self, contraseña):
        self.__contraseña = contraseña

    def agregar_usuario(self, usuario):
        self.listausuarios.append(usuario)

    def consultar_usuario(self):
        for usuario in self.listausuarios:
            print("ID: ", usuario.getid())
            print("Nombre: ", usuario.getnombre())
            print("Apellido Paterno: ", usuario.getapellido_P())
            print("Apellido Materno: ", usuario.getapellido_M())
            print("Correo: ", usuario.getcorreo())
            print("Contraseña: ", usuario.getcontraseña())

    def eliminar_usuario(self, id):
        for usuario in self.listausuarios:
            if usuario.getid() == id:
                self.listausuarios.remove(usuario)
                break

    def modificar_usuario(self, id, nombre, apellidoP, apellidoM, correo, contraseña):
        for usuario in self.listausuarios:
            if usuario.getid() == id:
                usuario.setnombre(nombre)
                usuario.setapellido_P(apellidoP)
                usuario.setapellido_M(apellidoM)
                usuario.setcorreo(correo)
                usuario.setcontraseña(contraseña)
    
    def validar_usuario(self, correo, contraseña):
        for usuario in self.listausuarios:
            if usuario['correo'] == correo and usuario['Pasw'] == contraseña:
                accesso=True
            else:
                accesso=False
        return accesso

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
        usuarionuevo.agregar_usuario(usuarionuevo)
        print("Usuario creado")
    elif opcion == 'C':
        print("------------Lista de usuarios------------")
        for usuario in Usuario.listausuarios:
            print("ID: ", usuario.getid())
            print("Nombre: ", usuario.getnombre())
            print("Apellido Paterno: ", usuario.getapellido_P())
            print("Apellido Materno: ", usuario.getapellido_M())
            print("Correo: ", usuario.getcorreo())
            print("Contraseña: ", usuario.getcontraseña())
    elif opcion == 'E':
        id_eliminar = input("Introduce el ID del usuario que deseas eliminar: ")
        Usuario.eliminar_usuario(id_eliminar)
        print("El usuario ha sido eliminado")
    elif opcion == 'M':
        id_modificar = input("Ingrese el ID del usuario que quieres modificar: ")
        nombre = input("Ingrese el nuevo nombre: ")
        apellidoP = input("Ingrese el nuevo apellido paterno: ")
        apellidoM = input("Ingrese el nuevo apellido materno: ")
        correo = input("Ingrese el nuevo correo: ")
        contraseña = input("Ingrese la nueva contraseña: ")
        Usuario.modificar_usuario(id_modificar, nombre, apellidoP, apellidoM, correo, contraseña)
        print("El usuario ha sido modificado")
    elif opcion == 'I':
        print("------------LOGIN------------")
        correo_login = input("Ingrese su correo: ")
        contraseña_login = input("Ingrese su contraseña: ")
        if Usuario.validar_usuario(correo_login, contraseña_login):
            print("Bienvenido")
        else:
            print("Acceso denegado")

    else:
        print("Opción no válida")
