from datetime import datetime
class Reserva():
        # Constructor
        def __init__(self, informacion_del_prestatario): 
                self.__informacion_del_prestatario = informacion_del_prestatario
                self.__fecha = datetime.now().date()

        def set_fecha(self, informacion_del_prestatario):
                self.__informacion_del_prestatario = informacion_del_prestatario
        
        def get_fecha(self):
                return self.__informacion_del_prestatario

        def set_fecha(self, fecha):
                self.__fecha = fecha
        
        def get_fecha(self):
                return self.__fecha
        
        def __str__(self):
                return self.__fecha, self.__informacion_del_prestatario
        
        def crear(self):
                pass
        
        def destruir(self):
                pass
        
        def encontrar(self):
                pass