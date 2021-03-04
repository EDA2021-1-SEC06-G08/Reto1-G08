"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo.")
    print("2- Consultar videos en tendencia en un pais y por categoria.")
    print("3- Consultar video con mayor trending en un pais.")
    print("4- Consultar video con mayor trending por categoria.")
    print("5- Consultar los videos con mas vistas.")
    print("0- Salir del menu.")

def initCatalog_ARRAY_LIST():
    """
    Inicializa el catalogo de libros con el tipo ARRAY_LIST
    """
    return controller.initCatalog_ARRAY_LIST()

def initCatalog_SINGLE_LINKED():
    """
    Inicialzia el catalogo de libros con el tiepo SINGLE_LINKED
    """
    return controller.initCatalog_SINGLE_LINKED()

def loadData(catalog):
    """
    Carga los videos en la estructura de datos
    """
    controller.loadData(catalog)

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        regresar=True
        while regresar:
            type_list = input('Ingrese 0 si quiere que el tipo de representacion de la lista sea ARRAY_LIST o 1 si quiere que sea LINKED_LIST\n')
            if int(type_list[0]) == 0:
                print("Cargando información de los archivos ....")
                catalog = initCatalog_ARRAY_LIST()
                loadData(catalog)
                print('Videos cargados ' + str(lt.size(catalog['videos'])))
                print('Categorias cargadas ' + str(lt.size(catalog['categories'])))
                regresar=False
        
            elif int(type_list[0]) == 1:
                print("Cargando información de los archivos ....")
                catalog = initCatalog_SINGLE_LINKED()
                loadData(catalog)
                print('Videos cargados' + str(lt.size(catalog['videos'])))
                print('Categorias cargadas' + str(lt.size(catalog['categories'])))
                regresar=False
            else:
                print("Recuerde que es un numero entre 0 y 1")

    elif int(inputs[0]) == 2:
        regresar = True
        while regresar:
            ordenamiento = input('Seleccione 0 si quiere que el ordenamiento sea de tipo Merge, 1 si quiere que sea Quick\n')
            if int(ordenamiento[0]) == 0:
                size = input("Indique el tamanio de la muestra: ")
                result = controller.sortMergeVideo(catalog, int(size))
                if int(size) <= lt.size(catalog['videos']):
                    print("Para la muestra de", size, "elementos, el tiempo (mseg)es: '", str(result[0]))
                    regresar = False
                else:
                    print("Porfavor introduzca un numero menor que: " + str(lt.size(catalog['videos'])))
            elif int(ordenamiento[0]) == 1:
                size = input("Indique el tamanio de la muestra: ")
                result = controller.sortQuickVideo(catalog, int(size))
                if int(size) <= lt.size(catalog['videos']):
                    print("Para la muestra de", size, "elementos, el tiempo (mseg)es: '", str(result[0]))
                    regresar = False
                else:
                    print("Porfavor introduzca un numero menor que: " + str(lt.size(catalog['videos'])))
            else: 
                print('Porfavor recuerde que es un numero entre 0 y 2') 

    elif int(inputs[0] == 3):
        print("Cargando informacion de videos ...")

    elif int(inputs[0] == 4):
        print("Cargando informacion de videos ...")

    elif int(inputs[0] == 5):
        print("Cargando informacion de videos ...")
        
    else:
        sys.exit(0)
sys.exit(0)
