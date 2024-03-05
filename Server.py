import socket
from _thread import *
import threading
from Network import Network

HOST = "192.168.0.50"
PORT = 55555

clients = [] 

import socket
import threading

class ServerClass:
    clients = []

    @staticmethod
    def threaded_client(conn): 
        conn.send(str.encode("Connected"))
    
        while True:
            try:
                data = conn.recv(1024) 

                if not data:
                    print("Disconnected")
                    break
            
                for client in ServerClass.clients:
                    if client != conn:
                        try:
                            client.send(data)
                        except:
                            ServerClass.clients.remove(client)
            except:
                break
    
        ServerClass.clients.remove(conn)
        print("Lost connection")
        conn.close()

    @staticmethod
    def server():
        HOST = "192.168.0.50"
        PORT = 55555
        socketForServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socketForServer.bind((HOST, PORT))
        socketForServer.listen()

        print("Server is listening...")

        while True: 
            conn, addr = socketForServer.accept() 
            ServerClass.clients.append(conn)
            print("Connected to:", addr)

            clientHandler = threading.Thread(target=ServerClass.threaded_client, args=(conn,))
            clientHandler.start()

if __name__ == "__main__":
    ServerClass.server()


class Client:
    def __init__(self):
        self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = "192.168.0.50"
        self.port = 55555
        self.address = (self.host, self.port)
        self.player = None

    def connect(self):
        self.clientSocket.connect(self.address)
        print(self.clientSocket.recv(1048).decode())

    def sendPosition(self):
        data = self.player.send_position(self.clientSocket)
        if self.player:
            self.player.sendall(data)
        
    def receivePositions(self):
        data = self.player.receive_position(self.clientSocket)
        if self.player:
            return self.player.recv(data)
    
    def close(self):
        self.clientSocket.close()