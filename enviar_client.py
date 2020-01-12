
import paho.mqtt.client as mqtt
import time

print('Iniciando programa')
           
broker_address="localhost"
client = mqtt.Client('italia')
client.connect(broker_address)

topic = "salaD"
payload = "120"
client.publish(topic, payload)



