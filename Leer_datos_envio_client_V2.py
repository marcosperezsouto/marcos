#!/usr/bin/env python3

import json
import os
import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import time

payload = 0
litros_italia = 0
litros_camara2 = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)

totales = os.path.join(os.path.dirname(__file__), 'total_acumulados.json')

try:
    with open(totales, 'r') as cefrico_file:
        total_data = json.load(cefrico_file)
        total_italia = total_data.get('litros italia')
        total_camara2 = total_data.get('litros camara2')
        print(total_italia)
        print(total_camara2)
except:
    total_data = {}


while True:
    Pulso_24 = GPIO.input(24)
    P_italia = not Pulso_24
    Pulso_23 = GPIO.input(23)
    P_camara2 = not Pulso_23   

    def guardar_totales(fichero, datos):
        with open(fichero, 'w') as fichero_file:
            json.dump(datos, fichero_file, indent='  ')
 
    if P_italia:
        litros_italia = litros_italia + 50
        total_italia = total_italia + 50
        print(time.strftime("%d/%m/%Y-%H:%M"))
        print(litros_italia, 'litros italia')

        total_data['litros italia'] = total_italia
        guardar_totales(totales, total_data)
        time.sleep(1.8)
        
    if P_camara2:
        litros_camara2 = litros_camara2 + 250
        total_camara2 = total_camara2 + 250
        print(time.strftime("%d/%m/%Y-%H:%M"))
        print(litros_camara2, 'litros camara2')

        total_data['litros camara2'] = total_camara2
        guardar_totales(totales, total_data)
        time.sleep(1.8)

    minuto = time.strftime("%M:%S")

    if minuto in('00:00', '15:00', '30:00', '45:00'):
        hostname = "192.168.19.161"
        response = os.system("ping -c 1 " + hostname + " > /dev/null 2>&1") 
        if response == 0:
            if litros_italia != 0:            
                topic = "italia"
                payload = litros_italia
                broker_address="192.168.19.161"
                client = mqtt.Client('cefrico')
                client.connect(broker_address)
                print('Datos enviados')
                client.publish(topic, payload)
                payload = 0
                litros_italia = 0
            else:
                time.sleep(0.3)
            if litros_camara2 != 0:        
                topic = "camara2"
                payload = litros_camara2
                broker_address="192.168.19.161"
                client = mqtt.Client('cefrico')
                client.connect(broker_address)
                print('Datos enviados')
                client.publish(topic, payload)
                payload = 0
                litros_camara2 = 0
            else:
                time.sleep(0.3)
        else:
            time.sleep(0.3)
    time.sleep(0.3)
    

