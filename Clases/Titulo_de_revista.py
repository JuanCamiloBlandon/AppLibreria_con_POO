from Titulo import Titulo
class Titulo_de_revista(Titulo):
        # Constructor
        def __init__(self): 
                self.__tiempo_pendiete = 10

        def set_fecha(self, tiempo_pendiete):
                self.__tiempo_pendiete = tiempo_pendiete
        
        def get_fecha(self):
                return self.__tiempo_pendiete
        
        def __str__(self):
                return self.__tiempo_pendiete