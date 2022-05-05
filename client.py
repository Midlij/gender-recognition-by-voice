import paho.mqtt.client as mqtt
import time
import requests
import sys
from grovepi import *

#From GrovePi libraries
sys.path.append('../../Software/Python/')
import grovepi

led = 4

grovepi.pinMode(led,"OUTPUT")

class device_subpub():

    def __init__(self):
        self.update = False
        self.gender = None
        self.client = mqtt.Client()
        self.client.on_message = on_message
        self.client.on_connect = on_connect
        self.client.connect("test.mosquitto.org", 1883, 60)
    
    def on_connect(self, client, userdata, flags, rc):
        print("Connected to server (i.e., broker) with result code "+str(rc))
        self.client.subscribe("paho/gender")
        self.client.custom_callback_add("paho/gender", custom_callback)

    def on_message(self, client, userdata, msg):
        self.gender = str(msg.payload, "utf-8")
        print("on_message: " + msg.topic + " " + str(msg.payload, "utf-8"))
        self.update = True

    def custom_callback(self, client, userdata, message):
        print(str(msg.payload, "utf-8"))
        
        if(str(msg.payload, "utf-8") == "male"):
            grovepi.digitalWrite(LED,1)
        elif(str(msg.payload, "utf-8") == "female"):
            grovepi.digitalWrite(LED,0)

    def loop_forever(self):
        self.client.loop_forever()
            
if __name__ == '__main__':
    dps = device_subpub()
    dps.loop_forever()
                
