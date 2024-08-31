from datetime import datetime
prestamos = []
class Prestamo:
        # Constructor
        def __init__(self): 
                pass

        def set_informacion_del_prestatario(self, informacion_del_prestatario):
                self.__informacion_del_prestatario = informacion_del_prestatario
        
        def get_informacion_del_prestatario(self):
                return self.__informacion_del_prestatario

        def set_fecha(self, fecha):
                self.__fecha = fecha
        
        def get_fecha(self):
                return self.__fecha
        
        def set_ejemplar(self, ejemplar):
                self.__ejemplar = ejemplar
        
        def get_ejemplar(self):
                return self.__ejemplar
        
        def __str__(self):
                return f"{self.get_ejemplar()} \n{self.get_informacion_del_prestatario()}\nFecha del prestamo: {self.get_fecha()}\n"
        
        def crear(self, ejemplar, informacion_del_prestatario):
                self.__ejemplar = ejemplar
                self.__informacion_del_prestatario = informacion_del_prestatario
                self.__fecha = datetime.now().date()
        
        def destruir(self):
                pass
        
        def encontrar(self):
                pass

def imprimir_prestamos():
        for prestamo in prestamos:
                print(prestamo)

def encontrar_prestamo_por_idEjemplar(idEjemplar):
        for prestamo in prestamos:
                if (prestamo.get_ejemplar()).get_id() == idEjemplar:
                        return prestamo
        return "No se encontro el prestamo"

def encontrar_prestamo_por_codigo_prestatario(prestatario):
        for prestamo in prestamos:
                if (prestamo.get_informacion_del_prestatario())== prestatario:
                        return prestamo
        return "No se encontro el prestamo"

def eliminar_prestamo(prestamo):
        prestamos.remove(prestamo)