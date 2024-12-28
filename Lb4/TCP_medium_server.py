import socket

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print(f"Server {HOST}:{PORT}")
    while True:
        conn, addr = server_socket.accept()
        with conn:
            print(f"Client: {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    print(f"Client {addr} leave.")
                    break
                print(f"Get: {data.decode()}")
                conn.sendall(data)
