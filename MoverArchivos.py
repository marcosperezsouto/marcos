#!/usr/bin/env python3

# Copia un archivo completo
# será creado y si existe será reemplazado. 
import time
import os
import shutil


while True:

    hora = time.strftime("%H:%M")

    if hora == '06:50':

        ruta = os.getcwd() + os.sep
        origen = "/home/marcos1984/Escritorio/italia.csv"
        destino = "/home/marcos1984/Documentos/italia.csv"

        if os.path.exists(origen):
            with open(origen, 'rb') as forigen:
                with open(destino, 'wb') as fdestino:
                    shutil.copyfileobj(forigen, fdestino)
                    print("Archivo copiado")


        ruta = os.getcwd() + os.sep
        origen = "/home/marcos1984/Downloads/italia.csv"
        destino = "/home/marcos1984/Escritorio/italia.csv"

        if os.path.exists(origen):
            with open(origen, 'rb') as forigen:
                with open(destino, 'wb') as fdestino:
                    shutil.copyfileobj(forigen, fdestino)
                    print("Archivo copiado")


# Para renombrar un archivo en Python 3 sólo debes usar la función rename del módulo.

        dia = time.strftime("%d-%m-%Y")

        ubicacion = "/home/marcos1984/Documentos/italia"
        extension = ".csv"

        nombre = ubicacion + dia + extension
        print(nombre)

        archivo = "/home/marcos1984/Documentos/italia.csv"
        nombre_nuevo = nombre

        os.rename(archivo, nombre_nuevo)

    time.sleep(50)

    if hora == '06:52':

        ruta = os.getcwd() + os.sep
        origen = "/home/marcos1984/Escritorio/camara2.csv"
        destino = "/home/marcos1984/Documentos/camara2.csv"

        if os.path.exists(origen):
            with open(origen, 'rb') as forigen:
                with open(destino, 'wb') as fdestino:
                    shutil.copyfileobj(forigen, fdestino)
                    print("Archivo copiado")


        ruta = os.getcwd() + os.sep
        origen = "/home/marcos1984/Downloads/camara2.csv"
        destino = "/home/marcos1984/Escritorio/camara2.csv"

        if os.path.exists(origen):
            with open(origen, 'rb') as forigen:
                with open(destino, 'wb') as fdestino:
                    shutil.copyfileobj(forigen, fdestino)
                    print("Archivo copiado")


# Para renombrar un archivo en Python 3 sólo debes usar la función rename del módulo.

        dia = time.strftime("%d-%m-%Y")

        ubicacion = "/home/marcos1984/Documentos/camara2"
        extension = ".csv"

        nombre = ubicacion + dia + extension
        print(nombre)

        archivo = "/home/marcos1984/Documentos/camara2.csv"
        nombre_nuevo = nombre

        os.rename(archivo, nombre_nuevo)

    time.sleep(50)



