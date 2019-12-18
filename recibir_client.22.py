import paho.mqtt.client as mqtt 

broker_address = "192.168.1.136"
broker_port = 1883

topics = ['prueba', 'prueba2', 'prueba3']

def on_connect(client, userdata, flags, rc):
    print("on connect"+str(rc))
    try:
        for topic in topics:
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
