import socket

client = socket.socket()

client.connect(('localhost',8000))

name = input('Enter message: ')
client.send(bytes(name,'utf-8'))

print(client.recv(1024).decode())
client.close()