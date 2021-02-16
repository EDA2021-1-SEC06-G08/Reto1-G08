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
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, 
una para los videos, otra para las categorias de los mismos.
"""

# Construccion de modelos


def newCatalog():
    """
    Inicializa el catálogo de videos. Crea una lista vacia para guardar todos los videos,
    adicionalmente, crea una lista vacia para las categorias. Retorna el catalogo inicializado.
    """
    catalog = {'videos':None,
                'categories':None}

    catalog['videos'] = lt.newList()
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
    t = newCategory(catalog['name'], catalog['id'])
    lt.addLast(catalog['catalog'], t)

# Funciones para creacion de datos

def newCategory(name):
    """
    Crea una nueva estructura para modelar los videos de
    una categoria y su promedio de ratings
    """
    category = {'name':'','id':''}
    category['name'] = name
    category['id'] = id
    return category

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

def comparecategories(name, category):
    return (name == category'name'])

# Funciones de ordenamiento