import paho.mqtt.publish as publish
import RPi.GPIO as GPIO
import time


litros_pulso = 20

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    Pulso_cont_1 = GPIO.input(24)
    P_C_1 = not Pulso_cont_1
        
    if P_C_1:
        litros_pulso = litros_pulso + 50
        print(time.strftime("%d/%m/%Y-%H:%M"))
        print(litros_pulso, 'litros')
        
    minuto = time.strftime("%M:%S")
    if minuto in('00:00', '25:00', '30:00', '48:00'):
        print('Datos enviados')
        publish.single("GPIO", litros_pulso, hostname="localhost")
        litros_pulso = 0
        time.sleep(1)
    time.sleep(0.2)
    


