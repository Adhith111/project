# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from login import Ui_MainWindow
import pymysql
db=pymysql.connect("localhost","root","123","file")
cursor=db.cursor()
cursor.execute("SELECT VERSION()")
data=cursor.fetchone()
print("Database version: %s :",data)

class Ui_Register(object):
    def openWindow(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self.window)
        
        self.window.show()
    def openWindow1(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self.window)
        name=self.textEdit.toPlainText()
        email=self.textEdit_2.toPlainText()
        mobile=self.textEdit_3.toPlainText()
        address=self.textEdit_4.toPlainText()
        place=self.textEdit_5.toPlainText()
        usrname=self.textEdit_6.toPlainText()
        psw=self.textEdit_7.toPlainText()
        query="INSERT INTO register (name,email,mobile,address,place,usrname,psw) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        query1="INSERT INTO login (username,password) VALUES (%s,%s)"
        print("hai")
        cursor.execute(query,(name,email,mobile,address,place,usrname,psw))
        cursor.execute(query1,(usrname,psw))
        db.commit()
        print(cursor.rowcount, "record inserted.")
        self.window.show()




    def setupUi(self, Register):
        Register.setObjectName("Register")
        Register.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(Register)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 50, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(230, 110, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(230, 170, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(230, 230, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(230, 280, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(230, 330, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(230, 380, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(340, 50, 251, 31))
        self.textEdit.setObjectName("textEdit")

        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(340, 110, 251, 31))
        self.textEdit_2.setObjectName("textEdit_2")

        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(340, 170, 251, 31))
        self.textEdit_3.setObjectName("textEdit_3")

        self.textEdit_4 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_4.setGeometry(QtCore.QRect(340, 230, 251, 31))
        self.textEdit_4.setObjectName("textEdit_4")

        self.textEdit_5 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_5.setGeometry(QtCore.QRect(340, 280, 251, 31))
        self.textEdit_5.setObjectName("textEdit_5")

        self.textEdit_6 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_6.setGeometry(QtCore.QRect(340, 330, 251, 31))
        self.textEdit_6.setObjectName("textEdit_6")

        self.textEdit_7 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_7.setGeometry(QtCore.QRect(340, 380, 251, 31))
        self.textEdit_7.setObjectName("textEdit_7")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(210, 440, 99, 27))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(500, 440, 99, 27))
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton.clicked.connect(self.openWindow1)


        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(290, 490, 241, 27))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.openWindow)
        Register.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Register)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        Register.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Register)
        self.statusbar.setObjectName("statusbar")
        Register.setStatusBar(self.statusbar)

        self.retranslateUi(Register)
        QtCore.QMetaObject.connectSlotsByName(Register)


    def retranslateUi(self, Register):
        _translate = QtCore.QCoreApplication.translate
        Register.setWindowTitle(_translate("Register", "subtitles"))
        self.label.setText(_translate("Register", "Name"))
        self.label_2.setText(_translate("Register", "Email id"))
        self.label_3.setText(_translate("Register", "Mobile no"))
        self.label_4.setText(_translate("Register", "Address"))
        self.label_5.setText(_translate("Register", "Place"))
        self.label_6.setText(_translate("Register", "User name"))
        self.label_7.setText(_translate("Register", "Password"))
        self.pushButton.setText(_translate("Register", "SIGN IN"))
        self.pushButton_2.setText(_translate("Register", "CANCEL"))
        self.pushButton_3.setText(_translate("Register", "Allready have an Account?"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Register = QtWidgets.QMainWindow()
    ui = Ui_Register()
    ui.setupUi(Register)
    Register.show()
    sys.exit(app.exec_())

