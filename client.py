import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(('26.247.253.157/8', 32192))
    text = input('Сообщение: ')
    s.sendall(text.encode("utf-8"))

