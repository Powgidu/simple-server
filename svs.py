import socket

SERVER_PORT = 1729
SERVER_IP = '0.0.0.0'

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_IP, SERVER_PORT))
server_socket.listen(1)
while True:
    client_socket, address = server_socket.accept()
    client_socket.settimeout(1.412)
    raw_len = client_socket.recv(2).decode()
    file_name_len = int(raw_len)
    file_name = client_socket.recv(file_name_len).decode()
    with open(file_name, 'wb') as f:
        while True:
            try:
                chunk = client_socket.recv(1024)
                if not chunk:
                    break
                f.write(chunk)
            except socket.timeout:
                break
    client_socket.sendall(b"file sent successfully")
    client_socket.close()
