#!/usr/bin/env python
# -*- coding: utf-8 -*-
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import hashlib
import json
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("/listener")

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    print (json.loads(msg.payload.decode())
)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("10.102.24.227", 1883, 60)

payload = {"method": "LOGOUT",
    "userid": "859365",
    "session": "RPipKZTl",
    "version":"1.0"}
Pub_topic="/manage"
Sub_topic="/listener/859365/RPipKZTl"
Qos=1

client.subscribe(Sub_topic,Qos)
client.publish(Pub_topic, json.dumps(payload), Qos, False)
print("waiting for message")

client.loop_forever()






