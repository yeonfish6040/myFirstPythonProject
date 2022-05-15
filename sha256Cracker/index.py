from PyQt5 import QtCore
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QBasicTimer
from PyQt5.QtWidgets import * 
from PyQt5 import uic 
from PyQt5.QtCore import *
from matplotlib.pyplot import text
from pyee import EventEmitter
from queue import Queue

import threading
import sys
import os
import time
import functions
import re
import hashlib

ee = EventEmitter()

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.lblnotice = QLabel(self)
        self.lblnotice.setText("please put sha256 hash")
        self.lblnotice.setAlignment(QtCore.Qt.AlignLeft)
        self.lblnotice.move(0, 3)

        self.lblcount = QLabel(self)
        self.lblcount.setText("waiting...")
        self.lblcount.setAlignment(QtCore.Qt.AlignLeft)
        self.lblcount.move(100, 20)
        self.lblcount.resize(150, 30)

        self.lblhash = QLabel(self)
        self.lblhash.setText("waiting...")
        self.lblhash.setAlignment(QtCore.Qt.AlignLeft)
        self.lblhash.move(100, 40)
        self.lblhash.resize(150, 40)

        self.input = QLineEdit(self)
        self.input.move(150, 0)
        self.input.textChanged.connect(self.onChanged)

        self.buttonStart = QPushButton(self)
        self.buttonStart.setText('Start')
        self.buttonStart.clicked.connect(self.onStart)
        self.buttonStart.move(350, 0)
        self.buttonStart.setDisabled(True)

        self.setWindowTitle('Password Finder')
        self.setGeometry(1000, 1000, 500, 400)
        self.show()

    def onChanged(self):
        QApplication.processEvents()
        if re.match('[A-Fa-f0-9]{64}', self.input.text()):
            text = "ready for cracking"
            self.buttonStart.setDisabled(False)
        else:
            text = "please type a valid hash"
            self.buttonStart.setDisabled(True)
        self.lblcount.setText(text)

    def onStart(self):
        self.input.setDisabled(True)
        global pwMatched
        global result
        global count
        global threads
        result = "a"
        pwMatched = False
        q = Queue()
        threads = dict()
        for i in range(0, 1):
            threads[i] = threading.Thread(target=pwMatch, args=[1, self.input, time.time(), self.lblcount, self.lblhash ,q])
        for i in threads:
            threads[i].start()
 
def pwMatch(jump, input, start_time, lbl1, lbl2, q):
    inputText = input.text()
    charList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '{', '[', '}', ']', '|', '\\', ':', ';', '"', '\'', ',', '<', '.', '>', '/', '?', ' ']
    global result
    global pwMatched
    global count
    global threads
    while not pwMatched:
        result = q.get()
        lbl2.setText(hashlib.sha256(result.encode()).hexdigest())
        ok = False
        QApplication.processEvents()
        if hashlib.sha256(result.encode()).hexdigest() == inputText:
            ok = True
            q.put("★")
        else:
    
        lbl1.setText(result)
        if ok == True:
            pwMatched = True
            lbl1.setText("finished!"+" - "+result+"\n"+"--- "+str(round(time.time() - start_time, 2))+" seconds --- ")
            break
        if result == "★":
            break
        increased = functions.str_increaser(result, charList, jump)
        if increased != "str_increaser(): Input already max in charset":
            result = increased
        else:
            result = "a"+"a"*result.__len__()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())