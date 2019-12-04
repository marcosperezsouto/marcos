
import paho.mqtt.client as mqtt
import time

print('Iniciando programa')
           
broker_address="10.0.0.153"
client = mqtt.Client('marcos')
client.connect(broker_address)

topic = "prueba"
payload = "hola"
client.publish(topic, payload)



