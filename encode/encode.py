from PyQt5 import QtCore
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QBasicTimer
from PyQt5.QtWidgets import * 
from PyQt5 import uic 
from PyQt5.QtCore import *
from pyee import EventEmitter

import sys
import os
import pyperclip
import math
import functions

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.lblString = QLabel(self)
        self.lblString.setText("난독화할 문자열을 입력해주세요")
        self.lblString.setAlignment(QtCore.Qt.AlignLeft)
        self.lblString.move(0, 23)
        self.lblKey = QLabel(self)
        self.lblKey.setText("키를 입력해 주세요")
        self.lblKey.setAlignment(QtCore.Qt.AlignLeft)
        self.lblKey.move(0, 90)

        self.lbl1 = QLabel(self)
        self.lbl1.setText("waiting")
        self.lbl1.move(0, 200)
        self.lbl1.repaint()

        self.inputString = QLineEdit(self)
        self.inputString.move(0, 40)
        self.inputString.textChanged.connect(self.onChanged)
        self.inputKey = QLineEdit(self)
        self.inputKey.move(0, 107)
        self.inputKey.textChanged.connect(self.onChanged)

        self.buttonEncode = QPushButton(self)
        self.buttonEncode.setText('난독화')
        self.buttonEncode.clicked.connect(self.encode)
        self.buttonEncode.move(300, 40)

        self.buttonCopy = QPushButton(self)
        self.buttonCopy.setText('복사')
        self.buttonCopy.clicked.connect(self.copyText)
        self.buttonCopy.move(0, 170)

        self.setWindowTitle('문자열 난독화')
        self.setGeometry(1000, 1000, 500, 400)
        self.show()

    def encode(self):
        do_work_encode(self)

    def copyText(self):
        pyperclip.copy(self.lbl1.text().replace("복호화된 문자열: ","").replace("난독화된 문자열: ",""))
 
def do_work_encode(self):
    result = functions.encode(self.inputString.text(), self.inputKey.text())
    self.lbl1.setText("난독화된 문자열: %s" % result)
    self.lbl1.adjustSize()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())