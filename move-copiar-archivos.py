# Copia un archivo completo
# La función shutil.copyfileobj() copia el contenido completo de un archivo origen 
# (o sólo una parte del mismo) a un archivo destino. Si el archivo destino no existe 
# será creado y si existe será reemplazado. 

import shutil, os

ruta = os.getcwd() + os.sep
origen = "/home/decodigo/Documentos/python/archivos/origen.txt"
destino = "/home/decodigo/Documentos/python/archivos/destino.txt"

if os.path.exists(origen):
    with open(origen, 'rb') as forigen:
        with open(destino, 'wb') as fdestino:
            shutil.copyfileobj(forigen, fdestino)
            print("Archivo copiado")



# Mover un directorio y su contenido a otro directorio 
#  La función shutil.move() mueve un archivo o un directorio (y su contenido) 
# a otra ubicación y devuelve la ruta del nuevo destino.

#  shutil.move(src, dst, copy_function=copy2)

# El argumento opcional copy_function se utiliza indicar la función de copia a utilizar (copy2, copy) 
# en el caso de que no se use la función os.rename(). La función os.rename() la emplea shutil.move() 
# cuando un proceso se puede resolver con renombrar en lugar de copiar. 

import shutil, os

ruta = os.getcwd() + os.sep
origen = ruta + 'dir1'
destino = ruta + 'dir2'

if os.path.exists(origen):  
    ruta = shutil.move(origen, destino)
    print('El directorio ha sido movido a', ruta)
else:
    print('El directorio origen no existe')


# Para renombrar un archivo en Python 3 sólo debes usar la función rename del módulo.

import os

archivo = "/home/decodigo/Documentos/python/archivos/archivo.txt"
nombre_nuevo = "/home/decodigo/Documentos/python/archivos/archivo_renombrado.txt"

os.rename(archivo, nombre_nuevo)

# La función pide como parámetros la ruta completa del archivo y la ruta completa del archivo con el nuevo nombre.  
# Si existe un archivo con el mismo nombre, lo sobrescribirá.

