print("starting server")
import socket
print("i'm working")
SERVER_PORT = 1730
SERVER_IP = '0.0.0.0'
SOCKET_TIMOUT = 10
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_IP, SERVER_PORT))
server_socket.listen(1)
print(f"Server listening on {SERVER_IP}:{SERVER_PORT}")  
while True:
    client_socket, address = server_socket.accept()
    raw_len = client_socket.recv(2).decode()
    file_name_len = int(raw_len)
    file_name = client_socket.recv(file_name_len).decode()
    with open(file_name, 'wb') as f:
        while True:
            try:
                client_socket.settimeout(SOCKET_TIMOUT)
                chunk = client_socket.recv(1024)
                if not chunk:
                    break
                f.write(chunk)
            except socket.timeout:
                break
    client_socket.sendall(b"file sent successfully")
    client_socket.close()
