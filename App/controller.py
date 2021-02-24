﻿"""
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
 """

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


# Inicialización del Catálogo de libros

def initCatalog_ARRAY_LIST():
    """
    Llama la funcion de inicializacion del catalogo del modelo en modo ARRA_LIST.
    """
    catalog = model.newCatalog_ARRAY_LIST()
    return catalog

def initCatalog_SINGLE_LINKED():
    """
    Llama la funcion de inicializacion del catalogo del modelo en modo SINGLE_LINKED.
    """
    catalog = model.newCatalog_SINGLE_LINKED()
    return catalog

    
# Funciones para la carga de datos

def loadData(catalog):
    """
    Carga los datos de los archivos y carga los datos en la 
    estructura datos
    """
    loadVideos(catalog)
    loadCategories(catalog)


def loadVideos(catalog):
    """
    Carga los videos del archivo. Por cada video se toma su categoria y por
    cada una de ellas, se crea en la lsita de categorias, a dicha categoria 
    una referencia al video que se esta procesando.
    """
    videosfile = cf.data_dir + 'videos-large.csv'
    input_file = csv.DictReader(open(videosfile), encoding= 'utf-8')
    for video in input_file:
        model.addVideo(catalog, video)

def loadCategories(catalog):
    """
    Carga todas las categorias del archivo y las agrega a la lista de categorias
    """
    categoriesfile = cf.data_dir + 'category-id.csv'
    input_file = csv.DictReader(open(categoriesfile))
    for category in input_file:
        model.addCategory(catalog, category)
        
# Funciones de ordenamiento

def sortSelectionVideo(catalog, size):
    """
    Ordena los videos por views
    """
    return model.sortSelectionVideos(catalog, size)

def sortInsertionVideo(catalog, size):
    """
    Ordena los videos por views
    """
    return model.sortInsertionVideos(catalog, size)

def sortShellVideo(catalog, size):
    """
    Ordena los videos por views
    """
    return model.sortShellVideos(catalog, size)
# Funciones de consulta sobre el catálogo
