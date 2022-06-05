from PyQt5 import QtCore
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QBasicTimer
from PyQt5.QtWidgets import * 
from PyQt5 import uic 
from PyQt5.QtCore import *

import sys
import functions
import os
import psutil

class Worker(QObject):
    def settingData(self, data):
        db_path = './sha256Values.db'
        with open(db_path, 'r') as f:
            # check file emtpy
            if f.read() == '':
                with open(db_path, 'w') as fs:
                    fs.write('a§'+functions.getHash("a")+"\n")
                string = "a"
            else:
                # get last string
                with open(db_path, 'r') as f:
                    string = f.readlines()[-1].split('§')[0]
        stop = False
        while not stop:
            QApplication.processEvents()
            increased = functions.str_increaser(string, functions.charList(), 1)
            if increased != "str_increaser(): Input already max in charset":
                string = increased
            else:
                string = "a"+"a"*string.__len__()
            with open(db_path, 'a') as f:
                f.write(string+"§"+functions.getHash(string)+"\n")
            with open(db_path, 'r') as f:
                    count = f.readlines().__len__()
            data.lblcount.setText(string)
            data.lblhash.setText(functions.getHash(string))

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.lblcount = QLabel(self)
        self.lblcount.setText("waiting...")
        self.lblcount.setAlignment(QtCore.Qt.AlignLeft)
        self.lblcount.move(30, 10)
        self.lblcount.resize(150, 30)

        self.lblhash = QLabel(self)
        self.lblhash.setText("waiting...")
        self.lblhash.setAlignment(QtCore.Qt.AlignLeft)
        self.lblhash.move(30, 50)
        self.lblhash.resize(500, 40)

        self.buttonStart = QPushButton(self)
        self.buttonStart.setText('Start')
        self.buttonStart.clicked.connect(self.onStart)
        self.buttonStart.move(350, 0)

        self.buttonStop = QPushButton(self)
        self.buttonStop.setText('Stop')
        self.buttonStop.clicked.connect(self.stop)
        self.buttonStop.move(350, 20)
        self.buttonStop.setDisabled(True)

        self.setWindowTitle('sha256 db builder')
        self.setGeometry(1000, 1000, 500, 400)
        self.show()

    def onStart(self):
        self.buttonStart.setDisabled(True)
        self.buttonStop.setDisabled(False)
        self.thread = QThread()
        self.worker = Worker()
        self.worker.moveToThread(self.thread)
        self.thread.setDaemon = True
        self.thread.started.connect(lambda: self.worker.settingData(self))
        self.thread.start()

    def stop(self):
        self.buttonStop.setDisabled(True)
        self.buttonStart.setDisabled(False)
        QApplication.processEvents()
        p = psutil.Process(os.getpid())
        p.terminate()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())