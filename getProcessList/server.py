import socket
import threading
import os
import cv2
from pyee import EventEmitter
import winsound as sd
import numpy as np
import matplotlib.pyplot as plt

def beepsound():
    fr = 500    # range : 37 ~ 32767
    du = 300     # 1000 ms ==1second
    sd.Beep(fr, du) 

ee = EventEmitter()



HOST = '0.0.0.0'

PORT = 9999        
  
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind((HOST, PORT))

server_socket.listen()

client_socket, addr = server_socket.accept()
client_socket.sendall("Connected".encode())
ipAddr = client_socket.recv(1024).decode()
print('Connected by', ipAddr)
beepsound()

def writePsList():
    global server_socket
    global client_socket
    data = client_socket.recv(100000)
    ip = data.decode().split(":-!?!-:")[-1]
    f = open("%s.txt" % ip, 'w')
    f.write(data.decode().replace("psutil.Process(", "").replace(")", "").replace(":-!?!-:%s" % ip, ""))
    print("%s: finished" % ip)
    return data.decode()

def saveScreen():
    global ipAddr
    global server_socket
    global client_socket
    data = client_socket.recv(800000)
    # show image using data 
    img = np.frombuffer(data, dtype=np.uint8)
    img = cv2.imdecode(img, cv2.IMREAD_COLOR)
    plt.imshow(img, interpolation='bicubic')
    plt.show()

def work():
    global server_socket
    global client_socket
    while True:
        inputUser = input("Input: ") 
        if inputUser == "exit":
            client_socket.sendall("exitAll".encode())
            ee.emit('exit')
        elif inputUser == "list":
            client_socket.sendall("send".encode())
            writePsList()
        elif inputUser == "exitClient":
            client_socket.sendall("exit".encode())
        elif inputUser == "exitApp":
            client_socket.sendall("exitApp".encode())
        elif inputUser == "screen":
            client_socket.sendall("screen".encode())
            saveScreen()

if __name__ == "__main__":
    threading.Thread(target=work).start()
    @ee.on('exit')
    def exit():
        # exit program
        print("exit")
        os._exit(0)