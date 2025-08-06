
import socket 
import os

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.connect(('172.27.167.156.', 1730))
file = input("Please enter a file path, either absolute or relative to simple-server \n")
fileName = input("please name the file (include type) \n")
my_socket.send(str(len(fileName)).zfill(2).encode())
my_socket.send(fileName.encode())

with open(file, 'rb') as file:
    fileConent = file.read()
my_socket.send(fileConent)

try:
    print(my_socket.recv(64).decode())
except:
    pass
my_socket.close()