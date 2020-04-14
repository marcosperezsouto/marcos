
#!/usr/bin/env python3

import json
import os
import csv
import paho.mqtt.client as mqtt
import datetime

broker_address = "192.168.19.161"
broker_port = 1883
topics = ['italia', 'camara2', 'lavadora_1', 'lavadora_2']

cefrico = os.path.join(os.path.dirname(__file__), 'cefrico.json')
cefrico2 = os.path.join(os.path.dirname(__file__), 'cefrico2.json')
italia_csv = os.path.join(os.path.dirname(__file__), 'italia.csv')
camara2_csv = os.path.join(os.path.dirname(__file__), 'camara2.csv')
lavadora_1_csv = os.path.join(os.path.dirname(__file__), 'lavadora_1.csv')
lavadora_2_csv = os.path.join(os.path.dirname(__file__), 'lavadora_2.csv')

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
        
crear_csv(italia_csv, create_data)
crear_csv(camara2_csv, create_data)
crear_csv(lavadora_1_csv, create_data)
crear_csv(lavadora_2_csv, create_data)


def guardar_fichero(fichero, datos):
    with open(fichero, 'a') as fichero_file:
        json.dump(datos, fichero_file, indent='  ')


def csv_italia(fichero, datos):
    with open(fichero, 'a') as f:
        csv_file = csv.writer(f)
        for key in datos:
            csv_file.writerow([key, datos[key]['fecha'], datos[key]['hora'], datos[key]['litros']])  


def csv_camara2(fichero, datos):
    with open(fichero, 'a') as f:
        csv_file = csv.writer(f)
        for key in datos:
            csv_file.writerow([key, datos[key]['fecha'], datos[key]['hora'], datos[key]['litros']])  


def csv_lavadora_1(fichero, datos):
    with open(fichero, 'a') as f:
        csv_file = csv.writer(f)
        for key in datos:
            csv_file.writerow([key, datos[key]['fecha'], datos[key]['hora'], datos[key]['litros']])          

def csv_lavadora_2(fichero, datos):
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
    if topic=='italia':
        csv_italia(italia_csv, cefrico_data)
    elif topic=='camara2':
        csv_camara2(camara2_csv, cefrico_data)
    elif topic=='lavadora_1':
        csv_lavadora_1(lavadora_1_csv, cefrico_data)
    elif topic=='lavadora_2':
        csv_lavadora_2(lavadora_2_csv, cefrico_data)
    print('recibido')  

    

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message


client.connect(broker_address, broker_port, 60)

client.loop_forever()





