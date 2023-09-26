import threading
import socket
from random import randint

host = '127.0.0.1'  # localhost
port = randint(0, 65535)
print(f'Port of the server: {port}')

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
usernames = []


# Function send message to client
def broadcast(message):
    for client in clients:
        client.send(message)


# Function handle client
def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            # Remove client and username in list of clients and usernames
            if client in clients:
                index = clients.index(client)
                clients.remove(client)
                client.close()
                username = usernames[index]
                broadcast(f'{username} left the chat!'.encode('ascii'))
                usernames.remove(username)
                print(f"{username} left the server!")
                break


# Function receive message
def receive():
    while True:
        client, address = server.accept()
        print(f"Connected with {str(address)}")

        client.send('NICK'.encode('ascii'))
        username = client.recv(1024).decode('ascii')

        usernames.append(username)
        clients.append(client)

        print(f'Username of the client is {username}!')
        broadcast(f'{username} join the chat!'.encode('ascii'))
        client.send('Connected to the server!'.encode('ascii'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


print("Server is listening...")
receive()
