import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import time

topic = "prueba"
broker_address="localhost"
client = mqtt.Client('marcos')
client.connect(broker_address)
litros_pulso = 20

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    Pulso_cont_1 = GPIO.input(24)
    P_C_1 = not Pulso_cont_1
        
    if P_C_1:
        litros_pulso = litros_pulso + 50
        payload = litros_pulso
        print(time.strftime("%d/%m/%Y-%H:%M"))
        print(payload, 'litros')
        
    minuto = time.strftime("%M:%S")
    if minuto in('00:00', '15:00', '30:00', '45:00'):
        print('Datos enviados')
        client.publish(topic, payload)
        litros_pulso = 0
        time.sleep(1)
    time.sleep(0.2)
    



