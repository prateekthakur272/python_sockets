import socket

server = socket.socket()
print('Socket created')

server.bind(('localhost', 8000))
server.listen(3)
print('Waiting for connections')

while True:
    client, address = server.accept()
    print(f'Connected with the client {address}')
    print(client.recv(1024).decode())
    client.send(bytes('Hello Sockets', 'utf-8'))
    client.close()