class Armas:
    
    def seleccionar_arma(self,get__nombre):
        seleccion = int(input("Selecciona el arma: \n 1= Rifle de asalto \n 2=Espada de energia \n 3=Rifle M392 \n"))
        
        if (seleccion == 1):
            print("Rifle de asalto asignado a " + get__nombre)
            print("Municiones: 7.62 * 53mm , sin mira")
            
        if (seleccion == 2):
            print("Espada de energía asignada a " + get__nombre)
            print("Arma creada por los Sangheili")
        
        if (seleccion == 3):
            print("Rifle M392 asignado a " + get__nombre)
            print("Municiones: 7.62 * 53mm , con mira")
             
    #metodos armas
    def recargarArma(self,munucion):
        cargador = 25
        cargador= cargador +munucion
        print("arma recargada al "+ str(cargador) + "%")
     
