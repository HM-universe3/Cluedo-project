import socket
from _thread import *
import sys

server = " 192.168.0.50"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2) #the number is how many people can connect
print("Wating for a connection, server started")

def threaded_client(conn): #runs in background
    reply = ""
    
    while True:
        try:
            data = conn.recv(2048) #larger the size, longer it takes to recieve 
            reply = data.decode("utf-8")

            if not data:
                print("Disconnected")
                break
            else:
                print("Recieved: ", reply)
                print("Sending :", reply)

            conn.sendall(str.encode(reply))
        except:
            break

while True: #continuously listens for connections
    conn, addr = s.accept() #accepts incoming connections
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn))