"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
import time
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.DataStructures import listiterator as it
from DISClib.Algorithms.Sorting import quicksort as qc
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, 
una para los videos, otra para las categorias de los mismos.
"""

# Construccion de modelos

def newCatalog_SingleList():
    """
    Inicializa el catálogo de videos. Crea una lista vacia para guardar todos los videos,
    adicionalmente, crea una lista vacia para las categorias. Retorna el catalogo inicializado.
    """
    catalog = {'videos':None,
                'categories':None}

    catalog['videos'] = lt.newList('SINGLE_LINKED',
                                       cmpfunction=cmpVideosByViews)
    catalog['categories'] = lt.newList('SINGLE_LINKED',
                                       cmpfunction=comparecategories)

    return catalog


# Funciones para agregar informacion al catalogo

def addVideo(catalog, video):
    # Se adiciona el video a la lista de videos
    lt.addLast(catalog['videos'],video)


def addCategory(catalog, category):
    """
    Adiciona la categoria a lista de categoria
    """
    t = newCategory(category['name'], category['id'])
    if lt.isPresent(catalog['categories'],t) == 0:
        lt.addLast(catalog['categories'], t)

# Funciones para creacion de datos

def newCategory(name, id):
    """
    Crea una nueva estructura para modelar las categorias 
    """
    category = {'name': '', 'id': ''}
    category['name'] = name
    category['id'] = id
    return category

# Funciones de consulta

def organizarCountryCategory(catalog, country, id):

    countryVideoList = lt.newList('ARRAY_LIST')
    iterador = it.newIterator(catalog['videos'])
    while it.hasNext(iterador):
        elemento = it.next(iterador)
        if compareCountryCategory(elemento,country, id) == 1:
            lt.addFirst(countryVideoList,elemento)
    return countryVideoList

def lista_categoria(catalog, category):
    categorylist = lt.newList('ARRAY_LIST')
    iterador = it.newIterator(catalog['videos'])
    while it.hasNext(iterador):
        elemento = it.next(iterador)
        if comparecategory_video(category, elemento) == 1:
            lt.addFirst(categorylist,elemento)
    return lista_categoria

# Funciones utilizadas para comparar elementos dentro de una lista

def comparecategories(name, category):
    if name == category:
        return 0

def cmpVideosByViews(video1, video2):
    """
    Devuelve verdadero (True) si los 'views' de video1 son menores que los del video2
     Args:
        video1: informacion del primer video que incluye su valor 'views'
        video2: informacion del segundo video que incluye su valor 'views'
    """
    if video1['views']<video2['views']:
        return -1
    elif video1['views']>video2['views']:
        return 1
    else:
        return 0
def comparecategory_video(category, video):
    if category == video["category_id"]:
        return 1
def comparetitle(video1, video2):
    if str((video1['title']) > str(video2['title'])):
        return 1 
    elif str((video1['title']) > str(video2['title'])):
        return -1 
    elif str((video1['title']) == str(video2['title'])):
        return 0



def compareCountryCategory(video, country, id):
    if country == video['country'] and id == video['category_id']:
        return 1

# Funciones de ordenamiento

def sortQuickVideos(compareCountryCategory, size):
    sub_list = lt.subList(compareCountryCategory, 0, size)
    sub_list = sub_list.copy()
    sorted_list = sa.sort(sub_list,cmpVideosByViews)
    return sorted_list

def sortQuicktitlte(catalog, category):
    sub_list = lista_categoria(catalog, category)
    sorted_list = qc.sort(sub_list, comparetitle(sub_list['title'],sub_list['title'])

    count = 0
    count_max = 0
    videomax = {} 
    basevideo = lt.firstElement(sorted_list)
    iterador = it.newIterator(sorted_list['videos'])
    while it.hasNext(iterador):
        elemento = it.next(iterador)
        tempvideo = lt.getElement(sorted_list, elemento)
        if tempvideo['title'] == basevideo ['title']:
            count = count + 1
            basevideo = tempvideo
            
            if count > count_max:
                count_max = count 
                videomax = tempvideo 
    return count, videomax