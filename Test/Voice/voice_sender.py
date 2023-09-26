from vidstream import AudioSender
import threading

port = input("Enter port of server: ")
port_int = int(port)
print("Connecting... Wait a second!!!")

sender = AudioSender('192.168.1.14', port_int)

send_thread = threading.Thread(target=sender.start_stream)
send_thread.start()

while input("") != "STOP":
    continue

sender.stop_stream()