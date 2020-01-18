import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import time

payload = 0
litros_italia = 0
litros_camara2 = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    Pulso_24 = GPIO.input(24)
    P_italia = not Pulso_24
    Pulso_23 = GPIO.input(23)
    P_camara2 = not Pulso_23        

    if P_italia:
        litros_italia = litros_italia + 50
        print(time.strftime("%d/%m/%Y-%H:%M"))
        print(litros_italia, 'litros italia')
        
    if P_camara2:
        litros_camara2 = litros_camara2 + 250
        print(time.strftime("%d/%m/%Y-%H:%M"))
        print(litros_camara2, 'litros camara2')

    minuto = time.strftime("%M:%S")

    if minuto in('00:00', '15:00', '30:00', '45:00'):
        if litros_italia != 0:    
            topic = "italia"
            payload = litros_italia
            broker_address="localhost"
            client = mqtt.Client('cefrico')
            client.connect(broker_address)
            print('Datos enviados')
            client.publish(topic, payload)
            payload = 0
            litros_italia = 0

        if litros_camara2 != 0:
            topic = "camara2"
            payload = litros_camara2
            broker_address="localhost"
            client = mqtt.Client('cefrico')
            client.connect(broker_address)
            print('Datos enviados')
            client.publish(topic, payload)
            payload = 0
            litros_camara2 = 0

    time.sleep(0.3)
    



