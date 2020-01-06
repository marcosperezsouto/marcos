import paho.mqtt.publish as publish
import RPi.GPIO as GPIO
import time
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--litros-pulso", help="litros por pulso",
                    type=int)
parser.add_argument("--pin", help="litros por pulso",
                    type=int, default=24)
args = parser.parse_args()

print("Usando litros pulso: " + str(args.litros_pulso))

litros_pulso = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    Pulso_cont_1 = GPIO.input(args.pin)
    P_C_1 = not Pulso_cont_1
        
    if P_C_1:
        litros_pulso = litros_pulso + args.litros_pulso
        print(time.strftime("%d/%m/%Y-%H:%M"))
        print(litros_pulso, 'litros')
        
    minuto = time.strftime("%M:%S")
    if minuto in('00:00', '15:00', '30:00', '45:00'):
        print('Datos enviados')
        publish.single("GPIO", litros_pulso, hostname="192.168.168.152")
        litros_pulso = 0
    
    time.sleep(1)
    


