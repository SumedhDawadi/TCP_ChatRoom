import threading
import socket

hosts = '127.0.0.1' #Loopback address
port = 55555
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(hosts,port)
server.listen()
clients = []
nicknames = []

def broadcast(message):
    for clients in clients:
        clients.send(message)
def handle(clients):
    while True:
        try:
            message = clients.recv(1024)
            broadcast(message)
        except:
            index = clients.index(clients)
            clients.remove(clients)
            nicknames = nicknames[index]
            broadcast(f'(nicknams) Left the chat room'.encode('ascii'))
            nicknames.remove(nicknames)
            break
