#!/usr/bin/env python3

import json
import os
import csv
import paho.mqtt.client as mqtt
import datetime
import time

broker_address = "192.168.19.161"
broker_port = 1883
topics = ['enfriadores', 'prueba1', 'prueba2', 'prueba3']

cefrico = os.path.join(os.path.dirname(__file__), 'cefrico.json')
cefrico3 = os.path.join(os.path.dirname(__file__), 'cefrico3.json')
enfriadores_csv = os.path.join(os.path.dirname(__file__), 'enfriadores.csv')
#prueba1_csv = os.path.join(os.path.dirname(__file__), 'prueba1.csv')
#prueba2_csv = os.path.join(os.path.dirname(__file__), 'prueba2.csv')
#prueba3_csv = os.path.join(os.path.dirname(__file__), 'prueba3.csv')

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
        
crear_csv(enfriadores_csv, create_data)
#crear_csv(prueba1_csv, create_data)
#crear_csv(prueba2_csv, create_data)
#crear_csv(prueba3_csv, create_data)


def guardar_fichero(fichero, datos):
    with open(fichero, 'a') as fichero_file:
        json.dump(datos, fichero_file, indent='  ')


def csv_enfriadores(fichero, datos):
    with open(fichero, 'a') as f:
        csv_file = csv.writer(f)
        for key in datos:
            csv_file.writerow([key, datos[key]['fecha'], datos[key]['hora'], datos[key]['litros']])  


#def csv_prueba1(fichero, datos):
#    with open(fichero, 'a') as f:
#        csv_file = csv.writer(f)
#        for key in datos:
#            csv_file.writerow([key, datos[key]['fecha'], datos[key]['hora'], datos[key]['litros']])  


#def csv_prueba2(fichero, datos):
#    with open(fichero, 'a') as f:
#        csv_file = csv.writer(f)
#        for key in datos:
#            csv_file.writerow([key, datos[key]['fecha'], datos[key]['hora'], datos[key]['litros']])          

#def csv_prueba3(fichero, datos):
#    with open(fichero, 'a') as f:
#        csv_file = csv.writer(f)
#        for key in datos:
#            csv_file.writerow([key, datos[key]['fecha'], datos[key]['hora'], datos[key]['litros']])          

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

    guardar_fichero(cefrico3, cefrico_data)
    if topic=='enfriadores':
        csv_enfriadores(enfriadores_csv, cefrico_data)
#    elif topic=='prueba1':
#        csv_prueba1(prueba1_csv, cefrico_data)
#    elif topic=='prueba2':
#        csv_prueba2(prueba2_csv, cefrico_data)
#    elif topic=='prueba3':
#        csv_prueba3(prueba3_csv, cefrico_data)
    print('recibido')
    dato = 0

    

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message


client.connect(broker_address, broker_port, 60)

client.loop_forever()





