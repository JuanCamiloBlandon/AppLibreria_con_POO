from Titulo import Titulo
class Titulo_del_libro(Titulo):
        # Constructor
        def __init__(self): 
                self.__tiempo_pendiente = 30

        def set_tiempo_pendiente(self, tiempo_pendiente):
                self.__tiempo_pendiente = tiempo_pendiente
        
        def get_tiempo_pendiente(self):
                return self.__tiempo_pendiente
        
        def __str__(self):
                return self.__tiempo_pendiente