import socket
import os
import sys
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
    dataSize = client_socket.recv(1024)
    dataSize = int(dataSize.decode())
    dataShape = client_socket.recv(1024)
    dataShape = dataShape.decode().split("|")
    dataShape = (int(dataShape[0]), int(dataShape[1]), int(dataShape[2]))
    data = client_socket.recv(dataSize)
    # print size of data
    print(sys.getsizeof(data))
    img = np.frombuffer(data, dtype=np.uint8)
    img = img.reshape(dataShape)
    plt.imshow(img)
    plt.show()

@ee.on('exit')
def exit():
    # exit program
    print("exit")
    os._exit(0)

while True:
    if sys.argv.__len__() == 2:
        if sys.argv[1] == "exit":
            client_socket.sendall("exitApp".encode())
            ee.emit('exit')
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
        ee.emit('exit')
    elif inputUser == "screen":
        client_socket.sendall("screen".encode())
        saveScreen()