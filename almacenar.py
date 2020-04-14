
#!/usr/bin/env python3

import json
import os
import csv
import paho.mqtt.client as mqtt
import datetime
import time

broker_address = "192.168.19.161"
broker_port = 1883
topics = ['italia', 'salaD', 'lavadora', 'camara2']

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

create_data = {}

def crear_csv(fichero, datos):
    with open(fichero, 'w') as f:
        csv_create = csv.writer(f)
        csv_create.writerow(['contador', 'fecha', 'hora', 'litros'])
        
crear_csv(cefrico_csv, create_data)

def guardar_fichero(fichero, datos):
    with open(fichero, 'a') as fichero_file:
        json.dump(datos, fichero_file, indent='  ')


def guardar_csv(fichero, datos):
    with open(fichero, 'a') as f:
        csv_file = csv.writer(f)
        for key in datos:
            csv_file.writerow([key, datos[key]['fecha'], datos[key]['hora'], datos[key]['litros']])         


def on_connect(client, userdata, flags, rc):
    print("on connect"+str(rc))
    try:
        for topic in topics:
            client.subscribe(topic)
        print("subscribed")
    except:
        print("exception")

def on_message(client, userdata, msg):
    topic = msg.topic
    print(topic)
    dato = msg.payload
    totales = dato.decode("utf-8")
    # guarda en diccionario datos topic y payload
    # generar topics en diccionario
    # guardar archivos
    cefrico_data = {}
    if not topic in cefrico_data:
        cefrico_data[topic] = {}
        print(cefrico_data)


    fecha_str = datetime.date.today().isoformat()
    cefrico_data[topic]['fecha'] = fecha_str
    hora_str = time.strftime("%H:%M")
    cefrico_data[topic]['hora'] = hora_str
    cefrico_data[topic]['litros'] = totales
    print(cefrico_data)

    guardar_fichero(cefrico2, cefrico_data)
    guardar_csv(cefrico_csv, cefrico_data)
    print('recibido') 
    dato = 0 

    

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message


client.connect(broker_address, broker_port, 60)

client.loop_forever()





