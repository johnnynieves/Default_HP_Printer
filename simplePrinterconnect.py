import socket

HEADER = 64
PORT = 23
SERVER = "10.0.107.22"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    message = msg.encode("ascii")
    msg_length = len(message)
    send_length = str(msg_length).encode("ascii")
    send_length += b" " * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    # print(client.recv(2048).decode("ascii"))


send('support-contact Test message')
send('exit')
send('Y')
"""
find out how to send json file with printer data
"""

print('Send Json config file')
client.close()
