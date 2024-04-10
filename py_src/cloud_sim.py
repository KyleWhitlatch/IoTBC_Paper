import paho.mqtt.client as mqtt
from paho.mqtt.subscribeoptions import SubscribeOptions
import pygame


class cloud(pygame.sprite.Sprite):
    def __init__(self):
        self.brokers = ['localhost:' + str(x) for x in range(1883, 1888)]



    def on_message(client, userdata, message):
        try:
            print("request received from: " + message.properties.se)
            print(message.payload.decode())
            response_topic = message.properties.ResponseTopic
            client.publish(response_topic, 'server message', 1, properties=message.properties)
            print('response sent from server')
        except:
            print('error')







