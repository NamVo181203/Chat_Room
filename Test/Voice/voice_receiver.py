from vidstream import AudioReceiver
import threading
from random import randint

port = randint(0, 65535)
print(f"Port of server is [{port}]")
print("Enter port address in Voice Sender to connect!")

receiver = AudioReceiver('192.168.1.14', port)

receive_thread = threading.Thread(target=receiver.start_server)
receive_thread.start()

while input("") != "STOP":
    continue

receiver.stop_server()