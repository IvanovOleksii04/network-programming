import socket

HOST = '127.0.0.1'
PORT = 65433

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))
    file_path = input("Add path to file: ")
    try:
        with open(file_path, "rb") as file:
            while chunk := file.read(1024):
                client_socket.sendall(chunk)
        print("Файл успішно відправлено.")
    except FileNotFoundError:
        print("Файл не знайдено. Перевірте шлях.")
