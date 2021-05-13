import socket

HEADER = 1048
PORT = 8080
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client.connect(ADDR)

    text = "CONNECTED"
    while text != "$quit":
        text = input()
        if text == "$quit":
            print("Desconectando...")
        else:
            send(text)

    send("!DISCONNECT")
except:
    print("Servidor indisponível!\n Desconectando...")


