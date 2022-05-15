import sys
import wget
import time
import os
import threading

from queue import Queue
from PyQt5 import QtCore
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QBasicTimer
from PyQt5.QtWidgets import * 
from PyQt5 import uic 
from PyQt5.QtCore import *

args = sys.argv

if not args.__len__() == 1:
    def download():
        def bar_progress(current, total, width=50):
            progress_message = "Downloading: %d%% [%smb / %smb] | %smb/s" % (current / total * 100, round(current / 1000000, 2), round(total / 1000000, 2), str((current / (time.time() - start_time)) / 1000000)[0:4])
            sys.stdout.write("\r" + progress_message)
            sys.stdout.flush()
        global start_time
        start_time = time.time()
        path = "C:/Users/%s/Desktop" % os.getlogin()
        wget.download(args[1], path, bar=bar_progress)
        finishmsg = "%sDownload Complete! %sseconds%s" % ("="*10, str(round(time.time() - start_time, 2)), "="*10)
        print("\n"*50)
        sys.stdout.write("\r" + finishmsg)
        sys.stdout.flush()
        os.startfile(path)
    threading.Thread(target=download).start()
else:
    class MyApp(QWidget):
        def __init__(self):
            super().__init__()
            self.initUI()

        def initUI(self):
            self.lblnotice = QLabel(self)
            self.lblnotice.setText("put the file's url in the input box")
            self.lblnotice.setAlignment(QtCore.Qt.AlignLeft)
            self.lblnotice.move(0, 8)

            self.input = QLineEdit(self, alignment=Qt.AlignCenter)
            self.input.setPlaceholderText('file url to download')
            self.input.move(0, 30)
            self.input.resize(300, 20)

            self.buttonStart = QPushButton(self)
            self.buttonStart.setText('Start')
            self.buttonStart.clicked.connect(self.onStart)
            self.buttonStart.move(300, 30)
            self.buttonStart.resize(60, 22)

            self.buttonPath = QPushButton(self)
            self.buttonPath.setText('open folder')
            self.buttonPath.clicked.connect(self.openFolder)
            self.buttonPath.move(0, 140)
            self.buttonPath.resize(100, 22)

            self.lblinfo = QLabel(self)
            self.lblinfo.setText("Downloading: 0% [0 mb / 0 mb] | 0 mb/s")
            self.lblinfo.move(0, 100)
            self.lblinfo.resize(400, 20)

            self.pbar = QProgressBar(self)
            self.pbar.setGeometry(0, 70, 300, 25)
            self.pbar.setTextVisible(False)

            self.setWindowTitle('Web Downloader')
            self.setGeometry(500, 500, 600, 200)
            self.move(QApplication.desktop().screen().rect().center()- self.rect().center())
            self.show()

        def openFolder(self):
            path = "C:/Users/%s/Desktop" % os.getlogin()
            os.startfile(path)

        def onStart(self):
            self.input.setDisabled(True)
            self.buttonStart.setDisabled(True)
            q = Queue()
            threading.Thread(target=download, args=[q, self.input.text()]).start()
            threading.Thread(target=update, args=[q, self]).start()

    def update(q, self):
            while True:
                QApplication.processEvents()
                if q.get()[0] == "done":
                    self.lblinfo.setText(q.get()[1])
                else:
                    self.lblinfo.setText(q.get()[0])
                    self.pbar.setValue(q.get()[1])
                    self.pbar.setMaximum(q.get()[2])

    def download(q, url):
        # process event
        QApplication.processEvents()
        def bar_progress(current, total, width=50):
            QApplication.processEvents()
            progress_message = "Downloading: %d%% [%smb / %smb] | %smb/s" % (current / total * 100, round(current / 1000000, 2), round(total / 1000000, 2), str((current / (time.time() - start_time)) / 1000000)[0:4])
            q.put([progress_message, current, total])
        start_time = time.time()
        path = "C:/Users/%s/Desktop" % os.getlogin()
        wget.download(url, path, bar=bar_progress)
        finishmsg = "Download Complete! "+str(round(time.time() - start_time, 2))+"seconds"
        q.put(["done", finishmsg])

    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    app.exec_()