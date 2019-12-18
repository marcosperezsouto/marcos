
import paho.mqtt.client as mqtt
import time

print('Iniciando programa')
           
broker_address="localhost"
client = mqtt.Client('italia')
client.connect(broker_address)

topic = "prueba"
payload = "152"
client.publish(topic, payload)



