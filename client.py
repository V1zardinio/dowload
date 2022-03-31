import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(('178.71.101.104', 32192))
    text = input('Сообщение: ')
    s.sendall(text.encode("utf-8"))

