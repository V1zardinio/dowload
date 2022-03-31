import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(('192.168.100.11', 32192))
    text = input('Сообщение: ')
    s.sendall(b(text))