#!/usr/bin/env python3

import json
import os
import csv

cefrico = os.path.join(os.path.dirname(__file__), 'cefrico.json')
cefrico2 = os.path.join(os.path.dirname(__file__), 'cefrico2.json')
cefrico_csv = os.path.join(os.path.dirname(__file__), 'cefrico.csv')

try:
    with open(cefrico, 'r') as cefrico_file:
        cefrico_data = json.load(cefrico_file)
        print(cefrico_data)
except:
    # crea diccionario
    cefrico_data = {}

def guardar_fichero(fichero, datos):
    with open(fichero, 'w') as fichero_file:
        json.dump(datos, fichero_file, indent='  ')
        

def guardar_csv(fichero, datos):
    with open(fichero, 'w') as fichero_file:
        csv_file = csv.writer(fichero_file)
        csv_file.writerow(['nombre', 'total'])
        for key in datos:
            csv_file.writerow([key, datos[key]['total']])

def mi_funcion(....):
    msg.topic, msg.payload
    

# ejemplos datos "msg.payload"
topico_salad = 'salad'
salad_total = 100


topico_italia = 'italia'
italia_total = 200



# generar topics en diccionario
if not topico_salad in cefrico_data:
    cefrico_data["msg.topic"] = {}

# guarda en diccionario datos topic y payload
cefrico_data["msg.topic"]['total'] = "msg.payload"
cefrico_data[topico_salad]['fecha-total'] = salad_total


# guardar archivos
guardar_fichero(cefrico2, cefrico_data)
guardar_csv(cefrico_csv, cefrico_data)


