import socket
import psutil
import requests
import select
import os
from time import time, sleep
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
                print(data.decode())
            elif data.decode() == "exitAll":
                print("server shutdown")
                break
            elif data.decode() == "exitApp":
                p = psutil.Process(os.getpid())
                p.terminate()

        # 소켓을 닫습니다.
        client_socket.close()
        print("Restarting...")
        sleep(2 - time() % 1)
        print("Restarting complete")
    except:
        print("restart due to error")
        continue