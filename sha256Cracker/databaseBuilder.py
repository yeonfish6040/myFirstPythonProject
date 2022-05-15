from PyQt5 import QtCore
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QBasicTimer
from PyQt5.QtWidgets import * 
from PyQt5 import uic 
from PyQt5.QtCore import *

import functions
import sqlite3
import os
import sys

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.lblnotice = QLabel(self)
        self.lblnotice.setText("char to start")
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
        self.lblhash.move(100, 60)
        self.lblhash.resize(150, 40)

        self.input = QLineEdit(self)
        self.input.move(150, 0)

        self.buttonStart = QPushButton(self)
        self.buttonStart.setText('Start')
        self.buttonStart.clicked.connect(self.onStart)
        self.buttonStart.move(350, 0)

        self.setWindowTitle('sha256 db builder')
        self.setGeometry(1000, 1000, 500, 400)
        self.show()

    def onStart(self):
        db_path = './sha256Values.db'
        conn = sqlite3.connect(db_path)
        print(conn)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())