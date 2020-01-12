import paho.mqtt.client as mqtt 

broker_address = "10.0.0.150"
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
    topic = msg.topic
    dato = msg.payload
    print(topic) 
    print(dato.decode("utf-8"))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker_address, broker_port, 60)

client.loop_forever()
