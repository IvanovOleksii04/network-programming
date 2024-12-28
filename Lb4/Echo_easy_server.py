import socket

HOST = '127.0.0.1'  # Локальний хост
PORT = 65432        # Порт для зв'язку

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print(f"Server: {HOST}:{PORT}")
    conn, addr = server_socket.accept()
    with conn:
        print(f"Client: {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(f"Get: {data.decode()}")
            conn.sendall(data)
