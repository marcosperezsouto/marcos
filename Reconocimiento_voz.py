# -*- coding: utf-8 -*-

import speech_recognition as sr  #importacion de librerias para o reconicimiento de voz
import _portaudio as r
 
r = sr.Recognizer() 

from opcua import Client   # importar librerias para a comunicacion, neste caso por opc
from opcua import ua

url = "opc.tcp://192.168.1.150:4840"   # crear conexion cliente-servidor
client = Client(url)
client.connect()

from gtts import gTTS
#import os
from playsound import playsound

while True: 
    with sr.Microphone() as source:
        print('Te escucho : ')
        audio = r.listen(source)     # poñer o micro en escucha
 
        try:
            text = r.recognize_google(audio, language="es-ES")  # traduce o audio que escoitou
            print('Digiste: {}'.format(text))
            
            Usuario = client.get_node('ns=4; i=5')    # envia o texto a variable designada no PLC, en vez destas 3 lineas,
            Us = ua.DataValue(ua.Variant(text, ua.VariantType.String))  # podese implementar calquera tipo de comunicacion
            Usuario.set_data_value(Us)  # ou grabar o texto nun archivo q despios o lee no nodeRed e envialo o PLC
            
            comparacion = ('dime el estado de las entradas'==text)
            if comparacion == True:
                Entrada00 = client.get_node('ns=4; i=19')
                Entrada00 = Entrada00.get_value()
                texto1 = int(Entrada00) 

                Entrada01 = client.get_node('ns=4; i=20')
                Entrada01 = Entrada01.get_value()
                texto2 = int(Entrada01)

                Entrada02 = client.get_node('ns=4; i=21')
                Entrada02 = Entrada02.get_value()
                texto3 = int(Entrada02)

                Entrada03 = client.get_node('ns=4; i=22')
                Entrada03 = Entrada03.get_value()
                texto4 = int(Entrada03)
                
                Entrada04 = client.get_node('ns=4; i=23')
                Entrada04 = Entrada04.get_value()
                texto5 = int(Entrada04)
                
                Entrada05 = client.get_node('ns=4; i=24')
                Entrada05 = Entrada05.get_value()
                texto6 = int(Entrada05)


                texto = "la entrada 1 es" + str(texto1) + "la entrada 2 es" + str(texto2)+ "la entrada 3 es" + str(texto3) + " la entrada 4 es" + str(texto4) + "la entrada 5 es" + str(texto5) + " la entrada 6 es" + str(texto6)


                lenguaje = 'es-ES'

                audio = gTTS(text = texto, lang = lenguaje, slow = True)
                audio.save('prueba.mp3')
                #os.system('prueba.mp3')
                playsound('prueba.mp3')
            else:
                print('adios')
        except:
            print('No te entiendo')
 
'''    
    Voz = client.get_node('ns=4; i=5')
    Vz = ua.DataValue(ua.Variant('desactiva salida 3', ua.VariantType.String))
    Voz.set_data_value(Vz)


    Usuario = client.get_node('ns=4; i=3')
    Us = ua.DataValue(ua.Variant('marcos', ua.VariantType.String))
    Usuario.set_data_value(Us)

    Entrada00 = client.get_node('ns=4; i=19')
    Entrada00 = Entrada00.get_value()
    print('Entrda 0.0', Entrada00)
 
    Entrada01 = client.get_node('ns=4; i=13')
    dv = ua.DataValue(ua.Variant(False, ua.VariantType.Boolean))
    Entrada01.set_data_value(dv)
    time.sleep(5)
'''