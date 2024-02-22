class Personaje:
    # Atributos del perosnaje de halo 
    
    especie = "Humano"
    nombre = "John"
    altura = 2.18
    
    # Metodos del personaje de halo
    def correr(self,estado):
        if(estado):
            print("el personaje " + self.nombre + " esta corriendo")
        else:
            print("el personaje " + self.nombre + " esta muerto")
            
            #self para llamar los atributos de la clase
            
    def lanzarGranada(self):
        print(self.nombre + "pego una granada")
        
        
    def recargarArma(self,munucion):
        cargador = 25
        cargador= cargador +munucion
        print("arma recargada al "+ str(cargador) + "%")
     
# creamos el objeto de la clase personaje   
spartan = Personaje()

print(spartan.nombre)
print(spartan.especie)
print(spartan.altura)
