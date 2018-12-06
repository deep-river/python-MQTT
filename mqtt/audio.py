import threading
from pyaudio import PyAudio, paInt16

class Audio(threading.Thread):
    def __init__(self, client):
        threading.Thread.__init__(self)
        self.client = client
        self.lock = threading.Lock()
        self.p = PyAudio()
        self.stream = None
    def __del__(self) :
        if self.stream is not None:
            self.stream.stop_stream()
            self.stream.close()
        self.p.terminate()
    def run(self):
        num =1200
        self.stream = self.p.open(format=paInt16, 
                                           channels=1,
                                           rate=8000,
                                           input=True,
                                           frames_per_buffer=num)
        while True:
            if self.client.conData =='on':
                string_audio_data = self.stream.read(num)
                Pub_topic="/listener/"+self.client.userID+"/"+self.client.userSession
                Qos=1
                self.client.publish(Pub_topic, string_audio_data, Qos, False)
            else:
                pass
                


 
