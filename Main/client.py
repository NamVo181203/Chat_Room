import socket
import threading

port = input("Enter port of server: ")
username = input("Enter a username: ")

port_int = int(port)
if username == 'admin':
    password = input("Enter admin password: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('192.168.1.9', port_int))

stop_thread = False


def receive():
    while True:
        global stop_thread
        if stop_thread:
            break

        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(username.encode('ascii'))
                next_massage = client.recv(1024).decode('ascii')
                if next_massage == 'PASS':
                    client.send(password.encode('ascii'))
                    if client.recv(1024).decode('ascii') == 'REFUSE':
                        print("Connection was refused! Wrong password")
                        stop_thread = True
                elif next_massage == 'BAN':
                    print('Connection refused because of ban!')
                    client.close()
                    stop_thread = True
            else:
                print(message)

        except:
            print("An error occurred!")
            client.close()
            break


# Function write message
def write():
    while True:
        if stop_thread:
            break
        message = f'{username}: {input("")}'
        if message[len(username)+2:].startswith('/'):
            if username == 'admin':
                if message[len(username)+2:].startswith('/kick'):
                    client.send(f'KICK {message[len(username)+2+6:]}'.encode('ascii'))
                elif message[len(username)+2:].startswith('/ban'):
                    client.send(f'BAN {message[len(username)+2+5:]}'.encode('ascii'))
            else:
                print("Permission denies! Commands can only executed by the Admin!")
        else:
            client.send(message.encode('ascii'))


receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
