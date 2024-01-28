import socket
from _thread import *
import sys
host = "192.168.0.50"
port = 55555


clients = []

try:
    s.bind((server, port))
except socket.error as e:
    str(e)
#The number is how many people can connect
#s.listen(2)
print("Wating for a connection, server started")

def threaded_client(conn): #runs in background
    conn.send(str.encode("Connected"))
    reply = ""
    
    while True:
        try:
            #this receives the data from the client
            data = conn.recv(1024) #larger the size, longer it takes to recieve 

            if not data:
                print("Disconnected")
                break
            
            for client in clients:
                if client != conn:
                    try:
                        client.send(data)
                    except:
                        clients.remove(client)
        except:
            break
    
    clients.remove(conn)
    print("Lost connection")
    conn.close()


def server():
    socket_for_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_for_server.bind((host, port))
    socket_for_server.listen()

    while True: #continuously listens for connections
        conn, addr = socket_for_server.accept(conn, addr) #accepts incoming connections
        clients.append(conn)
        print("Connected to:", addr)

        #need to start a new thread for each client that's connected

