import socket
import threading

HEADER = 64
PORT = 5056
SERVER = socket.gethostbyname(socket.gethostname())
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ADDR = (SERVER, PORT)
server.bind(ADDR)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = 'BYEBYE'

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    connected = True
    while connected:
        msglen = conn.recv(HEADER).decode(FORMAT)
        if msglen:
            msglen = int(msglen)
            msg = conn.recv(msglen).decode(FORMAT)
            print(f"[{addr}] {msg}")
            if msg == DISCONNECT_MESSAGE:
                connected = False
            if msg.endswith('over') or msg.endswith('OVER'):
                while True:
                    sm = input()
                    m = sm.encode(FORMAT)
                    conn.send(m)
                    if sm.endswith('over') or sm.endswith('OVER'):
                        break
    conn.close()
def start():
    server.listen()
    print(F"[LISTENING] server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target = handle_client, args = (conn, addr))
        thread.start()
        print(f"[ACTIVE_CONNECTIONS] {threading.activeCount() - 1}")

print("[STARTING] server is starting")
start()




CLIENT CODE

import socket

HEADER = 64
PORT = 5056
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = 'BYEBYE'
SERVER = '127.0.1.1'
ADDR = (SERVER,PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msglen = len(message)
    send_length = str(msglen).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    if msg.endswith('over') or msg.endswith('OVER'):
        while True:
            m = client.recv(2048).decode(FORMAT)
            print("SERVER: ",m)
            if m.endswith('over') or m.endswith("OVER"):
                break




while True:
    m = input()
    if m == 'BYEBYE':
        send(m)
        break
    else:
        send(m)
