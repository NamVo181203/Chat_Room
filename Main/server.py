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
            msg = message = client.recv(1024)
            if msg.decode('ascii').startswitch('KICK'):
                if usernames[clients.index(client)] == 'admin':
                    name_to_kick = msg.decode('ascii')[5:]
                    kick_user(name_to_kick)
                else:
                    client.send(f'Command was refuse!!!'.encode('ascii'))
            elif msg.decode('ascii').startswitch('BAN'):
                if usernames[clients.index(client)] == 'admin':
                    name_to_ban = msg.decode('ascii')[4:]
                    kick_user(name_to_ban)
                    with open('bans.txt', 'a') as f:
                        f.write(f'{name_to_ban}\n')
                    print(f'{name_to_ban} was banned!!!')
                else:
                    client.send(f'Command was refuse!!!'.encode('ascii'))
            else:
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

        with open('bans.txt', 'r') as f:
            bans = f.readlines()

        if username == 'admin':
            print("Admin is logining!!!")
            client.send('PASS'.encode('ascii'))
            password = client.recv(1024).decode('ascii')

            if password != 'admin123':
                client.send('REFUSE'.encode('ascii'))
                client.close()
                continue

        if username+'\n' in bans:
            client.send('BAN'.encode('ascii'))
            client.close()
            continue

        usernames.append(username)
        clients.append(client)

        print(f'Username of the client is {username}!')
        broadcast(f'{username} join the chat!'.encode('ascii'))
        client.send('Connected to the server!'.encode('ascii'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


# Function kick user
def kick_user(name):
    if name in usernames:
        index = usernames.index(name)
        client_to_kick = clients[index]
        clients.remove(client_to_kick)
        client_to_kick.send('You were kick by Admin!'.encode('ascii'))
        client_to_kick.close()
        usernames.remove(name)
        broadcast(f'{name} was kicked by Admin!!!'.encode('ascii'))


print("Server is listening...")
receive()
