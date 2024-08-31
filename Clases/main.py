from Titulo import Titulo, encontrar_titulos,encontrar_titulos_sin_parametro, imprimir_titulos,eliminar_titulo, titulos
from Ejemplar import Ejemplar, imprimir_ejemplares, imprimir_ejemplares_disponibles, encontrar_ejemplar_por_Id, encontrar_ejemplares_por_titulo,eliminar_ejemplar,imprimir_ejemplares_por_lista,ejemplares, ejemplaresDisponibles,encontrar_ejemplares_dispnibles_por_titulo
from Prestamo import Prestamo, prestamos, encontrar_prestamo_por_idEjemplar,encontrar_prestamo_por_codigo_prestatario, eliminar_prestamo, imprimir_prestamos
from Informacion_del_prestatario import Informacion_del_prestatario, prestatarios, prestatariosInactivos, prestatariosActivos, inhabilitar_prestatario_por_codigo, imprimir_prestatarios_activos, imprimir_prestatarios_inactivos,eliminar_prestatario,   encontrar_prestatario_por_codigo

continuar = "si"
while(continuar == "si"):
        print("\n")
        print("__________________________MENU__________________________")
        print("1.  Crear titulos")
        print("2.  Crear ejemplar de titulos")
        print("3.  Registrar información de prestatario")
        print("4.  Prestar un ejemplar")
        print("5.  Eliminar titulo")
        print("6.  Eliminar ejemplar")
        print("7.  Eliminar prestamo por código")
        print("8.  Eliminar prestatario por código")
        print("9. Inhabilitar prestatario")
        print("10. Buscar titulos por nombre")
        print("11. Buscar ejemplares disponibles por titulo")
        print("12. Buscar total de ejemplares por titulo")
        print("13. Imprimir todos los titulos")
        print("14. Imprimir todos los ejemplares")
        print("15. Imprimir todos los ejemplares disponibles")
        print("16. Imprimir todos los prestatarios activos")
        print("17. Imprimir todos los prestamos registrados")
        print("18. Imprimir todos los prestatarios inactivos")
        print("19. Salir")
        print("")
        opcion = int(input("Ingresa la opción que necesitas: "))
        print("")
        match opcion:
            case 1:
                seguir = "s"
                while(seguir == "s"):
                    titulo = Titulo()
                    titulo.crear()
                    titulos.append(titulo)
                    seguir = input("\nDesea crear otro Titulo (s/n): ")
                print("\n")
            case 2:
                seguir = "s"
                while(seguir == "s"):
                    imprimir_titulos()
                    titulo = "Titulo no encontrado"
                    while(titulo == "Titulo no encontrado"):
                        nombreTitulo = input("\nIngresa el nombre del titulo del cual deseas crear el ejemplar: ")
                        titulo = encontrar_titulos(nombreTitulo)
                        if(titulo == "Titulo no encontrado"):
                            print(titulo)
                            print("Escribe el nombre de un titulo que si exista")
                        else:
                            break
                    while(True):
                        idEjemplar = int(input("Ingresa el id del ejemplar que deseas crear: "))
                        if(encontrar_ejemplar_por_Id(idEjemplar) == "Ejemplar no encontrado"):
                            nuevoEjemplar = Ejemplar()
                            nuevoEjemplar.crear(titulo, idEjemplar)
                            ejemplares.append(nuevoEjemplar)
                            ejemplaresDisponibles.append(nuevoEjemplar)
                            print("Ejemplar creado exitosamente")
                            break
                            
                        else:
                            print("El id del ejemplar que has proporcianado ya existe, intenta con uno diferente")
                    seguir = input("Desea crear otro ejemplar (s/n): ")
                print("\n")
            case 3:
                prestatario = Informacion_del_prestatario()
                prestatario.crear()
                prestatarios.append(prestatario)
                prestatariosActivos.append(prestatario)
                print("Prestatario creado con exito\n")
            case 4:
                seguir = "s"
                while(seguir == "s"):
                    while(True):
                        codigoPrestatario = input("Ingresa tu codigo de prestatario para continuar: ")
                        prestatario = encontrar_prestatario_por_codigo(codigoPrestatario)
                        if(prestatario != "Prestatario no encontrado"):
                            break                         
                        else:
                            print("El codigo de prestatario ingresado no existe, intenta con uno diferente")
                    imprimir_titulos()                            
                    while(True):
                        nombreTitulo = input("\nIngresa el titulo del ejemplar que deseas prestar: ")
                        listaEjemplaresDisponibles = encontrar_ejemplares_dispnibles_por_titulo(nombreTitulo)
                        if(len(listaEjemplaresDisponibles)>0):
                            break
                        else:
                            print("No se encontro ningun ejemplar disponible para el titulo proporcionado, intenta de nuevo")
                    imprimir_ejemplares_por_lista(listaEjemplaresDisponibles)
                    print(f"Ejemplares disponibles para este titulo: {len(ejemplaresDisponibles)}\n")
                    while(True):
                        idEjemplar = int(input("\nIngresa el ID del ejemplar que deseas prestar: "))
                        ejemplar = encontrar_ejemplar_por_Id(idEjemplar)
                        if(ejemplar != "Ejemplar no encontrado"):
                            prestamo = Prestamo()
                            prestamo.crear(ejemplar, prestatario)
                            prestamos.append(prestamo)
                            ejemplaresDisponibles.remove(ejemplar)
                            print("Ejemplar prestado con exito")
                            break

                        else:
                            print("\nNo se encontro ningun ejemplar para el titulo proporcionado, intenta de nuevo")

                    seguir = input("\nDesea prestar otro ejemplar (s/n): ")
            case 5:
                seguir = "s"
                while(seguir == "s"):
                    imprimir_titulos()
                    print(f"Total de titulos en inventario: {len(titulos)}")
                    while(True):
                        nombreTitulo = input("\nIngresa el nombre del titulo que deseas eliminar: ")
                        resultado = encontrar_titulos(nombreTitulo)
                        if(resultado == "Titulo no encontrado"):
                            print("El titulo que estas intentando eliminar no existe, intenta con otro titulo")
                        else: 
                            listaEjemplaresEliminar = encontrar_ejemplares_por_titulo(resultado.get_nombre())
                            confirmacion = input("Recuerda que al eliminar este titulo se borraran todos \nlos ejemplares del mismo en el inventario, deseas continuar (s/n): ")
                            if(confirmacion == "s"):
                                for ejemplar in listaEjemplaresEliminar:
                                        eliminar_ejemplar(ejemplar)
                                        break
                                eliminar_titulo(resultado)
                                print("Titulo eliminado con exito")
                                break
                            break
                    seguir = input("\nDesea eliminar otro ejemplar (s/n): ")
            case 6:
                seguir = "s"
                while(seguir == "s"):
                    print("\n")
                    imprimir_ejemplares_disponibles()
                    print(f"Total de ejemplares disponibles en inventario: {len(ejemplaresDisponibles)}")
                    while(True):
                        idEjemplar = int(input("\nIngresa el ID del ejemplar que deseas eliminar: "))
                        resultado = encontrar_ejemplar_por_Id(idEjemplar)
                        if(resultado == "Ejemplar no encontrado"):
                            print("El ejemplar que estas intentando eliminar no existe, intenta con un ID diferente")
                        else: 
                            eliminar_ejemplar(resultado)
                            resultado2 = encontrar_prestamo_por_idEjemplar(idEjemplar)
                            if(resultado2 != "No se encontro el prestamo"):
                                eliminar_prestamo(resultado2)
                            print("Ejemplar eliminado con exito")
                            break
                    seguir = input("\nDesea eliminar otro ejemplar (s/n): ")
            
            case 7:
                seguir = "s"
                while(seguir == "s"):
                    print("\n")
                    while(True):
                        codigoPrestatario = int(input("\nIngresa el codigo del prestatario del cual deseas eliminar un prestamo: "))
                        resultado = encontrar_prestatario_por_codigo(codigoPrestatario)
                        if(resultado == "Prestatario no encontrado"):
                            print("El codigo del prestatario suministrado no existe, intenta con uno nuevo")
                        else: 
                            resultado2 = encontrar_prestamo_por_codigo_prestatario(resultado)
                            if(resultado2 == "No se encontro el prestamo"):
                                print("El prestatario seleccionado no tiene ningun prestamo registrado")
                                break
                            else:
                                eliminar_prestamo(resultado2)
                                ejemplaresDisponibles.append(resultado2.get_ejemplar())
                                print("Prestamo eliminado con exito")
                    seguir = input("\nDesea eliminar otro prestatario (s/n): ")

            case 8:
                seguir = "s"
                while(seguir == "s"):
                    print("\n")
                    while(True):
                        codigoPrestatario = int(input("\nIngresa el codigo del prestatario que deseas eliminar: "))
                        resultado = encontrar_prestatario_por_codigo(codigoPrestatario)
                        if(resultado == "Prestatario no encontrado"):
                            print("El prestatario que estas intentando eliminar no existe, intenta con un codigo diferente")
                        else: 
                            resultado2 = encontrar_prestamo_por_codigo_prestatario(resultado)
                            if(resultado2 == "No se encontro el prestamo"):
                                eliminar_prestatario(resultado)
                                print("Prestatario eliminado con exito")
                                break
                            else:
                                print("La operación no se puede realizar debido a que el prestatario que intentas eliminar tiene prestamos activos")
                                break
                    seguir = input("\nDesea eliminar otro prestatario (s/n): ")


            case 9:
                seguir = "s"
                while(seguir == "s"):
                    print("\n")
                    while(True):
                        codigoPrestatario = input("\nIngresa el codigo del prestatario que deseas inhabilitar: ")
                        resultado = encontrar_prestatario_por_codigo(codigoPrestatario)
                        if(resultado == "Prestatario no encontrado"):
                            print("El prestatario que estas intentando inhabilitar no existe, intenta con un codigo diferente")
                        else: 
                            inhabilitar_prestatario_por_codigo(resultado)
                            prestatariosActivos.remove(prestatario)
                            prestatariosInactivos.append(prestatario)
                            print("Prestatario inhabilitado con exito")
                            break
                    seguir = input("\nDesea inhabilitar otro prestatario (s/n): ")

            case 10:
                seguir = "s"
                while(seguir == "s"):
                    resultado = encontrar_titulos_sin_parametro()
                    if(resultado != "Titulo no encontrado"):
                        print("Titulo encontrado")
                        print(resultado)
                    else:
                        print(resultado)
                    seguir = input("\nDesea buscar otro Titulo (s/n): ")
                print("\n")
            case 11:
                seguir = "s"
                while(seguir == "s"):
                    nombreTitulo = input("Ingresa el nombre del titulo de los ejemplares que quieres encontrar: ")
                    listaEjemplares = encontrar_ejemplares_dispnibles_por_titulo(nombreTitulo)
                    if(len(listaEjemplares)>0):
                        imprimir_ejemplares_por_lista(listaEjemplares)
                        print(f"\nCantidad de ejemplares disponibles para este titulo: {len(listaEjemplares)}")
                        print("")
                    else:
                        print("No se encontraron ejemplares por el titulo proporcionado")
                    seguir = input("\nDesea buscar otros ejemplares (s/n): ")
                    print("")
                print("\n")

            case 12:
                seguir = "s"
                while(seguir == "s"):
                    nombreTitulo = input("Ingresa el nombre del titulo de los ejemplares que quieres encontrar: ")
                    listaEjemplares = encontrar_ejemplares_por_titulo(nombreTitulo)
                    if(len(listaEjemplares)>0):
                        imprimir_ejemplares_por_lista(listaEjemplares)
                        print(f"\nCantidad de ejemplares para este titulo: {len(listaEjemplares)}")
                        print("")
                    else:
                        print("No se encontraron ejemplares por el titulo proporcionado")
                    seguir = input("\nDesea buscar otros ejemplares (s/n): ")
                    print("")
                print("\n")
                
                
            case 13:
                if(len(titulos)> 0):
                    imprimir_titulos()
                    print(f"\nTotal de titulos en inventario: {len(titulos)}")
                else:
                    print("No hay ningun titulo en inventario")

            case 14:
                if(len(ejemplares)> 0):
                    imprimir_ejemplares()
                    print(f"\nTotal de ejemplares en inventario: {len(ejemplares)}")
                else:
                    print("No hay ningun ejemplar en inventario")

            case 15:
                if(len(ejemplaresDisponibles)> 0):
                    imprimir_ejemplares_disponibles()
                    print(f"\nTotal de ejemplares disponibles en inventario: {len(ejemplaresDisponibles)}")
                else:
                    print("No hay ningun ejemplar disponible en inventario")

            case 16:
                if(len(prestatariosActivos)> 0):
                    imprimir_prestatarios_activos()
                    print(f"\nTotal de prestatarios activos: {len(prestatariosActivos)}")
                else:
                    print("No hay ningun prestatario activo a la fecha")

            case 17:
                if(len(prestamos)> 0):
                    imprimir_prestamos()
                    print(f"\nTotal de prestamos registrados es: {len(prestamos)}")
                else:
                    print("No hay ningun prestamo registrado a la fecha")
            case 18:
                if(len(prestatariosInactivos)> 0):
                    imprimir_prestatarios_inactivos()
                    print(f"\nTotal de prestatarios inactivos: {len(prestatariosInactivos)}")
                else:
                    print("No hay ningun prestatario inactivo a la fecha")
            
            case 19:
                break
            


            




