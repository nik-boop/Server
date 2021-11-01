import socket, threading, sys

NAME = 'localhost'
PORT = 50000
sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
servaddr = (NAME, PORT)

nik_name = input('Write you`r nik: ')

sock.sendto(f'nik<>{nik_name}'.encode(), servaddr)
sock.recvfrom(1024)
sock.setblocking(False)
fex = False
def Exit():
    global fex
    fex = True


def send():
    while True:
        data = input()
        try:
            sock.sendto(data.encode(), servaddr)
            if data == 'exit':
                Exit()
        except socket.error as err:
            print(1, err)


def getmes():
    while True:
        try:
            try:
                data, addr = sock.recvfrom(1024)
                data = data.decode()
            except BlockingIOError as err:
                pass
            else:
                if data == 'exo':
                    sock.sendto('exo'.encode(), addr)
                else:
                    print(addr, data)
        except socket.error as err:
            print(err)


sendt = threading.Thread(target=send, name='send')
sendt.daemon = True
sendt.start()
getmest = threading.Thread(target=getmes, name='get')
getmest.daemon = True
getmest.start()

while True:
    if fex:
        exit()