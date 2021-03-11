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
import operator 
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

#Funciones requerimiento 3 

    """
    Crea una lista con los videos que tienen la categoría que entra por parametro. 
    """
def lista_categoria(catalog, category):
    categorylist = lt.newList('ARRAY_LIST')
    iterador = it.newIterator(catalog['videos'])
    while it.hasNext(iterador):
        elemento = it.next(iterador)
        if comparecategory_video(category, elemento, catalog) == 1:
            lt.addLast(categorylist,elemento)
    return categorylist

    """
    Crea un diccionario con los id de los paises de la categorylist y cuenta
    el número de apariciones del id para obtener el video mas trending 
    """
def creardiccionarioId(categorylist):
    dicc = {}
    iterador = it.newIterator(categorylist)
    while it.hasNext(iterador):
        elemento = it.next(iterador)
        id = elemento['video_id']
        if id not in dicc.keys():
            dicc[id] = 1
        else:
            dicc[id] += 1 
    max_id = max(dicc.items(),key=operator.itemgetter(1))[0]
    return max_id, dicc[max_id]

    """
    relaciona el video_id con los datos del video que tiene el id correspondiente 
    """
def buscar_id(catalog, id):
    datos = None
    iterador = it.newIterator(catalog['videos'])
    while it.hasNext(iterador):
        elemento = it.next(iterador)
        actual = elemento['video_id']
        if id == actual:
            datos = elemento 
            break
    return datos

    """
    relaciona la el id de la categoría con el nombre de la categoría
    """

def relacionar_id_categorias(category, catalog):
    nombre = ""
    iterador = it.newIterator(catalog['categories'])
    while it.hasNext(iterador):
        elemento = it.next(iterador)
        if category == elemento['id']:
            nombre = elemento['name']
            break
    return nombre

    """
    relaciona la categoría que entra por parametro con la categoría de cada video por su nombre 
    """

def comparecategory_video(category, video, catalog):
    relacion = relacionar_id_categorias(video['category_id'], catalog)
    if category == relacion:
        return 1

    """
    Obtiene el video mas trending teniendo en cuenta la categorylist, el video con mas apariciones de video_id
    y la relación entre el id obtenido con los datos del pais correspondiente. 
    """

def videomastrending(catalog, category):
    lista = lista_categoria(catalog, category)
    diccionario,dias = creardiccionarioId(lista)
    datos_video = buscar_id(catalog, diccionario)
    return datos_video['title'], datos_video['channel_title'], datos_video['category_id'], dias



#Funciones req 4 
    """
    Crea una lista con los videos que tienen el tag que entra por parametro. 
    """

def lista_tags(catalog, tag):
    taglist = lt.newList('ARRAY_LIST')
    iterador = it.newIterator(catalog['videos'])
    while it.hasNext(iterador):
        elemento = it.next(iterador)
        lista_tags = elemento['tags'].split("|")
        tag_entre_comillas = '"' + tag + '"'
        if tag_entre_comillas in lista_tags:
            lt.addLast(taglist, elemento)
    return taglist

    """
    Compara por likes, de mayor a menor 
    """
def shell_comparacion(elemento1, elemento2):
    return elemento1['likes'] > elemento2['likes']

    """
    Usa el ordenamiento shell para organizar los videos de taglist teniendo en
    cuenta los likes (de mayor a menor)
    """
def video_tag_mas_likes(catalog, tag):
    lst_tags = lista_tags(catalog, tag)
    lt.ordenamientoshell(lst_tags, shell_comparacion)
    return lst_tags 


def organizarCountryCategory(catalog, country, id):

    countryVideoList = lt.newList('ARRAY_LIST')
    iterador = it.newIterator(catalog['videos'])
    while it.hasNext(iterador):
        elemento = it.next(iterador)
        if compareCountryCategory(elemento,country, id) == 1:
            lt.addFirst(countryVideoList,elemento)
    return countryVideoList



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


#compara los datos por titulo
def comparetitle(video1, video2):
    return str((video1['title']) > str(video2['title']))
        
def compareCountryCategory(video, country, id):
    if country == video['country'] and id == video['category_id']:
        return 1

# Funciones de ordenamiento

def sortQuickVideos(compareCountryCategory, size):
    sub_list = lt.subList(compareCountryCategory, 0, size)
    sub_list = sub_list.copy()
    sorted_list = sa.sort(sub_list,cmpVideosByViews)
    return sorted_list

