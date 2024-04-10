import paho.mqtt.client as mqtt
from paho.mqtt.subscribeoptions import SubscribeOptions
from paho.mqtt.properties import Properties
from paho.mqtt.packettypes import PacketTypes
import time
import pygame

class iot(pygame.sprite.Sprite):
    def __init__(self, port, eid, topic):
        super(iot, self).__init__()
        self.surf = pygame.Surface((25, 25))
        self.surf.fill((0, 0, 0))
        self.rect = self.surf.get_rect()
        self.id = eid
        self.topic = topic
        self.status = "IDLE"
        self.timer = 0
        self.schedules = []
        self.tx_targets = []
        self.broker_address = 'localhost:' + str(port)
        self.client = mqtt.Client("client", protocol=mqtt.MQTTv5)
        self.client.connect(self.broker_address)
        self.client.on_message = self.on_message
        self.client.subscribe('response/' + str(self.id))
        self.publish_properties = Properties(PacketTypes.PUBLISH)
        self.publish_properties.ResponseTopic = 'response/' + str(self.id)
        self.publish_properties.CorrelationData = b""+bytes((self.eid * 124))
        self.client.loop_start()

    def on_message(self, client, userdata, message):
        msg = message.payload.decode()
        msg_type, data = str(msg).split(" ")
        match msg_type:
            case "add_schedule":
                self.schedules.append(data)
                self.tx_targets.append(self.timer+data)
            case "rm_schedule":
                i = self.schedules.index(data)
                del self.schedules[i]
                del self.tx_targets[i]
            case _:
                print(msg)


    def transmit_active(self):
        while self.status == "ACTIVE":
            self.client.publish(str(self.topic) + "/" + str(self.id), "data data_size user "+str(id), 2,
                                properties=self.publish_properties)

    def transmit_idle(self):
        while self.status == "IDLE":
            self.client.publish("idle/"+str(self.id), ""+str(self.id)+" is IDLE", 2, properties=self.publish_properties)

    def time_manager(self):
        self.timer += 1
        if self.status == "IDLE" & self.timer == 60:
            self.transmit_idle()
            self.timer = 0
        elif self.status == "ACTIVE" & self.timer in self.schedules:
            self.transmit_active()
            self.tx_targets.__setitem__(self.tx_targets.index(self.timer),
                                        self.schedules[self.tx_targets.index(self.timer)] +
                                        self.tx_targets[self.tx_targets.index(self.timer)])

























