import socket
import time
def listen(sock):
    print(f'Start listening')
    sock.listen(1)
    conn, addr = sock.accept()
    print(f'Connection is done\n'
          f'client:{addr}')
    return (conn, addr)

print('Srart Server!')
sock = socket.socket()
sock.bind(('localhost', 9090))


(conn, addr) = listen(sock)

def Captions():
    print(f'get_mes len'.ljust(20), f"get_time".ljust(7),
          f'send_mes len'.ljust(20), f"send_time".ljust(7),
          sep="    ", end='\n')
Captions()
while True:

    data = conn.recv(1024).decode()

    t = time.strftime('%H:%M:%S', time.localtime())
    print(f'get_mes len: {len(data)}Byte'.ljust(20), f'{t}'.ljust(7), sep="    ",  end='    ')

    if data == 'None':
        data = f'-'
    data = f'Seerver: {data}'
    conn.send(data.encode())

    print(f'send_mes len: {len(data)}Byte'.ljust(20), f'{t}'.ljust(7), sep="    ", end='\n')
    if 'exit' in data.lower():
        print(f'\ndisconnect: {addr} ')
        print('Sock is close')
        conn, addr = listen(sock)
        Captions()
    if 'quit' in data.lower():
        print('Exit!')
        exit()

