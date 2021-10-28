import socket
def listen(sock):
    print(f'Start listening ')
    sock.listen(1)
    conn, addr = sock.accept()
    print(f'connection done\n'
          f'client:{addr}')
    return (conn, addr)

print('Srart Server!')
sock = socket.socket()
sock.bind(('localhost', 9090))


(conn, addr) = listen(sock)


while True:
    data = conn.recv(1024).decode()
    print(f'get_mes\n'
          f'    len: {len(data)}Byte')


    conn.send(data.upper().encode())
    print(f'send_mes\n'
          f'    len: {len(data)}Byte')
    if 'exit' in data.lower():
        print('Sock is close')
        conn, addr = listen(sock)
    if 'quit' in data.lower():
        print('Exit!')
        exit()

