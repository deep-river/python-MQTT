# -*- coding: utf-8 -*-

"""
Module implementing main.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow
import add_user
import show_list
from PyQt5 import QtWidgets
from Ui_main import Ui_MainWindow



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
        global str_name
        global str_pass
        super(main, self).__init__(parent)
        self.setupUi(self)
        self.add_b.clicked.connect(self.add)
        self.load_ok.clicked.connect(self.load)
    def add(self):
        self.win_a = add_user.add_user()
        self.win_a.show()
        
        
    def load(self):
        self.hide()
        self.list_f = show_list.show_list()
        self.list_f.show()
        global str_name
        str_name = self.line_name.text()
        global str_pass
        str_pass = self.line_pass.text()
        
if __name__=="__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)
    myshow2=main()
    myshow2.show()
    sys.exit(app.exec_())
