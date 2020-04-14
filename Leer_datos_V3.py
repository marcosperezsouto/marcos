#!/usr/bin/env python3

import json
import os
import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import time

payload = 0
litros_italia = 0
litros_camara2 = 0
litros_pulso_italia = 50
litros_pulso_camara2 = 250
litros_pulso_lavadora_1 = 10
litros_pulso_lavadora_2 = 10
ip_brocker = "192.168.19.161"

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_UP)

totales = os.path.join(os.path.dirname(__file__), 'total_acumulados.json')

try:
    with open(totales, 'r') as cefrico_file:
        total_data = json.load(cefrico_file)
        total_italia = total_data.get('litros italia')
        total_camara2 = total_data.get('litros camara2')
        total_lavadora_1 = total_data.get('litros lavadora_1')
        total_lavadora_2 = total_data.get('litros lavadora_2')
        print(total_italia)
        print(total_camara2)
        print(total_lavadora_1)
        print(total_lavadora_2)
except:
    total_data = {}


while True:
    Pulso_24 = GPIO.input(24)
    P_italia = not Pulso_24
    Pulso_23 = GPIO.input(23)
    P_camara2 = not Pulso_23  
    Pulso_18 = GPIO.input(18)
    P_lavadora_1 = not Pulso_18
    Pulso_25 = GPIO.input(25)
    P_lavadora_2 = not Pulso_25   

    def guardar_totales(fichero, datos):
        with open(fichero, 'w') as fichero_file:
            json.dump(datos, fichero_file, indent='  ')
 
    if P_italia:
        litros_italia = litros_italia + litros_pulso_italia
        total_italia = total_italia + litros_pulso_italia
        print(time.strftime("%d/%m/%Y-%H:%M"))
        print(litros_italia, 'litros italia')
        total_data['litros italia'] = total_italia
        guardar_totales(totales, total_data)
        time.sleep(1.8)
        
    if P_camara2:
        litros_camara2 = litros_camara2 + litros_pulso_camara2
        total_camara2 = total_camara2 + litros_pulso_camara2
        print(time.strftime("%d/%m/%Y-%H:%M"))
        print(litros_camara2, 'litros camara2')
        total_data['litros camara2'] = total_camara2
        guardar_totales(totales, total_data)
        time.sleep(1.8)
        
    if P_lavadora_1:
        litros_lavadora_1 = litros_lavadora_1 + litros_pulso_lavadora_1
        total_lavadora_1 = total_lavadora_1 + litros_pulso_lavadora_1
        print(time.strftime("%d/%m/%Y-%H:%M"))
        print(litros_lavadora_1, 'litros lavadora_1')
        total_data['litros lavadora_1'] = total_lavadora_1
        guardar_totales(totales, total_data)
        time.sleep(1.8)

    if P_lavadora_2:
        litros_lavadora_2 = litros_lavadora_2 + litros_pulso_lavadora_2
        total_lavadora_2 = total_lavadora_2 + litros_pulso_lavadora_2
        print(time.strftime("%d/%m/%Y-%H:%M"))
        print(litros_lavadora_2, 'litros lavadora_2')
        total_data['litros lavadora_2'] = total_lavadora_2
        guardar_totales(totales, total_data)
        time.sleep(1.8)


    minuto = time.strftime("%M:%S")

    if minuto in('00:00', '15:00', '30:00', '45:00'):
        if litros_italia != 0:           
            topic = "italia"
            payload = litros_italia
            broker_address=ip_broker
            try:
                client = mqtt.Client('cefrico')
                client.connect(broker_address)
                client.publish(topic, payload)
                payload = 0
                litros_italia = 0
                print('Datos enviados')
            except:
                time.sleep(0.2)
        if litros_camara2 != 0:        
            topic = "camara2"
            payload = litros_camara2
            broker_address=ip_broker
            try:
                client = mqtt.Client('cefrico')
                client.connect(broker_address)
                client.publish(topic, payload)
                payload = 0
                litros_camara2 = 0
                print('Datos enviados')
            except:
                time.sleep(0.2)
        if litros_lavadora_1 != 0:        
            topic = "lavadora_1"
            payload = litros_lavadora_1
            broker_address=ip_broker
            try:
                client = mqtt.Client('cefrico')
                client.connect(broker_address)
                client.publish(topic, payload)
                payload = 0
                litros_lavadora_1 = 0
                print('Datos enviados')
            except:
                time.sleep(0.2)
        if litros_lavadora_2 != 0:        
            topic = "lavadora_2"
            payload = litros_lavadora_2
            broker_address=ip_broker
            try:
                client = mqtt.Client('cefrico')
                client.connect(broker_address)
                client.publish(topic, payload)
                payload = 0
                litros_lavadora_2 = 0
                print('Datos enviados')
            except:
                time.sleep(0.2)
    time.sleep(0.3)
    

