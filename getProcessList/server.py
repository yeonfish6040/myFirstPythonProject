import socket
import threading
import os
from pyee.base import EventEmitter

ee = EventEmitter()



HOST = '192.168.0.51'

PORT = 9999        
  
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind((HOST, PORT))

server_socket.listen()

client_socket, addr = server_socket.accept()
client_socket.sendall("Connected".encode())
print('Connected by', addr)

def acceptcnt():
    global server_socket
    global client_socket
    client_socket, addr = server_socket.accept()
    print('Connected by', addr)

def run():
    global server_socket
    global client_socket
    data = client_socket.recv(100000)
    ip = data.decode().split(":-!?!-:")[-1]
    f = open("%s.txt" % ip, 'w')
    f.write(data.decode().replace("psutil.Process(", "").replace(")", "").replace(":-!?!-:%s" % ip, ""))
    print("%s: finished" % ip)
    return data.decode()

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
            run()
        elif inputUser == "exitClient":
            client_socket.sendall("exit".encode())
        elif inputUser == "exitApp":
            client_socket.sendall("exitApp".encode())
        else:
            continue

if __name__ == "__main__":
    threading.Thread(target=acceptcnt).start()
    threading.Thread(target=work).start()
    @ee.on('exit')
    def exit():
        # exit program
        print("exit")
        os._exit(0)