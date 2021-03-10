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
from DISClib.Algorithms.Sorting import quicksort as sa
from DISClib.Algorithms.Sorting import mergesort as es
from DISClib.DataStructures import listiterator as it
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

def nCountryVideos(catalog, country, id):
    """
    Crea una lista con la informacion de los videos por pais y categoria
    """
    countryVideoList = lt.newList('ARRAY_LIST')
    iterador = it.newIterator(catalog['videos'])
    while it.hasNext(iterador):
        elemento = it.next(iterador)
        if compareCountryCategory(elemento,country, id) == 0:
            lt.addLast(countryVideoList,elemento)
    countryVideoList = sa.sort(countryVideoList, cmpVideosByViews)
    return countryVideoList

def organizarCountry(catalog, country):
    """
    Crea una lista con los videos por pais
    """
    countryVideoList = lt.newList('ARRAY_LIST', cmpfunction=compareTrendingCategory)
    iterador = it.newIterator(catalog['videos'])
    while it.hasNext(iterador):
        elemento = it.next(iterador)
        if compareCountry(elemento, country) == 0:
            lt.addLast(countryVideoList, elemento)
    countryVideoList = es.sort(countryVideoList,compareTitle)
    return countryVideoList

def organizarTrendingCategory(catalog, country):
    """
    dhhsgjs
    """
    videos = organizarCountry(catalog, country)
    diasValGrande = 0
    diasValPequenio = 0
    videoGrande = None
    videoPequenio = None
    videoAnterior = None
    iterador = it.newIterator(videos)
    while it.hasNext(iterador):
        elemento = it.next(iterador)
        title = elemento['title']
        if videoPequenio == None:
            videoPequenio = title
        elif title == videoPequenio:
            diasValPequenio += 1
        else:
            if diasValGrande < diasValPequenio:
                diasValGrande = diasValPequenio
                videoGrande = videoAnterior
            diasValPequenio = 1
            videoPequenio = title
        videoAnterior = elemento
    return videoGrande,diasValGrande
            

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
    return int(video1['views']) > int(video2['views'])

def compareCountryCategory(video, country, id):
    if country == video['country'] and id == video['category_id']:
        return 0

def compareCountry(video, country):
    if country == video['country']:
        return  0

<<<<<<< HEAD
def compareTrendingCategory(video1, video2):
    return str(video1['trending_date']) >= str(video2['trending_date']) and video1['title'] >= video2['title']

<<<<<<< HEAD
<<<<<<< HEAD
def sortQuickVideos(catalog, size):
    sub_list = lt.subList(catalog['videos'], 1, size)
=======
=======
>>>>>>> 50c248943fed75cfa9a54a73a935ffe77615e72e
def sortQuickVideos(compareCountryCategory, size):
    sub_list = lt.subList(compareCountryCategory, 0, size)
    sub_list = sub_list.copy()
    sorted_list = sa.sort(sub_list,cmpVideosByViews)
    return sorted_list
<<<<<<< HEAD
=======
def compareTitle(video, title):
    return title['title'] > video['title']

# Funciones de ordenamiento
>>>>>>> g.villabon
=======

    
>>>>>>> 50c248943fed75cfa9a54a73a935ffe77615e72e
