import sys
import wget
import time
import os
import threading
import datetime

from queue import Queue
from PyQt5 import QtCore
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QBasicTimer, QObject, QThread, pyqtSignal
from PyQt5.QtWidgets import * 
from PyQt5 import uic 
from PyQt5.QtCore import *

args = sys.argv

if not args.__len__() == 1:
    def download(args):
        def bar_progress(current, total, width=50):
            percentage = current / total * 100
            downloaded = round(current / 1000000, 2)
            totaly = round(total / 1000000, 2)
            speed = round((current / (time.time() - start_time)) / 1000000, 2)
            if speed == 0.0:
                left = "N/A"
            else:
                left = round((totaly - downloaded) / speed, 0)
            progress_message = "Downloading: %d%% [%smb / %smb] | %smb/s | %s left" % (percentage, downloaded, totaly, speed, left)
            sys.stdout.write("\r" + progress_message)
            sys.stdout.flush()
        global start_time
        start_time = time.time()
        # path = "C:/Users/%s/Desktop" % os.getlogin()
        path = ".\\"
        wget.download(args[1], path, bar=bar_progress)
        finishmsg = "%sDownload Complete! %sseconds%s" % ("="*10, str(round(time.time() - start_time, 2)), "="*10)
        print("\n"*50)
        sys.stdout.write("\r" + finishmsg)
        sys.stdout.flush()
        os.startfile(path)
    threading.Thread(target=download, args=[args]).start()
else:

    class Worker(QObject):
        finished = pyqtSignal()
        progress = pyqtSignal(int)

        def run(self, data):
            QApplication.processEvents()
            def bar_progress(current, total, width=50):
                QApplication.processEvents()
                percentage = current / total * 100
                downloaded = round(current / 1000000, 2)
                totaly = round(total / 1000000, 2)
                speed = round((current / (time.time() - start_time)) / 1000000, 2)
                if speed == 0.0:
                    left = "N/A"
                else:
                    left = round((totaly - downloaded) / speed, 0)
                progress_message = "Downloading: %d%% [%smb / %smb] | %smb/s | %s seconds left" % (percentage, downloaded, totaly, speed, left)
                data.lblinfo.setText(progress_message)
                data.pbar.setValue(current)
                data.pbar.setMaximum(total)
            start_time = time.time()
            # path = "C:/Users/%s/Desktop" % os.getlogin()
            path = ".\\"
            wget.download(data.input.text(), path, bar=bar_progress)
            finishmsg = "Download Complete! "+str(round(time.time() - start_time, 2))+"seconds"
            data.lblinfo.setText(finishmsg)
            

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
            self.lblinfo.resize(800, 20)

            self.pbar = QProgressBar(self)
            self.pbar.setGeometry(0, 70, 300, 25)
            self.pbar.setTextVisible(False)

            self.setWindowTitle('Web Downloader')
            self.setGeometry(500, 500, 600, 200)
            self.move(QApplication.desktop().screen().rect().center()- self.rect().center())
            self.show()

        def openFolder(self):
            # path = "C:/Users/%s/Desktop" % os.getlogin()
            path = ".\\"
            os.startfile(path)

        def onStart(self):
            self.input.setDisabled(True)
            self.buttonStart.setDisabled(True)
            self.thread = QThread()
            self.worker = Worker()
            self.worker.moveToThread(self.thread)
            self.thread.started.connect(lambda: self.worker.run(self))
            self.worker.finished.connect(self.thread.quit)
            self.worker.finished.connect(self.worker.deleteLater)
            self.thread.finished.connect(self.thread.deleteLater)
            self.thread.start()
            self.thread.finished.connect(lambda: self.buttonStart.setDisabled(False))
            self.thread.finished.connect(lambda: self.input.setDisabled(False))
            
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    app.exec_()