#!/usr/bin/env python3

# Copia un archivo completo
# La función shutil.copyfileobj() copia el contenido completo de un archivo origen 
# (o sólo una parte del mismo) a un archivo destino. Si el archivo destino no existe 
# será creado y si existe será reemplazado. 

import shutil, os

ruta = os.getcwd() + os.sep
origen = "/home/marcos1984/Escritorio/cefrico.json"
destino = "/home/marcos1984/Documentos/cefrico.json"

if os.path.exists(origen):
    with open(origen, 'rb') as forigen:
        with open(destino, 'wb') as fdestino:
            shutil.copyfileobj(forigen, fdestino)
            print("Archivo copiado")


# Para renombrar un archivo en Python 3 sólo debes usar la función rename del módulo.

import os

archivo = "/home/marcos1984/Documentos/cefrico.json"
nombre_nuevo = "/home/marcos1984/Documentos/cefrico-pruebas.json"

os.rename(archivo, nombre_nuevo)

# La función pide como parámetros la ruta completa del archivo y la ruta completa del archivo con el nuevo nombre.  
# Si existe un archivo con el mismo nombre, lo sobrescribirá.

