#!/usr/bin/python

import paho.mqtt.client as paho
mqttc = paho.Client()
topic = "/request/domain/endpoints/mbed-eth-endpoint/303/0/5700"
message = "{\"sync\":\"true\"}"
ip = "10.1.0.26"
mqttc.connect(ip, 1883, 60)
mqttc.publish(topic,message)
mqttc.disconnect();
