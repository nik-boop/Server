#!/usr/bin/env python

import socket

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)
conn, addr = sock.accept()

print('connected:', addr)

while True:
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        conn.send(data.upper().encode())
        if "exit".lower() in data:
            break
    if ("exit".lower() in data) or not data:
        break
conn.close()