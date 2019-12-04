import paho.mqtt.client as mqtt 

broker_address = "localhost"
broker_port = 1883
topic = "prueba"

def on_connect(client, userdata, flags, rc):
    print("on connect"+str(rc))
    try:
        client.subscribe(topic)
        print("subscribed")
    except:
        print("exception")

def on_message(client, userdata, msg):
    print(msg.topic)
    print(msg.payload)
    dato = msg.payload
    print(dato.decode("utf-8"))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker_address, broker_port, 60)

client.loop_forever()
