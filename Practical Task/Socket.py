import socket
import threading

ip_address = input('Input IP: ')

def port_scan(ip_adress ,port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    try:
        connect = sock.connect((ip_adress, port))
        print(f'Port: {port} is open!')
        sock.close()
    except:
        pass


for i in range(1000):
    stream = threading.Thread(target=port_scan, args=(ip_address, i))
    stream.start()
