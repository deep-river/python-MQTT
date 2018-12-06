# -*- coding: utf-8 -*-

"""
Module implementing Login.
"""
import hashlib
import json
import paho.mqtt.client as mqtt
import main
import  globalValue

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog

from Ui_login import Ui_Dialog

class Login(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Login, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_login.clicked.connect(self.login)
        self.pushButton_reg.clicked.connect(self.reg)
        
    def login(self): 
        client=mqtt.Client()
        self.userid=self.lineEdit_userid.text()
        password=self.lineEdit_password.text()
        
        globalValue.set_client(client)
        globalValue.set_userid(self.userid)
        
        client.on_connect = self.on_connect
        client.on_message = self.on_message
        
        client.connect("10.102.24.227", 1883, 60)
        client.loop_start()
        
        src = password.encode()
        m2 = hashlib.md5()
        m2.update(src)
        passwd_md5 = (m2.hexdigest())
        
        payload = {"method": "LOGIN",
            "userid": self.userid,
            "password": passwd_md5,
            "version":"1.0"}
        Pub_topic="/manage"
        Sub_topic="/listener/"+self.userid+passwd_md5[0]
        Qos=1

        client.subscribe(Sub_topic,Qos)
        client.publish(Pub_topic, json.dumps(payload), Qos, False)
        self.hide()
        self.main_show=main.main()
        self.main_show.show()
        
    def reg(self):
        username=self.lineEdit_userid.text()
        self.password=self.lineEdit_password.text()
        
        client = mqtt.Client()  
        client.on_connect = self.on_connect
        client.on_message = self.on_reg
        client.connect("10.102.24.227", 1883, 60)
        client.loop_start()
        
        src = self.password.encode()
        m2 = hashlib.md5()
        m2.update(src)
        passwd_md5 = (m2.hexdigest())
        
        payload = {"method": "REG",
            "username": username,
            "password": passwd_md5,
            "version":"1.0"}
        Pub_topic="/manage"
        Sub_topic="/listener/"+username+passwd_md5[0]
        Qos=1

        client.subscribe(Sub_topic,Qos)
        client.publish(Pub_topic, json.dumps(payload), Qos, False)
        
    def on_connect(self, client, userdata, flags, rc):
        print("Connected with result code "+str(rc))
        client.subscribe("/listener")
        
    def on_message(self, client, userdata, msg):
        message=json.loads(msg.payload.decode())
        print(message)
        session=message['session']
        globalValue.set_session(session)
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
        
if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    log_in = Login()   
    log_in.show()
    sys.exit(app.exec_())
