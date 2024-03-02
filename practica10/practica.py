class Usuario:
    listausuarios = []
    def __init__(self,id,nombre,apllido_P,apellido_M,correo,contraseña):
        self.__id = id
        self.__nombre = nombre
        self.__apellido_P = apllido_P
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
    
    def setid(self,id):
        self.__id =id
    def setnombre(self,nombre):
        self.__nombre = nombre
    def setapellido_P(self,apellido_P):
        self.__apellido_P = apellido_P
    def setapellido_M(self,apellido_M):
        self.__apellido_M = apellido_M
    def setcorreo(self,correo):
        self.__correo = correo
    def setcontraseña(self,contraseña):
        self.__contraseña = contraseña
        
    #metodos del usuario
    
   
    #metodo para agregar
    def agregar_usuario(self):
        id = int(input("Introduce el id del usuario: "))
        nombre = input("Introduce el nombre del usuario: ")
        apellido_P = input("Introduce el apellido paterno del usuario: ")
        apellido_M = input("Introduce el apellido materno del usuario: ")
        correo = input("Introduce el correo del usuario: ")
        contraseña = input("Introduce la contraseña del usuario: ")
        usuarionuevo = Usuario(id,nombre,apellido_P,apellido_M,correo,contraseña)
        self.listausuarios.append(usuarionuevo)
        self.listausuarios[0].getid()
    
    #metodo para consultar
    def consultar_usuario(self):
        for usuario in self.listausuarios:
            print("ID: ",usuario.getid())
            print("Nombre: ",usuario.getnombre())
            print("Apellido Paterno: ",usuario.getapellido_P())
            print("Apellido Materno: ",usuario.getapellido_M())
            print("Correo: ",usuario.getcorreo())
            print("Contraseña: ",usuario.getcontraseña())
    
    #metodo para eliminar
    def eliminar_usuario(self):
        self.consultar_usuario()
        num=int(input("Introduce el ID del usuario que deseas eliminar: "))
        self.listausuarios.remove(self.listausuarios[num - 1])
    
    #metodo para modificar
    def modificar_usuario(self):
        self.consultar_usuario()
        pos = int(input("Ingrese el ID del usuario que quieres modificar: "))
        nombre = input("Ingrese el nuevo nombre: ")
        apellidoP = input("Ingrese el nuevo apellido paterno: ")
        apellidoM = input("Ingrese el nuevo apellido materno: ")
        correo = input("Ingrese el nuevo correo: ")
        contraseña = input("Ingrese la nueva contraseña: ")
        self.listausuarios[pos- 1].setnombre(nombre)
        self.listausuarios[pos - 1].setapellido_P(apellidoP)
        self.listausuarios[pos -1 ].setapellido_M(apellidoM)
        self.listausuarios[pos - 1].setcorreo(correo)
        self.listausuarios[pos - 1].setcontraseña(contraseña)
        