#!/usr/bin/env python3

import json
import os
import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import datetime
import time

payload = 0
litros_enfriadores = 0
#litros_prueba1 = 0
#litros_prueba2 = 0
#litros_prueba3 = 0
litros_pulso_enfriadores = 100
#litros_pulso_prueba1 = 10
#litros_pulso_prueba2 = 10
#litros_pulso_prueba3 = 10
ip_brocker = "192.168.19.161"

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_UP)

totales = os.path.join(os.path.dirname(__file__), 'acumulados_cocion.json')

try:
    with open(totales, 'r') as cefrico_file:
        total_data = json.load(cefrico_file)
        total_enfriadores = total_data.get('litros enfriadores')
#        total_prueba1 = total_data.get('litros prueba1')
#        total_prueba2 = total_data.get('litros prueba2')
#        total_prueba3 = total_data.get('litros prueba3')
        print(total_enfriadores)
#        print(total_prueba1)
#        print(total_prueba2)
#        print(total_prueba3)
except:
    total_data = {}


while True:
    Pulso_24 = GPIO.input(24)
    P_enfriadores = not Pulso_24
#    Pulso_23 = GPIO.input(23)
#    P_prueba1 = not Pulso_23  
#    Pulso_18 = GPIO.input(18)
#    P_prueba2 = not Pulso_18
#    Pulso_25 = GPIO.input(25)
#    P_prueba3 = not Pulso_25   

    def guardar_totales(fichero, datos):
        with open(fichero, 'w') as fichero_file:
            json.dump(datos, fichero_file, indent='  ')
 
    if P_enfriadores:
        litros_enfriadores = litros_enfriadores + litros_pulso_enfriadores
        total_enfriadores = total_enfriadores + litros_pulso_enfriadores
        print(time.strftime("%d/%m/%Y-%H:%M"))
        print(litros_enfriadores, 'litros enfriadores')
        total_data['litros enfriadores'] = total_enfriadores
        guardar_totales(totales, total_data)
        
#    if P_prueba1:
#        litros_prueba1 = litros_prueba1 + litros_pulso_prueba1
#        total_prueba1 = total_prueba1 + litros_pulso_prueba1
#        print(time.strftime("%d/%m/%Y-%H:%M"))
#        print(litros_prueba1, 'litros prueba1')
#        total_data['litros prueba1'] = total_prueba1
#        guardar_totales(totales, total_data)
              
#    if P_prueba2:
#        litros_prueba2 = litros_prueba2 + litros_pulso_prueba2
#        total_prueba2 = total_prueba2 + litros_pulso_prueba2
#        print(time.strftime("%d/%m/%Y-%H:%M"))
#        print(litros_prueba2, 'litros prueba2')
#        total_data['litros prueba2'] = total_prueba2
#        guardar_totales(totales, total_data)

#    if P_prueba3:
#        litros_prueba3 = litros_prueba3 + litros_pulso_prueba3
#        total_prueba3 = total_prueba3 + litros_pulso_prueba3
#        print(time.strftime("%d/%m/%Y-%H:%M"))
#        print(litros_prueba3, 'litros prueba3')
#        total_data['litros prueba3'] = total_prueba3
#        guardar_totales(totales, total_data)

    time.sleep(1.8)


    minuto = time.strftime("%M:%S")

    if minuto in("05:00", "20:00", "35:00", "53:00"):
        if litros_enfriadores != 0: 
            print('hola')          
            topic = "enfriadores"
            payload = litros_enfriadores
            broker_address="192.168.19.161"
            try:
                client = mqtt.Client('cefrico')
                client.connect(broker_address)
                client.publish(topic, payload)
                payload = 0
                litros_enfriadores = 0
                print('Datos enviados')
            except:
                print('no enviado')
                time.sleep(0.2)
#        if litros_prueba1 != 0:        
#            topic = "prueba1"
#            payload = litros_prueba1
#            broker_address="192.168.19.161"
#            try:
#                client = mqtt.Client('cefrico')
#                client.connect(broker_address)
#                client.publish(topic, payload)
#                payload = 0
#                litros_prueba1 = 0
#                print('Datos enviados')
#            except:
#                time.sleep(0.2)
#        if litros_prueba2 != 0:        
#            topic = "prueba2"
#            payload = litros_prueba2
#            broker_address="192.168.19.161"
#            try:
#                client = mqtt.Client('cefrico')
#                client.connect(broker_address)
#                client.publish(topic, payload)
#                payload = 0
#                litros_prueba2 = 0
#                print('Datos enviados')
#            except:
#                time.sleep(0.2)
#        if litros_prueba3 != 0:        
#            topic = "prueba3"
#            payload = litros_prueba3
#            broker_address="192.168.19.161"
#            try:
#                client = mqtt.Client('cefrico')
#                client.connect(broker_address)
#                client.publish(topic, payload)
#                payload = 0
#                litros_prueba3 = 0
#                print('Datos enviados')
#            except:
#                time.sleep(0.2)
        time.sleep(0.2)
    time.sleep(0.3)
    

