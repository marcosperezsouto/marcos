#!/usr/bin/env python3

# Copia un archivo completo
# será creado y si existe será reemplazado. 
import time
import os
import shutil


while True:

    hora = time.strftime("%H:%M")

    if hora == '06:55':

        ruta = os.getcwd() + os.sep
        origen = "/home/pi/Desktop/italia.csv"
        destino = "/home/pi/Desktop/archivos_registrados/italia.csv"

        if os.path.exists(origen):
            with open(origen, 'rb') as forigen:
                with open(destino, 'wb') as fdestino:
                    shutil.copyfileobj(forigen, fdestino)
                    print("Archivo copiado")


        ruta = os.getcwd() + os.sep
        origen = "/home/pi/Documents/italia.csv"
        destino = "/home/pi/Desktop/italia.csv"

        if os.path.exists(origen):
            with open(origen, 'rb') as forigen:
                with open(destino, 'wb') as fdestino:
                    shutil.copyfileobj(forigen, fdestino)
                    print("Archivo copiado")


# Para renombrar un archivo en Python 3 sólo debes usar la función rename del módulo.

        dia = time.strftime("%d-%m-%Y")

        ubicacion = "/home/pi/Desktop/archivos_registrados/italia"
        extension = ".csv"

        nombre = ubicacion + dia + extension
        print(nombre)

        archivo = "/home/pi/Desktop/archivos_registrados/italia.csv"
        nombre_nuevo = nombre

        os.rename(archivo, nombre_nuevo)

        time.sleep(60.5)

    if hora == '06:56':

        ruta = os.getcwd() + os.sep
        origen = "/home/pi/Desktop/camara2.csv"
        destino = "/home/pi/Desktop/archivos_registrados/camara2.csv"

        if os.path.exists(origen):
            with open(origen, 'rb') as forigen:
                with open(destino, 'wb') as fdestino:
                    shutil.copyfileobj(forigen, fdestino)
                    print("Archivo copiado")


        ruta = os.getcwd() + os.sep
        origen = "/home/pi/Documents/camara2.csv"
        destino = "/home/pi/Desktop/camara2.csv"

        if os.path.exists(origen):
            with open(origen, 'rb') as forigen:
                with open(destino, 'wb') as fdestino:
                    shutil.copyfileobj(forigen, fdestino)
                    print("Archivo copiado")


# Para renombrar un archivo en Python 3 sólo debes usar la función rename del módulo.

        dia = time.strftime("%d-%m-%Y")

        ubicacion = "/home/pi/Desktop/archivos_registrados/camara2"
        extension = ".csv"

        nombre = ubicacion + dia + extension
        print(nombre)

        archivo = "/home/pi/Desktop/archivos_registrados/camara2.csv"
        nombre_nuevo = nombre

        os.rename(archivo, nombre_nuevo)

        time.sleep(60.5)


    if hora == '06:57':

        ruta = os.getcwd() + os.sep
        origen = "/home/pi/Desktop/lavadora_1.csv"
        destino = "/home/pi/Desktop/archivos_registrados/lavadora_1.csv"

        if os.path.exists(origen):
            with open(origen, 'rb') as forigen:
                with open(destino, 'wb') as fdestino:
                    shutil.copyfileobj(forigen, fdestino)
                    print("Archivo copiado")


        ruta = os.getcwd() + os.sep
        origen = "/home/pi/Documents/lavadora_1.csv"
        destino = "/home/pi/Desktop/lavadora_1.csv"

        if os.path.exists(origen):
            with open(origen, 'rb') as forigen:
                with open(destino, 'wb') as fdestino:
                    shutil.copyfileobj(forigen, fdestino)
                    print("Archivo copiado")


# Para renombrar un archivo en Python 3 sólo debes usar la función rename del módulo.

        dia = time.strftime("%d-%m-%Y")

        ubicacion = "/home/pi/Desktop/archivos_registrados/lavadora_1"
        extension = ".csv"

        nombre = ubicacion + dia + extension
        print(nombre)

        archivo = "/home/pi/Desktop/archivos_registrados/lavadora_1.csv"
        nombre_nuevo = nombre

        os.rename(archivo, nombre_nuevo)

        time.sleep(60.5)


    if hora == '06:58':

        ruta = os.getcwd() + os.sep
        origen = "/home/pi/Desktop/lavadora_2.csv"
        destino = "/home/pi/Desktop/archivos_registrados/lavadora_2.csv"

        if os.path.exists(origen):
            with open(origen, 'rb') as forigen:
                with open(destino, 'wb') as fdestino:
                    shutil.copyfileobj(forigen, fdestino)
                    print("Archivo copiado")


        ruta = os.getcwd() + os.sep
        origen = "/home/pi/Documents/lavadora_2.csv"
        destino = "/home/pi/Desktop/lavadora_2.csv"

        if os.path.exists(origen):
            with open(origen, 'rb') as forigen:
                with open(destino, 'wb') as fdestino:
                    shutil.copyfileobj(forigen, fdestino)
                    print("Archivo copiado")


# Para renombrar un archivo en Python 3 sólo debes usar la función rename del módulo.

        dia = time.strftime("%d-%m-%Y")

        ubicacion = "/home/pi/Desktop/archivos_registrados/lavadora_2"
        extension = ".csv"

        nombre = ubicacion + dia + extension
        print(nombre)

        archivo = "/home/pi/Desktop/archivos_registrados/lavadora_2.csv"
        nombre_nuevo = nombre

        os.rename(archivo, nombre_nuevo)

        time.sleep(60.5)

    time.sleep(0.5)




