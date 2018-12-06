# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\mqtt\login.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        Dialog.setSizeGripEnabled(True)
        self.lineEdit_userid = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_userid.setGeometry(QtCore.QRect(170, 110, 151, 20))
        self.lineEdit_userid.setObjectName("lineEdit_userid")
        self.lineEdit_password = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_password.setGeometry(QtCore.QRect(170, 160, 151, 20))
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.label_userid = QtWidgets.QLabel(Dialog)
        self.label_userid.setGeometry(QtCore.QRect(80, 100, 61, 41))
        self.label_userid.setObjectName("label_userid")
        self.label_password = QtWidgets.QLabel(Dialog)
        self.label_password.setGeometry(QtCore.QRect(80, 150, 61, 41))
        self.label_password.setObjectName("label_password")
        self.pushButton_login = QtWidgets.QPushButton(Dialog)
        self.pushButton_login.setGeometry(QtCore.QRect(110, 220, 75, 23))
        self.pushButton_login.setObjectName("pushButton_login")
        self.pushButton_reg = QtWidgets.QPushButton(Dialog)
        self.pushButton_reg.setGeometry(QtCore.QRect(220, 220, 75, 23))
        self.pushButton_reg.setObjectName("pushButton_reg")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(140, 50, 111, 41))
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_userid.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">用户名：</span></p></body></html>"))
        self.label_password.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">密码：</span></p></body></html>"))
        self.pushButton_login.setText(_translate("Dialog", "登录"))
        self.pushButton_reg.setText(_translate("Dialog", "注册"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">欢迎使用</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

