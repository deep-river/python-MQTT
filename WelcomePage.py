import sys
from PyQt5.QtWidgets import *
 
class Window(QWidget):
    right_uname = "Null"
    right_pword = "Password1"
 
    def __init__(self):
        super().__init__()
        self.init_ui()
 
    def init_ui(self):
        self.resize(390, 240)
        self.lbl_intro = QLabel('Welcome, please login')
        self.lbl_enter_username = QLabel('Username:')
        self.lbl_enter_password = QLabel('Password:')
        self.txt_enter_username = QLineEdit()
        self.txt_enter_password = QLineEdit()
        self.btn_login = QPushButton('Login')
        self.btn_register = QPushButton('Register')
 
 
        self.grid = QGridLayout()
        self.grid.setSpacing(6)
 
        self.grid.addWidget(self.lbl_intro, 1, 1)
 
        self.grid.addWidget(self.lbl_enter_username, 2, 0)
        self.grid.addWidget(self.txt_enter_username, 2, 1)
 
        self.grid.addWidget(self.lbl_enter_password, 3, 0)
        self.grid.addWidget(self.txt_enter_password, 3, 1)
 
        self.grid.addWidget(self.btn_login, 5, 1)
 
        self.grid.addWidget(self.btn_register, 6, 1)
 
        self.v_box = QVBoxLayout()
        self.v_box.addStretch(0)
        self.v_box.addLayout(self.grid)
        self.v_box.addStretch(0)
 
        self.h_box = QHBoxLayout()
        self.h_box.addStretch(0)
        self.h_box.addLayout(self.v_box)
        self.h_box.addStretch(0)
 
        self.setLayout(self.h_box)
        self.setWindowTitle('Login Page')
 
        self.btn_login.clicked.connect(lambda: self.btn_login_clk(self.txt_enter_username, self.txt_enter_password, self.lbl_intro))
 
        self.btn_register.clicked.connect(self.btn_register_clk)
        
        self.show()
 
    def btn_login_clk(self, username, password, intro):
        print('Click!')
        self.mw = MainWindow()
        self.hide()
        self.mw.show()
 
    def clear_box(self):
        self.txt_enter_username.clear()
        self.txt_enter_password.clear()
        self.txt_enter_username.setFocus()
        
    def btn_register_clk(self):
        print('Click!')
        self.mw = RegisterPage()
        self.hide()
        self.mw.show()
 
 
class MainWindow(Window):
 
    def __init__(self):
        super().__init__()
        self.init_ui()
 
    def init_ui(self):
        self.resize(320, 380)
        self.lbl_intro = QLabel('Terminal Control')
        self.lbl_user_logged = QLabel('Welcome,' + ' ' + self.right_uname)
        self.lbl_send = QLabel('chat box')
        self.txt_write_box = QLineEdit()
        self.btn_send = QPushButton('Send')
        self.btn_audio = QPushButton('Open Microphone')
        self.btn_video = QPushButton('Open Camera')
        self.btn_logout = QPushButton('Logout')
 
        layout = QVBoxLayout()
        layout.addWidget(self.lbl_intro)
        layout.addWidget(self.lbl_user_logged)
        layout.addWidget(self.lbl_send)
        layout.addWidget(self.txt_write_box)
        layout.addWidget(self.btn_send)
        layout.addWidget(self.btn_audio)
        layout.addWidget(self.btn_video)
        layout.addWidget(self.btn_logout)
 
        self.setLayout(layout)
        self.setWindowTitle('Control Page')
 
        self.btn_send.clicked.connect(self.send_clk)
        #self.btn_audio.clicked.connect(self.audio_clk)
        #self.btn_video.clicked.connect(self.video_clk)
        self.btn_logout.clicked.connect(self.logout_action)
 
        self.show()
 
    def send_clk(self):
        self.append = open('text.txt', 'a')
        self.append.write('hry')
        self.append.close()
        
    #def audio_clk(self):
        
        
    #def video_clk(self):
    
    
 
    def logout_action(self):
        self.close()
        a_window.show()
        a_window.clear_box()
        
class RegisterPage(QWidget):
    
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        self.resize(390, 240)
        self.lbl_register_intro = QLabel('Register')
        self.lbl_username = QLabel('Username:')
        self.lbl_password = QLabel('Password:')
        self.txt_username = QLineEdit()
        self.txt_password = QLineEdit()
        self.btn_enter = QPushButton('Register')
        self.btn_back = QPushButton('Back')
        
        self.grid = QGridLayout()
        self.grid.setSpacing(6)
        self.grid.addWidget(self.lbl_register_intro, 1, 1)
        self.grid.addWidget(self.lbl_username, 2, 0)
        self.grid.addWidget(self.txt_username, 2, 1)
        self.grid.addWidget(self.lbl_password, 3, 0)
        self.grid.addWidget(self.txt_password, 3, 1)
        self.grid.addWidget(self.btn_enter, 5, 1)
        self.grid.addWidget(self.btn_back, 6, 1)
 
        self.v_box = QVBoxLayout()
        self.v_box.addStretch(0)
        self.v_box.addLayout(self.grid)
        self.v_box.addStretch(0)
 
        self.h_box = QHBoxLayout()
        self.h_box.addStretch(0)
        self.h_box.addLayout(self.v_box)
        self.h_box.addStretch(0)
 
        self.setLayout(self.h_box)
        self.setWindowTitle('Register Page')
 
        #self.btn_enter.clicked.connect(self.enter_clk)
        self.btn_back.clicked.connect(self.back_action)
 
        self.show()
    
    #def enter_clk(self, username, password, intro):
        
        
    def back_action(self):
        self.close()
        a_window.show()
        a_window.clear_box()
 
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    a_window = Window()
    sys.exit(app.exec())
