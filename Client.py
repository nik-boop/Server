import socket

sock = socket.socket()
sock.connect(('localhost', 9090))
print(f'Conectin is done',
      f'    my: {sock.getsockname()}',
      f'server: {sock.getpeername()}', sep='\n')

while True:

    word = input('Message: ')
    if word == '':
        word = f'{None}'
    sock.send(word.encode())
    if "exit" in word.lower() or "quit" in word.lower():
        sock.close()
        print('Soket close')
        exit()


    data = sock.recv(1024).decode()
    print(f'{data}\n')
