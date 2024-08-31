class Persona:
        # Constructor
        def __init__(self, name, colorOjos, Altura, peso):
                #super.__init__():
                self.__name = name
                self.__colorOjos = colorOjos
                self.__Altura = Altura
                self.__peso = peso
                self.__caminarr = False
                self.__hablarr = False
        
        def getCaminar(self):
               return self.__caminarr
        
        def setCaminar(self, a=True):
               self.__caminarr = a

        def getHablar(self):
               return self.__hablarr
        
        def setHablar(self, a=True):
               self.__hablarr = a
        

persona1 = Persona("Juan Camilo", "Cafes", 1.70, 65)
persona1.setCaminar()

if(persona1.getCaminar()):
    print("La persona esta caminando")
else:
    print("La persona no esta caminando")

persona1.setCaminar(False)

if(persona1.getCaminar()):
    print("La persona esta caminando")
else:
    print("La persona no esta caminando")