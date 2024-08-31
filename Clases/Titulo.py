titulos = []
class Titulo:
        # Constructor
        def __init__(self): 
                pass

        def set_nombre(self, nombre):
                self.__nombre = nombre

        def set_autor(self, autor):
                self.__autor = autor

        def set_isbn(self, isbn):
                self.__isbn = isbn

        def set_numero_de_reserva(self, numero_de_reserva):
                self.__numero_de_reserva = numero_de_reserva

        def get_nombre(self):
                return self.__nombre
        
        def get_autor(self):
                return self.__autor
        
        def get_isbn(self):
                return self.__isbn
        
        def get_numero_de_reserva(self):
                return self.__numero_de_reserva
        
        def __str__(self):
                return f"Nombre: {self.__nombre}, Autor: {self.__autor}, ISBN: {self.__isbn}, Número de Reserva: {self.__numero_de_reserva}"
        
        def crear(self):
                nombre = input("Ingresa el nombre del titulo: ")
                autor = input("Ingresa el nombre del autor: ")
                isbn = input("Ingresa el nombre del isbn: ")
                numero_de_reserva = input("Ingresa el nombre del numero de reserva: ")
                self.__nombre = nombre
                self.__autor = autor
                self.__isbn = isbn
                self.__numero_de_reserva = numero_de_reserva
                

        def destruir(self):
                pass

        
def imprimir_titulos():
        contador = 1
        for titulo in titulos:
                print("\n")
                print(f"Titulo #{contador}:")
                print(titulo)
                contador += 1   

def eliminar_titulo(titulo):
       titulos.remove(titulo)
        
def encontrar_titulos_sin_parametro():
    tituloBuscar = input("Ingresa el nombre del titulo que deseas buscar: ")
    for titulo in titulos:
        if titulo.get_nombre() == tituloBuscar:
            return titulo
    return "Titulo no encontrado"

def encontrar_titulos(tituloBuscar):
    for titulo in titulos:
        if titulo.get_nombre() == tituloBuscar:
            return titulo
    return "Titulo no encontrado"