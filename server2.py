import socket
import threading

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDRESS = (SERVER,PORT)
HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('[CREATED] Socket created.')
server.bind(ADDRESS)


def handle_client(client, address):
    print(f'[NEW CONNECTION] {address} connected.')
    connected = True
    while connected:
        msg_length = client.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = client.recv(msg_length).decode(FORMAT)
            print(f'[{address}] {msg}')
            
            if msg == DISCONNECT_MESSAGE:
                connected = False
    client.close()
        

def start():
    server.listen()
    print(f'[LISTENING] listening on server {SERVER}')
    while True:
        client, address = server.accept()
        thread = threading.Thread(target=handle_client, args=(client,address))
        thread.start()
        print(f'[ACTIVE CONNECTIONS] {threading.active_count() - 1}')
        
        
print('[STARTING] server is starting...')
start()
