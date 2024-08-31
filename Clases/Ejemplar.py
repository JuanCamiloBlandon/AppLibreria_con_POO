ejemplares = []
ejemplaresDisponibles = []
class Ejemplar:
        # Constructor
        def __init__(self): 
                pass

        def set_id(self, id):
                self.__id = id

        def get_id(self):
                return self.__id
        

        def set_titulo(self, titulo):
                self.__titulo = titulo

        def get_titulo(self):
                return self.__titulo

        def __str__(self):
                return f"ID: {self.get_id()} \n{self.__titulo}"
        
        
        def crear(self, titulo, id):
                self.__titulo = titulo
                self.__id = id
        
        def destruir(self):
                pass

def imprimir_ejemplares():
        contador = 1
        for ejemplar in ejemplares:
                print("\n")
                titulo_nombre = (ejemplar.get_titulo()).get_nombre()
                print(f"Titulo: {titulo_nombre}")
                print(f"Ejemplar:")
                print(f"{ejemplar}")
                contador += 1 

def encontrar_ejemplares_dispnibles_por_titulo(tituloBuscar):
        ejemplares_por_titulo = []
        for ejemplar in ejemplaresDisponibles:
                if (ejemplar.get_titulo()).get_nombre() == tituloBuscar:
                        ejemplares_por_titulo.append(ejemplar)
        return ejemplares_por_titulo


def imprimir_ejemplares_disponibles():
        contador = 1
        for ejemplar in ejemplaresDisponibles:
                print("\n")
                titulo_nombre = (ejemplar.get_titulo()).get_nombre()
                print(f"Titulo: {titulo_nombre}")
                print(f"Ejemplar:")
                print(f"{ejemplar}")
                contador += 1 

def imprimir_ejemplares_por_lista(ejemplares):
        contador = 1
        for ejemplar in ejemplares:
                print("\n")
                titulo_nombre = (ejemplar.get_titulo()).get_nombre()
                print(f"Titulo: {titulo_nombre}")
                print(f"Ejemplar:")
                print(f"{ejemplar}")
                contador += 1 

def eliminar_ejemplar(ejemplar):
        ejemplares.remove(ejemplar)
        ejemplaresDisponibles.remove(ejemplar)

def encontrar_ejemplar_por_Id(id):
        for ejemplar in ejemplares:
                if(ejemplar.get_id() == id):
                        return ejemplar
        return "Ejemplar no encontrado"
        
def encontrar_ejemplares_por_titulo(tituloBuscar):
        ejemplares_por_titulo = []
        for ejemplar in ejemplares:
                if (ejemplar.get_titulo()).get_nombre() == tituloBuscar:
                        ejemplares_por_titulo.append(ejemplar)
        return ejemplares_por_titulo