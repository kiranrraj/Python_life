import socket


HEADER = 64
DICMSG = "Terminate"
FORMAT ='utf-8'

PORT = 5050
SERVERIP = socket.gethostbyname(socket.gethostname())
# print(SERVERIP)
ADDRESS = (SERVERIP, PORT)


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDRESS)
# print(ADDRESS)

def send(msg):
    msgToSend = msg.encode(FORMAT)
    msgLen = len(msgToSend)
    sendLen = str(msgLen).encode(FORMAT)
    sendLen += b' '*(HEADER - len(sendLen))
    client.send(sendLen)
    client.send(msgToSend)
    print(client.recv(2048).decode(FORMAT))

send("Hello World");

send(DICMSG)
