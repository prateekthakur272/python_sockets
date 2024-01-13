import socket

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDRESS = (SERVER,PORT)
HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'



client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDRESS)


def send_msg(msg:str):
    msg = msg.encode(FORMAT)
    msg_length = len(msg)
    length_msg = str(msg_length).encode(FORMAT)
    length_msg += b' ' * (HEADER - len(length_msg))
    client.send(length_msg)
    client.send(msg)
  
while True:
    msg = input('[ENTER MESSAGE] ')
    send_msg(msg)
    if msg == DISCONNECT_MESSAGE:
        break
