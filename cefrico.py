#!/usr/bin/env python3

import json
import os
import csv
import paho.mqtt.client as mqtt
import time

broker_address = "localhost"
broker_port = 1883
topics = ['italia', 'salaD', 'lavadora', 'prueba']

cefrico = os.path.join(os.path.dirname(__file__), 'cefrico.json')
print(cefrico)
cefrico2 = os.path.join(os.path.dirname(__file__), 'cefrico2.json')
print(cefrico2)
cefrico_csv = os.path.join(os.path.dirname(__file__), 'cefrico.csv')
print(cefrico_csv)

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

def on_connect(client, userdata, flags, rc):
    print("on connect"+str(rc))
    try:
        for topic in topics:
            client.subscribe(topic)
        print("subscribed")
    except:
        print("exception")


def on_message(client, userdata, msg):
    print(msg.topic)
    print(msg.payload)
   
    # generar topics en diccionario
    if not msg.topic in cefrico_data:
        cefrico_data[msg.topic] = {}
        print(cefrico_data)

    # guarda en diccionario datos topic y payload
    cefrico_data[msg.topic]['total'] = msg.payload
    cefrico_data[msg.topic]['fecha'] = time.strftime("%d/%m/%y-%H:%M")
    print(time.strftime("%d/%m/%y-%H:%M"))

    # guardar archivos
    guardar_fichero(cefrico2, cefrico_data)
    guardar_csv(cefrico_csv, cefrico_data)


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker_address, broker_port, 60)

client.loop_forever()













