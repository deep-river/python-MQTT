import json

def on_connect(self, client, userdata, flags, rc):
        print("Connected with result code "+str(rc))
        client.subscribe("/listener")
        
def on_message(self, client, userdata, msg):
    message=json.loads(msg.payload.decode())
    print(message)
    session=message['session']
    self.set_session(session)
    print(session)
    Qos=1
    client.on_message = self.on_subscribe
    Sub_topic="/listener/"+ self.userid+"/"+ session
    client.subscribe(Sub_topic,Qos)

def on_subscribe(self, client, userdata, msg):
    message=json.loads(msg.payload.decode())
    print(message)  
    
def on_reg(self, client, userdata, msg):
    message=json.loads(msg.payload.decode())
    print(message)
    self.lineEdit_userid.setText(message['userid'])
    self.lineEdit_password.setText(self.password)

def set_client(input_value):
   global client
   client = input_value
def get_client():
   return client
def set_userid(input_value):
   global userid
   userid = input_value
def get_userid():
   return str(userid)
def set_session(input_value):
   global session
   session = input_value
def get_session():
   return str(session)
