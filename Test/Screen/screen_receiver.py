from vidstream import StreamingServer
import threading
from random import randint

port = randint(0, 65535)
print(f"Port of server is [{port}]")
print("Enter port address in Screen Sender to connect!")

receiver = StreamingServer('192.168.1.9', port)

receive_thread = threading.Thread(target=receiver.start_server)
receive_thread.start()

while input("") != "STOP":
    continue

receiver.stop_server()