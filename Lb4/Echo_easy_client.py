import socket

HOST = '127.0.0.1'
PORT = 65432
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))
    while True:
        print('--------------')
        print('*Enter 0 to exit*')
        message = input("Enter your message: ")
        if message.lower() == '0':
            print('SERVER IS OVER')
            break
        client_socket.sendall(message.encode())
        data = client_socket.recv(1024)
        print(f"Server: {data.decode()}")
