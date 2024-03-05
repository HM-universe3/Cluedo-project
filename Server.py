import socket
from _thread import *
import threading
import sys
import pickle
from Network import Network

HOST = "192.168.0.50"
PORT = 55555

clients = [] 

class Server:

    def threaded_client(conn): #runs in background
        conn.send(str.encode("Connected"))
    
        while True:
            try:
                #this receives the data from the client
                data = conn.recv(1048) #larger the size, longer it takes to recieve 

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


    def server(threaded_client):
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

class Client:
    def __init__(self):
        self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = "192.168.0.50"
        self.port = 55555
        self.address = (self.host, self.port)
        self.player = None

    def connect(self):
        self.clientSocket.connect(self.address)
        #this receives inital data from the server when it connects
        print(self.clien_socket.recv(2048).decode())

    def sendPosition(self):
        if self.player:
            self.player.send_position(self.client_socket)
        
    def receivePositions(self):
        if self.player:
            return self.player.receive_position(self.client_socket)
    
    def close(self):
        self.clientSocket.close()
