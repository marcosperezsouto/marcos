#!/usr/bin/env python3

import json
import os
import csv

topicos = [
  'italia',
  'salad',
]

cefrico = os.path.join(os.path.dirname(__file__), 'cefrico.json')
cefrico2 = os.path.join(os.path.dirname(__file__), 'cefrico2.json')
cefrico_csv = os.path.join(os.path.dirname(__file__), 'cefrico.csv')

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
    

for topic in topicos:
    subscribe.callback(mi_function)

client_loop()

topico_salad = 'salad'
salad_total = 100


topico_italia = 'italia'
italia_total = 200

topico_salad_data = {}
topico_italia_data = {}

cefrico_data = {}

if not topico_salad in cefrico_data:
    cefrico_data[topico_salad] = {}

cefrico_data[topico_salad]['total'] = salad_total
cefrico_data[topico_salad]['fecha-total'] = salad_total
cefrico_data[topico_italia] = topico_italia_data


topico_salad_data['total'] = 50
topico_italia_data['marcos'] = 100
topico_italia_data['total'] = 100

topico_salad_data['total'] = 100

topico_salad_data['nacho'] = 10

guardar_fichero(cefrico2, cefrico_data)
guardar_csv(cefrico_csv, cefrico_data)

with open(cefrico, 'r') as cefrico_file:
    cefrico_json = json.load(cefrico_file)
    print(cefrico_json)
