import socket
from _thread import *
import threading
import sys


HOST = "192.168.0.50"
PORT = 55555

clients = [] #to hold which clients are connected

def threaded_client(conn): #runs in background
    conn.send(str.encode("Connected"))
    
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
    socketForServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socketForServer.bind((HOST, PORT))
    socketForServer.listen()

    while True: #continuously listens for connections
        conn, addr = socketForServer.accept(conn, addr) #accepts incoming connections
        clients.append(conn)
        print("Connected to:", addr)

        #need to start a new thread for each client that's connected
        clientHandler = threading.Thread(target=threaded_client, args=(conn,))
        clientHandler.start()


if __name__ == "__main__":
    server()

