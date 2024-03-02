class Personaje:
    # Atributos del perosnaje de halo 
    
    #declaramosm al connductor para crear los objetos
    def __init__(self,esp,nom,alt):
        self.__especie = esp
        self.__nombre = nom
        self.__altura = alt
  
    def get__especie(self):
        return self.__especie
    
    def get__nombre(self):
        return self.__nombre
    
    def get__altura(self):
        return self.__altura
    
    #Setters ( metodos Set)
    
    def set__especie(self, __especie):
        self._especie = __especie
    
    def set__nombre(self, __nombre):
        self.__nombre = __nombre
    
    def set__altura(self, __altura):
        self.__altura = __altura
        
    # Metodos del personaje de halo
    def correr(self,__estado):
        if(__estado):
            print("el personaje " + self.__nombre + " esta corriendo")
        else:
            print("el personaje " + self.__nombre + " esta muerto")
            
            #self para llamar los atributos de la clase
            
    def lanzarGranada(self):
        print(self.__nombre + " pego una granada")
        
    def __pensar(self):
        print(self.__nombre + " esta pensando")
