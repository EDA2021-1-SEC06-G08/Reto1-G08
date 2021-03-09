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
    print("1- Cargar información en el catálogo")
    print("2- Consultar videos en tendencia de un pais y en una categoria")
    print("3- Consultar video con mayor trending en un pais")
    print("4- Consultar video con mayor trending por categoria")
    print("5- Consultar los videos con mas vistas")
    print("0- Salir del menu")

def initCatalog_SingleList():
    """
    Inicializa el catalogo de libros con el tipo Single List
    """
    return controller.initCatalog_SingleList()

def loadData(catalog):
    """
    Carga los videos en la estructura de datos
    """
    controller.loadData(catalog)

def firstVideo(videos, sample):
    """
    Imprime el primer el video guardado
    """
    size = lt.size(videos)
    if size > sample:
        i=1
        while i <= sample:
            video = lt.getElement(videos,i)
            print('Primer video cargado: ' + video['title'])
            print('El nombre del canal: ' + video['channel_title'])
            print('Fecha de trending: ' + video['trending_date'])
            print('Pais de publicacion: ' + video['country'])
            print('Vistas: ' + video['views'])
            print('Likes: ' + video['likes'])
            print('Dislikes: ' + video['dislikes'])
            i+=1

def categoriesCargadas(categories):
    """
    Imprime las categorias cargadas
    """
    size = lt.size(categories)
    i=1
    print('Las categorias son: ')
    while i <= size:
        category = lt.getElement(categories,i)
        print(category['id'] + " " + category['name'])
        i+=1


def nCountryVideos(catalog, country, category):
    """
    Retorna la lista organizada por views
    """
    return controller.nCountryVideos(catalog, country, category)

def nOrganizador(videos, n):
    """
    retorna los n primeros videos
    """
    size = lt.size(videos)
    print('Los videos son: ')
    if size > n:
        i=0
        while i <= n:
            video = lt.getElement(videos, i)
            print('La fecha de trending es: ' + video['trending_date'])
            print('El titulo es: ' + video['title'])
            print('El canal es: ' + video['channel_title'])
            print('La fecha de publicacion es: ' + video['publish_time'])
            print('Las viewes son: ' + video['views'])
            print('Los likes son: ' + video['likes'])
            print('Los dislikes son: ' + video['dislikes'])
            i+=1

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalog = initCatalog_SingleList()
        loadData(catalog)
        print('Videos cargados ' + str(lt.size(catalog['videos'])))
        firstVideo(catalog['videos'],1)
        print('Categorias cargadas ' + str(lt.size(catalog['categories'])))
        categoriesCargadas(catalog['categories'])

    elif int(inputs[0]) == 2:
        
        pais = input("Introduzca un pais: ")
        categoria = input("Introduzca una categoria: ")
        print("Cargando informacion de los videos por pais y categoria...")
        videos = nCountryVideos(catalog, pais, categoria)
        size = lt.size(videos)
        video = controller.sortCountryVideos(videos, size)
        n = int(input("Introduzca la cantidad de videos: "))
        nOrganizador(video, n)

    elif int(inputs[0] == 3):
        
        print("Cargando informacion de videos ...")
        pais = input("Introduca un pais: ")

    elif int(inputs[0] == 4):
        print("Cargando informacion de videos ...")

    elif int(inputs[0] == 5):
        print("Cargando informacion de videos ...")
        
    else:
        sys.exit(0)
sys.exit(0)
