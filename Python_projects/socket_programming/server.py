import socket
import threading

HEADER = 64
FORMAT ='utf-8'
DICMSG = "Terminate"

PORT = 5050
SERVERIP = socket.gethostbyname(socket.gethostname())
ADDRESS = (SERVERIP, PORT)


mainServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mainServer.bind(ADDRESS)

def service_client(conn, addr):
    print(f"New connection : {addr}")
    connected = True
    while connected:
        firstmsg = conn.recv(HEADER).decode(FORMAT)
        if firstmsg:
            msg_len = int(firstmsg)
            nextMsg = conn.recv(msg_len).decode(FORMAT)
            if nextMsg == DICMSG:
                connected = False

            print(f"[{addr}] -- {nextMsg}")
            conn.send("Message received".encode(FORMAT))
    conn.close()
    print(f"Connection closed {connected}")

def start():
    mainServer.listen()
    print(f"Server is listening on {SERVERIP}")
    while True:
        conn, addr = mainServer.accept()
        threadForCon = threading.Thread(target=service_client, args=(conn, addr))
        threadForCon.start()
        print(f"[Current connections {threading.activeCount()-1}")

print(f"Server is starting at {SERVERIP}:{PORT} ")
start()