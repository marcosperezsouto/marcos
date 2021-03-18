# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 16:04:13 2021

@author: marcos
"""

from gtts import gTTS
import os

from opcua import Client
from opcua import ua

url = "opc.tcp://192.168.1.150:4840"
client = Client(url)
client.connect()

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
os.system('prueba.mp3')




