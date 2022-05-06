                                
import paho.mqtt.client as mqtt
import time
import requests
import sys
from grovepi import *

#From GrovePi libraries
sys.path.append('../../Software/Python/')
import grovepi

ledred = 4
ledblue = 3
grovepi.pinMode(ledred,"OUTPUT")
grovepi.pinMode(ledblue,"OUTPUT")

def custom_callback(client, userdata, message):
    print("Gender of Person: " +  str(message.payload, "utf-8"))

    if(str(message.payload, "utf-8") == "male"):
        grovepi.digitalWrite(ledred,1)
        time.sleep(1)
        time.sleep(1)
        grovepi.digitalWrite(ledred,0)
    elif(str(message.payload, "utf-8") == "female"):
        grovepi.digitalWrite(ledblue,1)
        time.sleep(1)
        time.sleep(1)
        grovepi.digitalWrite(ledblue,0)   
def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))
    client.subscribe("paho/gender")
    client.message_callback_add("paho/gender", custom_callback)

def on_message(client, userdata, msg):
    gender = str(msg.payload, "utf-8")
    print("on_message: " + msg.topic + " " + str(msg.payload, "utf-8"))
    update = True

def loop_forever():
    client.loop_forever()
          
if __name__ == '__main__':
    update = False
    gender = None
    client = mqtt.Client()
    client.on_message = on_message
    client.on_connect = on_connect
    client.connect("test.mosquitto.org", 1883, 60)
    client.loop_forever()
