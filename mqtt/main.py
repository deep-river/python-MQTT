# -*- coding: utf-8 -*-

"""
Module implementing main.
"""
import hashlib
import json
import paho.mqtt.client as mqtt
import cv2
import numpy
import threading
import  globalValue
from audio import *
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow

from Ui_mqtt import Ui_MainWindow


class main(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(main, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_connect.clicked.connect(self.chat)
        self.pushButton_OnVideo.clicked.connect(self.OnVideo)
        self.pushButton_OffVideo.clicked.connect(self.OffVideo)
        self.pushButton_RecVideo.clicked.connect(self.RecVideo)
        self.pushButton_UnrecVideo.clicked.connect(self.UnrecVideo)
        self.pushButton_OnVoice.clicked.connect(self.OnVoice)
        self.pushButton_OffVoice.clicked.connect(self.OffVoice)
        self.pushButton_RecVoice.clicked.connect(self.RecVoice)
        self.pushButton_UnrecVoice.clicked.connect(self.UnrecVoice)
        self.pushButton_add.clicked.connect(self.add)
        self.pushButton_del.clicked.connect(self.delete)
        self.pushButton_list.clicked.connect(self.listfriend)
        
        self.client = globalValue.get_client()
        self.client.conData='off'
        thread_sound = Audio(self.client)
        thread_sound.start()
        
        self.client.p = PyAudio()
        self.client.stream = self.client.p.open(format=paInt16,
                                           channels=1,
                                           rate=8000,
                                           output=True,
                                           frames_per_buffer = 1200
                                          )
                                          
    def on_chat(self, client, userdata, msg):
        message=json.loads(msg.payload.decode())
        print(message)
        self.client.userSession=message['online'][self.client.userID]
        print(self.client.userSession)
        self.client.on_message = self.on_subscribe
    
    def on_subscribe(self, client, userdata, msg):
        message=json.loads(msg.payload.decode())
        print(message)
    
    def on_video_command(self, client, userdata, msg):
        message=json.loads(msg.payload.decode())
        self.conData=message['data']
        print(self.conData)
        t=threading.Thread(target=self.pub_video)
        t.setDaemon(True)
        t.start()
        
    def on_video(self, client, userdata, msg):
        count=200
        length=self.recvall(count, msg)
        #recData = self.recvall(len(length), msg)
        data = numpy.fromstring(length, dtype='uint8')
        decimg=cv2.imdecode(data,1)
        cv2.imshow('Video',decimg)
        if (cv2.waitKey(1) & 0xFF == ord('q')) or (self.conData == 'off'):
            cv2.destroyAllWindows()
            self.client.on_message = self.on_null
            
    def on_null(self, client, userdata, msg):
        print('监控断开！')
        
    def recvall(self, count, msg): 
        buf=b''
        while (count>0):
            message=msg.payload
            if not message :
                return None
            buf+=message
            count -= len(message)
        return buf    
        
    def pub_video(self):
        if(self.conData == 'on'):
            capture = cv2.VideoCapture(0)
            ret, frame = capture.read()
            encode_param=[int(cv2.IMWRITE_JPEG_QUALITY),90]
            while ret:
                #cv2.imshow('Video',frame)
                result, imgencode = cv2.imencode('.jpg', frame, encode_param)
                data = numpy.array(imgencode)
                stringData = data.tostring()
                Pub_topic="/listener/"+self.client.userID+"/"+self.client.userSession
                Qos=1
                self.client.publish(Pub_topic,stringData , Qos, False)
                ret, frame = capture.read()
                if (cv2.waitKey(1) & 0xFF == ord('q')) or (self.conData == 'off'):
                    break
            capture.release()
            cv2.destroyAllWindows() 
            
    def chat(self):
        self.client.userID = self.lineEdit_ID.text()
        self.userid = globalValue.get_userid()
        self.session = globalValue.get_session()
        self.client.on_message = self.on_chat
        payload = {"method": "CHAT",
            "userid": self.userid,
            "session": self.session,
            "request":[self.client.userID], 
            "version":"1.0"}
        Pub_topic="/manage"
        Qos=1
        self.client.publish(Pub_topic, json.dumps(payload), Qos, False)
   
    def add(self):
        self.client.userID = self.lineEdit_ID.text()
        self.userid = globalValue.get_userid()
        self.session = globalValue.get_session()
        self.client.on_message = self.on_subscribe
        payload = {"method": "ADDFRIEND",
            "userid": self.userid,
            "session": self.session,
            "request":self.client.userID, 
            "version":"1.0"}
        Pub_topic="/manage"
        Qos=1
        self.client.publish(Pub_topic, json.dumps(payload), Qos, False)
        
    def delete(self):
        self.client.userID = self.lineEdit_ID.text()
        self.session = globalValue.get_session()
        self.userid = globalValue.get_userid()
        self.client.on_message = self.on_subscribe
        payload = {"method": "DELFRIEND",
            "userid": self.userid,
            "session": self.session,
            "request":self.client.userID, 
            "version":"1.0"}
        Pub_topic="/manage"
        Qos=1
        self.client.publish(Pub_topic, json.dumps(payload), Qos, False)
    
    def listfriend(self):  
        self.session = globalValue.get_session()
        self.userid = globalValue.get_userid()
        self.client.on_message = self.on_listfriend
        payload = {"method": "LISTFRIEND",
            "userid": self.userid,
            "session": self.session, 
            "version":"1.0"}
        Pub_topic="/manage"
        Qos=1
        self.client.publish(Pub_topic, json.dumps(payload), Qos, False)
    
    def on_listfriend(self, client, userdata, msg):
        message=json.loads(msg.payload.decode())
        #self.textBrowser.append(msg.payload.decode())
        friendlist=message['friendlist']
        for i in range(len(friendlist)):
            for key in friendlist:
                self.textBrowser.append("{}:{}".format(key,friendlist[key]))
        
    def OnVideo(self):
        self.client.on_message = self.on_video
        self.conData='on'
        payload = {"type":"control", 
            "data":"on"
        }
        Pub_topic="/listener/"+self.client.userID+"/"+self.client.userSession
        Qos=1
        self.client.publish(Pub_topic, json.dumps(payload), Qos, False)
        
    def OffVideo(self):
        self.conData='off'
        payload = {"type":"control", 
            "data":"off"
        }
        Pub_topic="/listener/"+self.client.userID+"/"+self.client.userSession
        Qos=1
        self.client.publish(Pub_topic, json.dumps(payload), Qos, False)
        
    def RecVideo(self):
        self.client.on_message = self.on_video_command
        
    def UnrecVideo(self):
        self.client.on_message = self.on_subscribe 
            
    def OnVoice(self):
        self.client.on_message = self.on_voice
        self.client.command='on'
        payload = {"type":"control", 
            "data":"on"
        }
        Pub_topic="/listener/"+self.client.userID+"/"+self.client.userSession
        Qos=1
        self.client.publish(Pub_topic, json.dumps(payload), Qos, False)
        
    def OffVoice(self):
        self.client.command='off'
        payload = {"type":"control", 
            "data":"off"
        }
        Pub_topic="/listener/"+self.client.userID+"/"+self.client.userSession
        Qos=1
        self.client.publish(Pub_topic, json.dumps(payload), Qos, False)
        
    def RecVoice(self):
        self.client.on_message = self.on_voice_command
        
    def UnrecVoice(self):
        self.client.on_message = self.on_subscribe 
    
    def on_voice_command(self, client, userdata, msg):
        message=json.loads(msg.payload.decode())
        self.client.conData=message['data']
        print(self.client.conData)
        
    def on_voice(self, client, userdata, msg):    
        if self.client.command =='on':
            buffer = msg.payload
            #print(buffer.decode())
            client.stream.write(buffer, 1200)
        
if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    dlg = main()
    dlg.show()
    sys.exit(app.exec_())
