prestatarios = []
prestatariosActivos = []
prestatariosInactivos = []
class Informacion_del_prestatario:
        # Constructor
        def __init__(self): 
                pass
        
        def set_nombre(self, nombre):
                self.__nombre = nombre

        def set_direcc(self, direcc):
                self.__direcc = direcc

        def set_estado(self, estado):
                self.__estado = estado

        def set_codigo(self, codigo):
                self.__codigo = codigo

        def get_nombre(self):
                return self.__nombre
        
        def get_direcc(self):
                return self.__direcc
        
        def get_estado(self):
                return self.__estado
        
        def get_codigo(self):
                return self.__codigo
        
        def __str__(self):                
                return f"Nombre: {self.__nombre} \nDirección: {self.__direcc}\nEstado: {self.__estado}\n"

        
        def encontrar(self):
                pass

        def crear(self):
                nombre = input("Ingresa el nombre del prestatario: ")
                direcc = input("Ingresa la dirección del prestatario: ")
                estado = "Activo"
                codigo = input("Ingresa un codigo para el prestatario: ")
                self.__nombre = nombre
                self.__direcc = direcc
                self.__estado = estado
                self.__codigo = codigo

        def destruir(self):
                pass

def eliminar_prestatario(prestatario):
        prestatarios.remove(prestatario)
        prestatariosActivos.remove(prestatario)
        prestatariosInactivos.remove(prestatario)

def imprimir_prestatarios_activos():
        for prestatario in prestatariosActivos:
                print(prestatario)

def imprimir_prestatarios_inactivos():
        for prestatario in prestatariosInactivos:
                print(prestatario)

def encontrar_prestatario_por_codigo(codigo):
        for prestatario in prestatarios:
                if prestatario.get_codigo() == codigo:
                        return prestatario
        return "Prestatario no encontrado"

def inhabilitar_prestatario_por_codigo(prestatario):
        prestatario.set_estado("Inactivo")