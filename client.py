import socket

HOST = '192.168.100.11'  # The server's hostname or IP address
PORT = 32192             # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'say hello')