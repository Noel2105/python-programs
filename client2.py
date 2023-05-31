import socket
import select
import sys

c = socket.socket()

c.connect(('192.168.69.141', 9999))
print('Connected to server')
name = input('Enter your name')
c.send(bytes(name, 'utf-8'))
while True:
    d1 = c.recv(1024).decode()
    print(d1)
    i = input()
    c.send(bytes(i, 'utf-8'))
    if i == 'bye':
        print('Connection terminated')
        break
